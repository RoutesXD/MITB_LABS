import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Downloads
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def custom_tokenizer(text):
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove mentions and hashtags
    text = re.sub(r'[@#]\w+', '', text)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t.lower() not in stop_words]
    return tokens

def stem_and_lemmatize(tokens):
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stemmed = [stemmer.stem(t) for t in tokens]
    lemmatized = [lemmatizer.lemmatize(t) for t in tokens]
    return stemmed, lemmatized

# Example usage
text = "Hey @user, check out https://example.com! This is #awesome. Loved it on 12/12/2022 😊"

tokens = custom_tokenizer(text)
stemmed, lemmatized = stem_and_lemmatize(tokens)

print("Cleaned Tokens:", tokens)
print("Stemmed:", stemmed)
print("Lemmatized:", lemmatized)
