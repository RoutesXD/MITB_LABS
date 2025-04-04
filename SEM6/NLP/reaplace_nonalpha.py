import re

def replace_non_alnum(sentence, replacement_char):
    return re.sub(r'[^a-zA-Z0-9]', replacement_char, sentence)

text = "Hello, world! 123 @#$"
replacement = "*"

result = replace_non_alnum(text, replacement)
print(result)
