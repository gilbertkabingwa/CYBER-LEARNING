#What is a data type?
"""a data type is a classification that tells the computer what kind of value a variable holds and what operations can be performed on it"""

""""Python uses **data types** to define what kind of value a variable contains.

# ==========================================
# PYTHON DATA TYPES
# No Value -> Single Value -> Multi-Values
# ==========================================


# ==========================================
# 1. NO VALUE
# ==========================================

# None means that a variable has NO value.
# It is not 0, it is not False, and it is not an empty string.
# It simply means "nothing" or "no value".

result = None

print(result)
print(type(result))

# Output:
# None
# <class 'NoneType'>


# Example:
# A function can return None when there is no result.

user_result = None

if user_result is None:
    print("There is no value.")


# IMPORTANT:
# Use "is None" when checking for None.

if result is None:
    print("Result is empty.")


# ==========================================
# 2. SINGLE VALUE
# ==========================================

# A single-value data type represents ONE value.

# ------------------------------------------
# INTEGER (int)
# ------------------------------------------

# int = whole number

age = 25
score = 100
year = 2026

print(age)
print(type(age))

# <class 'int'>


# ------------------------------------------
# FLOAT (float)
# ------------------------------------------

# float = number with a decimal

height = 160.5
price = 19.99

print(height)
print(type(height))

# <class 'float'>


# ------------------------------------------
# STRING (str)
# ------------------------------------------

# str = text

name = "Gilbert"
country = "Rwanda"

print(name)
print(type(name))

# <class 'str'>


# A string is still ONE value,
# even though it contains multiple characters.

name = "Gilbert"

# "Gilbert" is one string value.


# ------------------------------------------
# BOOLEAN (bool)
# ------------------------------------------

# bool = True or False

is_student = True
is_raining = False

print(is_student)
print(type(is_student))

# <class 'bool'>


# ==========================================
# SINGLE VALUE SUMMARY
# ==========================================

age = 25              # int
height = 160.5        # float
name = "Gilbert"      # str
is_student = True     # bool

# Think:
#
# int   -> whole number
# float -> decimal number
# str   -> text
# bool  -> True / False


# ==========================================
# 3. MULTI-VALUES
# ==========================================

# Multi-value data types can store
# multiple pieces of data inside ONE variable.


# ==========================================
# LIST
# ==========================================

# list = ordered collection
# Lists are CHANGEABLE (mutable).

fruits = ["apple", "banana", "orange"]

print(fruits)
print(type(fruits))

# <class 'list'>


# Access one item using its index.
# Python starts counting from 0.

print(fruits[0])
# apple

print(fruits[1])
# banana

print(fruits[2])
# orange


# You can change a list.

fruits[0] = "mango"

print(fruits)

# ['mango', 'banana', 'orange']


# You can also add a new item.

fruits.append("apple")

print(fruits)


# ==========================================
# TUPLE
# ==========================================

# tuple = ordered collection
# A tuple CANNOT normally be changed after creation.

coordinates = (10, 20)

print(coordinates)
print(type(coordinates))

# <class 'tuple'>


print(coordinates[0])
# 10

print(coordinates[1])
# 20


# This would cause an error:
#
# coordinates[0] = 50
#
# Because tuples cannot be changed.


# ==========================================
# SET
# ==========================================

# set = collection of UNIQUE values.
# Duplicate values are automatically removed.

numbers = {1, 2, 3, 4}

print(numbers)
print(type(numbers))

# <class 'set'>


# Duplicate values disappear.

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

# {1, 2, 3, 4}


# Sets are useful when you only care about
# unique values.


# ==========================================
# DICTIONARY
# ==========================================

# dict = collection of KEY : VALUE pairs.

person = {
    "name": "Gilbert",
    "age": 25,
    "country": "Rwanda"
}

print(person)
print(type(person))

# <class 'dict'>


# Access a value using its key.

print(person["name"])
# Gilbert

print(person["age"])
# 25

print(person["country"])
# Rwanda


# You can change dictionary values.

person["age"] = 26

print(person["age"])
# 26


# You can add new key/value pairs.

person["city"] = "Kigali"

print(person)


# ==========================================
# MULTI-VALUE SUMMARY
# ==========================================

fruits = ["apple", "banana", "orange"]   # list

coordinates = (10, 20)                  # tuple

numbers = {1, 2, 3, 4}                  # set

person = {
    "name": "Gilbert",
    "age": 25
}                                       # dict


# Think:
#
# list  -> ordered + changeable
# tuple -> ordered + NOT changeable
# set   -> unique values
# dict  -> key : value


# ==========================================
# THE BIG PICTURE
# ==========================================

# PYTHON DATA TYPES
#
# NO VALUE
#     |
#     └── None
#
# SINGLE VALUE
#     |
#     ├── int
#     ├── float
#     ├── str
#     └── bool
#
# MULTI-VALUES
#     |
#     ├── list
#     ├── tuple
#     ├── set
#     └── dict


# ==========================================
# VERY IMPORTANT EXAMPLES
# ==========================================

x = None
# No value

x = 25
# One integer value

x = 25.5
# One float value

x = "Hello"
# One string value

x = True
# One boolean value

x = ["Apple", "Banana", "Orange"]
# Multiple values in a list

x = (10, 20, 30)
# Multiple values in a tuple

x = {1, 2, 3}
# Multiple unique values in a set

x = {"name": "Gilbert", "age": 25}
# Multiple key/value pairs in a dictionary


# ==========================================
# TYPE()
# ==========================================

# Use type() to check what type of data you have.

x = 25

print(type(x))

# <class 'int'>


x = "Hello"

print(type(x))

# <class 'str'>


x = [1, 2, 3]

print(type(x))

# <class 'list'>


# ==========================================
# EASY MEMORY RULE
# ==========================================

# None
#     = Nothing
#
# int
#     = Whole number
#
# float
#     = Decimal number
#
# str
#     = Text
#
# bool
#     = True / False
#
# list
#     = Ordered + changeable collection
#
# tuple
#     = Ordered + unchangeable collection
#
# set
#     = Unique values
#
# dict
#     = Key : Value pairs

These four are the most important basic Python data types to know first."""