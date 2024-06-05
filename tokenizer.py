import pickle
import numpy as np

def load_tokenizer(tokenizer_file):
    with open(tokenizer_file, 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

def tokenize_text(text, tokenizer):
    tokens = tokenizer.texts_to_sequences([text])[0]
    return np.array(tokens)

if __name__ == "__main__":
    import sys
    tokenizer_file = sys.argv[1]
    text = sys.argv[2]

    # Load tokenizer
    tokenizer = load_tokenizer(tokenizer_file)

    # Tokenize text
    tokens = tokenize_text(text, tokenizer)
    print(tokens)
