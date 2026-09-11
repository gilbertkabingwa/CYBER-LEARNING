# String functions
"""A string value is just a text in between double quotes or single quotes and you can put between the quotes anything you want like ex. name or numbers or other things"""

# Why is handling string data important?
"""Text is everywhere:
- Filenames
- User input
- Web data
- Logs
# 80% of real world data is just text. Text often holds valuable information."""

# Srting Functions types:

# Types:
name = "Gilbert"
print(type(name))
# OR
age = 24
print(type(age))
# Python is flexible with data types but watch out! You can change a value's Python will treat it differently 

# String functions MATH:

# MATH:

# Length = len()
password = "1234am"
print(len(password))

if len(password)<8:
    print("Your Password is too short!")
# len() counts everything, even spaces.
# Use Case - Validate Input Length. Prevent value that are too short or too long

# Count:
text = """
Gilbert is king
Gilbert is Boss
Gilbert is nice"""

print(text.count("Gilbert"))
# Python is case-sensitive, means uppercase and lowrcase latters are treated as different.
# Use case- Detect issues count how many unwanted characters in my data

# Example
text = """
Gilbert is king
Gilbert is Boss
Gilbert is nice!"""

print(text.count("!"))