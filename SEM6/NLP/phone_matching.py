import re

text = """
Call me at 123-456-7890 or (123) 456-7890.
My office line is 123.456.7890, and my old number was 123 456 7890.
"""

pattern = r'(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}'


matches = re.findall(pattern, text, re.VERBOSE)
print(matches)





