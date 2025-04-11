import re

def clean_text(text):
    # Remove hashtags (e.g., #example)
    text = re.sub(r'#\w+', '', text)
    
    # Remove mentions (e.g., @user)
    text = re.sub(r'@\w+', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove special characters except basic punctuation and space
    text = re.sub(r'[^\w\s.,!?]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Example usage
text = "Check out our new product! #launch @company Visit https://example.com now!!!"
cleaned = clean_text(text)

print("Original text:")
print(text)
print("\nCleaned text:")
print(cleaned)
