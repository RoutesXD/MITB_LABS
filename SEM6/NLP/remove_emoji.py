import re
import emoji

def remove_emojis(text):
    text = emoji.replace_emoji(text, replace='')  # Removes emojis
    text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F]+', '', text)
    return text

# Example usage
text = "Hello 😊! How are you? 🚀🔥"
cleaned_text = remove_emojis(text)
print(cleaned_text)  # Output: Hello ! How are you?
