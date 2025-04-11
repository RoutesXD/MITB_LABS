import re

# Slang and emoji dictionaries
slang_dict = {
    r"\bu\b": "you",
    r"\bur\b": "your",
    r"\br\b": "are",
    r"\blol\b": "laughing out loud",
    r"\bomg\b": "oh my god",
    r"\bidk\b": "I don't know",
    r"\btbh\b": "to be honest",
    r"\bbtw\b": "by the way",
    r"\bgr8\b": "great",
    r"\bb4\b": "before",
    r"\bbrb\b": "be right back",
    r"\blmk\b": "let me know",
    r"\bsmh\b": "shaking my head",
    r"\bnp\b": "no problem"
}

emoji_dict = {
    "😂": "laughing",
    "😊": "smiling",
    "😢": "crying",
    "❤️": "love",
    "👍": "thumbs up",
    "😡": "angry",
    "😭": "crying",
    "🔥": "fire",
    "🙌": "celebrate",
    "😎": "cool",
}

def normalize_text(text):
    # Replace emojis
    for emoji, word in emoji_dict.items():
        text = text.replace(emoji, f" {word} ")

    # Replace slangs
    for pattern, replacement in slang_dict.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Normalize punctuation (e.g., "!!!" -> "!")
    text = re.sub(r"([!?.,])\1+", r"\1", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Convert to lowercase
    text = text.lower()

    return text

# Test input
text1 = "OMG!!! 😂😂 idk what u were thinking!!! this is gr8!!! 😊😊"
text2 = "SMH... I can't believe it!!! LOL omg 😂🔥"

# Test the function
print("Original:", text1)
print("Processed:", normalize_text(text1))
print("\nOriginal:", text2)
print("Processed:", normalize_text(text2))
