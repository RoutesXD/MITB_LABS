import random

def random_splits(word):
    positions = list(range(1, len(word)))  
    random.shuffle(positions)  
    
    splits = [(word[:i], word[i:]) for i in positions]
    return splits

word = "CARRIED"
splits = random_splits(word)

for part1, part2 in splits:
    print(f"({part1}, {part2})")
