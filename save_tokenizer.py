from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

# Misalnya, teks pelatihan yang digunakan untuk membuat tokenizer
texts = ["This is a sample text", "Another example text for tokenizer"]

# Membuat tokenizer
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)

# Menyimpan tokenizer
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Tokenizer saved successfully.")
