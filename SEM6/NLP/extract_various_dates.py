import re

def extract_dates(text):
    pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4})\b'
    dates = re.findall(pattern, text, flags=re.IGNORECASE)
    return dates

# Example usage
text = "We met on 12/05/2023, another event was on 05-14-2022, and we have a meeting on March 10, 2024."
dates = extract_dates(text)
print(dates)  # Output: ['12/05/2023', '05-14-2022', 'March 10, 2024']
