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

# Challenge 8 — Clean Messy Data

"""name = "   968-Maria   "
job = " (SECURITY ENGINEER) "
country = " rWAnDa "
age = " 27 """

# Clean Data
name = "   968-Maria   ".strip()
job = " (SECURITY ENGINEER) ".title()
country = " rWAnDa ".title()
age = " 27 ".strip()

print("name:",name)
print("Job:",job.replace("(","",).replace(")",""))
print("Country:",country.strip())
print("age:",age)