def generate_prefixes_suffixes(word):
    prefixes = [word[:i] for i in range(1, len(word) + 1)]
    suffixes = [word[i:] for i in range(len(word))]

    return prefixes, suffixes

# Example usage
word = "CARRIED"
prefixes, suffixes = generate_prefixes_suffixes(word)

print("Prefixes:", prefixes)
print("Suffixes:", suffixes)
