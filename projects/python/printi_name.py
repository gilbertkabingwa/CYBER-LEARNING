#  #Challenge 1 - DINOSAUR
"""Practicing the `print()`function by printing a pattern—in this case, I chose a dinosaur."""

print("...........__")
print("........../  _)")
print("...*-^^^-/  /..")
print("__/......../...")
print("<__.|_|-|_|...")

print("==" * 40)

# #Challenge 2 - Personal Profile 
"""This profile project outputs the desired information such as profile data—based on a query."""

name = input("What is your name?: ")
age = int(input("Enter your age: "))
country = "Finland"
student = input("Are you a student?: ")
height = float(input("What is your height?: "))

print("My name is", name)
print("My age is", age)
print("I was born in", country)
print("Student:", student)
print("My height is", height)


# Challenge 3 — Create a Menu
"""Create a restaurant menu using print()."""

print("==" * 12)
print("     RESTAURANT   ")
print("==" * 12)

Menu = "1. Burger\t €12.90\n2. Pizza\t €14\n3. Chicken\t €13.80\n4. Salad\t €6\n5. Water\t €3"
print (Menu)

print("==" * 12)
print("     MENU END   ")
print("==" * 12)

# Challenge 4 — Clean a Name
"""You receive messy information: name = "   maria   " or name = "   mArIa kAbInGwA   " """

# Origanl data 
name = "   maria   "
name2 = "   mArIa kAbInGwA   "
print(name, name2)

# Cleaned data 

name2 = "   mArIa kAbInGwA   ".strip().lower()
name = "   maria   ".strip().upper()
print(name2)
print(name)
print("==" * 40)

# Challenge 6 — Age Calculator

""" Create a program that asks: 
What is your name?
What year were you born?"""

namy = input("What is your name?: ")
age = int(input("What year were you born?: "))
print("Hello Maria")
print("You are approximately 27 years old")
print("==" * 40)

# Challenge 6 — Employee Information
""" You receive this data:
employee_id = "968-MARIA"
employee_name = "maria kabingwa"
department = "CYBERSECURITY"
job = "security engineer"

Your task is to clear it """

# Cleaned data: 

print("==" *15)
print("     EMPLOYEE PROFILI    ")
print("==" *15)
print()
ID = "968-Maria".lower()
Name = "maria kabingwa".title()
Department = "CYBERSECURITY".title()
Job = "security engineer".title()

print("ID: ",ID) 
print("Name: ",Name) 
print("Department: ",Department)
print("Job: ",Job)
print()
print("==" *15)

# Challenge 7 — Clean Messy Data

"""name = "   968-Maria   "
job = " (SECURITY ENGINEER) "
country = " rWAnDa "
age = " 27 """

# Clean Data
# Clean name
name = name.strip().removeprefix("968-").title()

# Clean job
job = Job.strip("() ").title()

# Clean country
country = country.strip().title()

# Clean age
age = int(age.strip())

# Display cleaned data
print("Name:", name)
print("Job:", job)
print("Country:", country)
print("Age:", age)

print("==" * 15)

# Challenge 8 — Personal Information System
"""Create a program that asks the user:"""

# Creat title for our profile
print("=="*15)
print("     PERSONAL PROFILE")
print("=="*15)
print()

# Creating base information 
name = input("What is your name?:")
age = int(input("What is your age?:"))
country = input("Country?:")
city = input("Enter the city you're from:")
job = input("What do you do for living?:")
company = input("In which company do you work for?:")
food = input("What is your favorite food?:")
hobby = input("What is your favorite hobby?:")


# Display personal information: 
print("My name is", name)
print("Age",age)
print("I'm from", country)
print("I live in", city)
print("I work as",job,"for", company)
print("My favorite food is", food, "and i love eating that food so much")
print("and my favorite hobby is", hobby)

# Creat the finishing touches
print()
print("=="*15)
print("     PROFILE CREATED ")
print("=="*15)

# Challenge 9 — Employee Registration System

"""Now lets combine everything we have learned so far. Create a program that registers an employee. The program should ask:"""

# Creat title for our profile
print("=="*15)
print("      EMPLOYEE REGISTRATION")
print("=="*15)
print()

# Creating base information 
ID = int(input("Enter employee ID:"))
name1 = input("Enter first name::")
name2 = input("Second name:")
age = int(input("Enter your age:"))
country = input("Which country are you from?:")
job = input("What you do for living?:")
department = input("In which department you work in?:")



# Display personal information: 
print("Employee ID:", ID)
print("Name:",name1, name2)
print("Age:",age)
print("Country:", country)
print("Job:",job)
print("Department:",department)

# Creat the finishing touches
print()
print("=="*15)
print("    REGISTRATION COMPLETE")
print("=="*15)

# LEVEL 10 — Realistic Challenge 🔥🔥
# Challenge 10 — Data Cleaning System

"""Imagine you work as a Junior Data Engineer.

Your company gives you this messy data:
employee_id = " 968- "
name = " maria "
lastname = " KABINGWA "
age = " 27 "
job = " (security engineer) "
country = " rWAnDa " 

Your job is to clean the data."""