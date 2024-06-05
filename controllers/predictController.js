const tf = require('@tensorflow/tfjs-node');
const { execSync } = require('child_process');
const fetch = require('node-fetch');

// URL publik untuk model
const modelUrl = 'https://storage.googleapis.com/equilibrare-425011.appspot.com/Model%20Prediction%20Equilibrare/model.json';

let model;

// Fungsi untuk memuat model
const loadModel = async () => {
  try {
    const response = await fetch(modelUrl);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const modelJson = await response.json();
    model = await tf.loadLayersModel(tf.io.browserHTTPRequest(modelUrl));
    console.log('Model loaded');
  } catch (error) {
    console.error('Error loading model:', error);
  }
};

// Fungsi untuk melakukan prediksi
const predictAnxiety = async (req, res) => {
  try {
    // Ambil input teks dari body request
    const inputText = req.body.input;

    // Jalankan skrip Python untuk pra-pemrosesan teks
    const cleanedText = execSync(`python3 preprocess/preprocess.py "${inputText}"`).toString().trim();
    const tokenizedText = JSON.parse(execSync(`python3 -c 'import preprocess; print(preprocess.tokenize_text(${JSON.stringify(cleanedText)}))'`).toString().trim());

    // Lakukan prediksi
    const prediction = model.predict(tf.tensor(tokenizedText));
    const predictionValue = prediction.arraySync()[0][0];

    // Tentukan hasil berdasarkan ambang batas 0.5
    const result = predictionValue > 0.5 ? 'Anxiety Detected' : 'Normal';

    // Kirim hasil prediksi sebagai respons JSON
    res.json({ prediction: predictionValue, result: result });
  } catch (error) {
    console.error('Error predicting anxiety:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
};

// Memuat model saat aplikasi dimulai
loadModel().catch(console.error);

// Ekspor fungsi predictAnxiety agar bisa digunakan di aplikasi Express
module.exports = { predictAnxiety };
