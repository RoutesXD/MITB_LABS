import math
from collections import Counter
import pandas as pd

def calculate_shannon_entropy(data):
    counts = Counter(data)
    total_count = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        probability = count / total_count
        entropy -= probability * math.log2(probability)
    return entropy

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Available columns in the Titanic dataset:")
print(df.columns.tolist())

column = input("Enter the column name to calculate Shannon entropy: ")

if column in df.columns:
    data = df[column]
    entropy = calculate_shannon_entropy(data)
    print(f"Shannon Entropy of the column '{column}': {entropy}")
else:
    print(f"Column '{column}' not found in the dataset. Please try again.")
