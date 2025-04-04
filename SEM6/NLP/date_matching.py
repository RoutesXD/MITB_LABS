import re

text = "Today's date is 04/04/2025. Another date might be 15/12/2023 or even 31/01/1999."

# Regex pattern for DD/MM/YYYY
pattern = r'\b\d{2}/\d{2}/\d{4}\b'

dates = re.findall(pattern, text)
print(dates)
