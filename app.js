const express = require('express');
const bodyParser = require('body-parser');
const predictRoutes = require('./routes/predictRoutes');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());
app.use('/api', predictRoutes);

// Hapus impor downloadModel dan panggilannya di sini

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
