from collections import Counter
from nltk.util import ngrams
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

def ngram_frequencies(text, n=1):
    tokens = word_tokenize(text.lower())
    n_grams = ngrams(tokens, n)
    return Counter(n_grams)

# Example usage
sentence = "This is a test. This test is only a test."
frequencies = ngram_frequencies(sentence)

for gram, freq in frequencies.items():
    print(f"{' '.join(gram)}: {freq}")
