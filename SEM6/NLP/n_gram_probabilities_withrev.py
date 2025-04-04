from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def ngram_probabilities(text, n=2):
    tokens = word_tokenize(text.lower())
    n_grams = list(ngrams(tokens, n))
    total = len(n_grams)
    freq = Counter(n_grams)
    probabilities = {gram: count / total for gram, count in freq.items()}
    return probabilities

def reverse_ngrams(text, n=2):
    tokens = word_tokenize(text.lower())
    reversed_tokens = list(reversed(tokens))
    reversed_n_grams = list(ngrams(reversed_tokens, n))
    return reversed_n_grams

# Example usage
sentence = "This is a test. This test is only a test."
probs = ngram_probabilities(sentence, n=2)
rev_ngrams = reverse_ngrams(sentence, n=2)

for gram, prob in probs.items():
    print(f"{' '.join(gram)}: {prob:.3f}")

for gram in rev_ngrams:
    print(f"{' '.join(gram)}")
