import pandas as pd
import re
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.columns)
def match_pattern(data, column, pattern):
    matched_results = []
    for value in data[column]:
        if re.match(pattern, str(value)):  
            matched_results.append(value)
    return matched_results

def get_user_input():
    print("Available columns to search: 'name', 'age', 'sex', 'survived', 'pclass'")
    column = input("Enter the column name to search: ").lower()

    if column not in ['name', 'age', 'sex', 'survived', 'pclass']:
        print("Invalid column name. Please enter a valid column name.")
        return

    pattern = input(f"Enter the pattern to match in the '{column}' column: ")
    matched_results = match_pattern(titanic, column, pattern)

    if matched_results:
        print(f"\nFound {len(matched_results)} matches for the pattern '{pattern}' in column '{column}':")
        for result in matched_results:
            print(result)
    else:
        print(f"\nNo matches found for the pattern '{pattern}' in column '{column}'.")

def main():
    print("Welcome to the Titanic Dataset Pattern Matching Program using Regular Expressions!")
    
    while True:
        get_user_input()
        again = input("\nDo you want to search again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the program! Goodbye.")
            break

main()
