import re

def normalize_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Example usage
text = "   This  is    a    SAMPLE   Text!  "
normalized_text = normalize_text(text)
print(normalized_text)  # Output: "this is a sample text!"
