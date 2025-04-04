import re

def count_non_alnum(sentence):
    non_alnum_chars = re.findall(r'[^a-zA-Z0-9]', sentence)
    return len(non_alnum_chars)

text = "Hello, world! 123 @#$"
count = count_non_alnum(text)
print(count)
