#  Use Print() # Dinosaur

print("...........__")
print("........../  _)")
print("...*-^^^-/  /..")
print("__/......../...")
print("<__.|_|-|_|...")



# Project: Personal Profile 

person = {
    "name": "Romion Kalle",
    "age": 35,
    "country": "Finland",
    "Student?": "Yes",
    "Hight": "180cm"
}
print(person)

 # Other way

name = str(input("What is your name?:"))
age = input("Enter your age:")
country = "Finland"
student = input("Are you a student?")
height = float(input("What is your height?"))

print("My name is", name,"\n"
    "My age is", age, "\n"
    "I was born in", country, "\n",
    student, ", I do study", "\n",
    "My height is", height)

# Fixed way or RRO Way

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