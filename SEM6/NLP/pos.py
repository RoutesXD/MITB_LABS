import nltk

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(tokens)

# Display results
print("Tokens with POS tags:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
