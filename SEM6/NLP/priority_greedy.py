import re
from nltk.tokenize import RegexpTokenizer

def prioritize_tokenizer(text):
    pattern = r'''(
        \d{1,2}/\d{1,2}/\d{2,4}        # Dates like 12/05/2023
        |[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}  # Emails
        |\w+                          # Words
        |[^\w\s]                      # Punctuation
    )'''

    tokenizer = RegexpTokenizer(pattern, flags=re.VERBOSE)
    return tokenizer.tokenize(text)

# Example usage
text = "Send an email to example123@test.com by 12/05/2023! Or contact backup@example.org on 1/1/24."

tokens = prioritize_tokenizer(text)
print(tokens)
