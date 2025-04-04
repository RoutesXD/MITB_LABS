def split_word(word):
    return [(word[:i], word[i:]) for i in range(1, len(word))]

# Example usage
word = "CARRIED"
result = split_word(word)
print(result)
