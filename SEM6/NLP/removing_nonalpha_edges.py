import re

def clean_sentence(sentence):
    sentence = re.sub(r'^[^a-zA-Z0-9]', '', sentence)
    
    sentence = re.sub(r'[^a-zA-Z0-9]$', '', sentence)
    
    return sentence

# Example usage
text = "!Hello, world!?"
cleaned = clean_sentence(text)
print(cleaned)
