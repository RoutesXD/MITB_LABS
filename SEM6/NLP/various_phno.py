import re

def standardize_phone_numbers(text):
    pattern = r'(\+?\d{1,3})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})'
    matches = re.findall(pattern, text)

    standardized_numbers = []
    for match in matches:
        country_code = match[0] if match[0] else "+1"  # Default to +1 if no country code
        standardized = f"{country_code} ({match[1]}) {match[2]}-{match[3]}"
        standardized_numbers.append(standardized)

    return standardized_numbers

# Example usage
text = "Call me at 123-456-7890 or (987) 654-3210. Also, reach me at +44 20 7946 0958."
phone_numbers = standardize_phone_numbers(text)
print(phone_numbers)
