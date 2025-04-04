import re

def split_text(text):
    tokens = re.split(r'[^\w]+', text)
    tokens = [token for token in tokens if token]
    return tokens

sample_text = """Hello there!
This is a sample text, with punctuation marks... and new lines.\nAlso, carriage returns\rshould be handled too."""

tokens = split_text(sample_text)
print(tokens)
