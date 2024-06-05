import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
import json
import pickle
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

MAX_SEQUENCE_LENGTH = 100  # Sesuaikan dengan model Anda

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # Hapus URL
    text = re.sub(r'\s+', ' ', text).strip()  # Hapus spasi berlebih
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return ' '.join(words)

def tokenize_text(text):
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    tokens = tokenizer.texts_to_sequences([text])[0]
    padded_tokens = pad_sequences([tokens], MAX_SEQUENCE_LENGTH)
    return np.array(padded_tokens).tolist()

def pad_sequences(sequences, maxlen):
    padded_sequences = np.zeros((len(sequences), maxlen))
    for i, seq in enumerate(sequences):
        if len(seq) > maxlen:
            padded_sequences[i] = seq[:maxlen]
        else:
            padded_sequences[i, -len(seq):] = seq
    return padded_sequences

if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    cleaned = clean_text(text)
    print(json.dumps(cleaned))
