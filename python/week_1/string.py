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

# Type() and STR():
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

# Count():
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

# Transformattions
# Replace()

# Example:
price ="12345,6"
print(price.replace(",","."))

# Replace (old, new) str method, output: str. Swaps part of text with something new.
# Replace() is not just for changing values, you can also remove unwanted parts by replacing them with an empty string ("")

# Example:
price ="12345/6"
print(price.replace("/",""))
# OR
price ="€123/45/6"
print(price.replace("€","").replace("/", " "))

# Chained methods are executed in order from left to right. Each replace() runs on the result of the one before it.

# Challenge
# Convert the messy phone number into a clean number format wtith digits
"""+49 (176) 123-4567"""

# Result:
phone = "+49 (176) 123-4567"
print(phone.replace("+49 (176) 123-4567","00491761234567"))