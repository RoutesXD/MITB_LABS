from nltk.tokenize import RegexpTokenizer

def process_digits(text):
    digit_tokenizer = RegexpTokenizer(r'\d+')
    digits = digit_tokenizer.tokenize(text)
    
    nondigit_tokenizer = RegexpTokenizer(r'[^\d]+')
    non_digits = nondigit_tokenizer.tokenize(text)
    cleaned_text = ''.join(non_digits).strip()
    
    return {
        'digit_count': len(digits),
        'extracted_digits': digits,
        'text_without_digits': cleaned_text
    }

# Example usage
sentence = "My phone number is 12345 and pin is 6789."
result = process_digits(sentence)

print("Count of digits:", result['digit_count'])
print("Extracted digits:", result['extracted_digits'])
print("Text without digits:", result['text_without_digits'])
