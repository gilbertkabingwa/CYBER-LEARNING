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

# Joing Strings 
first_name = "Romio"
last_name = "Julia"
last_name = first_name + " " + last_name
print (last_name)

# Other way
folder = "C:/users/romio/"
file = "repor.csv"
full_folder_path = folder + file
print(full_folder_path)
# Use Case - Build Paths. Build dynamic using folder and file variables

# f-string
name = "Romeo"
age = 34
is_student = False
# Old way of printing output
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".")

# NEW WAY
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

# By using F-STRING way is shorter, cleaner, it is easier to read.

# SPLIT()
# SPLIT(separator) str method output: list of strings, breaks a string into smaller parts

#Example:
info = "2026-10-11,Finland,Helsinki,"
print(info.split(","))

# STRING REPETITION
# "String" * number operator output: string, repeats the string multiple times

#exaple 
print("==" *21)
print("YES, Im boss. "* 3)
print("==" *21)
# Use repeated characters to create clear sections in output

# Indexing & Slicing
"""(+) Positive index 0 1 2 3 4 5 ..
# (-) Negative index -5 -4 -3 -2 -1 """

# Example:

# Extract the first charact
test = "Gilbert"
print(text[1])
# OR
print (text[7])
# Same on negative indext 
print (text[-0])

#indexes & Slicing 
date = "2026-10-10"
# Extract the year 
print(date[0:4])
print(date[:4])

# Extract the mouth
print(date[5:7])

# Extract the day
print(date[8:])
print(date[-2:])

# Use positive indexex if you want to extract part from the lefe side (start) of a string
# Use Negative indexes if you want to extract part from the right right side (end) of a string


# Remove space
# Whitespace Cleanup
text = " Gilbert".lstrip()
print(test)

text = "Gilbert ".rstrip
print(text)

text = " Gilbert " .strip