import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
import json, requests

stemmer = PorterStemmer()

#nltk.download('punkt')

def tokenize(phrase):
    return nltk.word_tokenize(phrase)

def stem(word) :
    return stemmer.stem(word.lower())

def word_bag(tokenized_phrases, all_words):
    tokenized_phrases = [stem(w) for w in tokenized_phrases]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w, in enumerate(all_words):
        if w in tokenized_phrases:
            bag[idx] = 1.0
    return bag

def get_kitty():
  response = requests.get('https://api.thecatapi.com/v1/images/search')
  json_data = json.loads(response.text)
  img_url = json_data[0]["url"]
  return img_url