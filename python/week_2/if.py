# Pratice the "if" statement
age = 20
if age >=18:
    print("You are an adult!")
 # Output: You are an adult.

# example
age = 15

if age >= 18:
    print("You are an adult.")
# Output: nothing.

# Comparison operators

# Example
password_attempts = 3

print(password_attempts == 3)
print(password_attempts != 3)
print(password_attempts > 5)
print(password_attempts <= 5)

# Output:
# True
# False
# False 
# True
print("=="*32)

# Practice 1 — Predict the output
# Let's start with five small exercises. For each one, decide whether the message will print

"""Question 1
age = 25

if age > 18:
    print("A")

- What's output?
A prints
Nothing prints"""

# Answer is: 

age = 25
if age >=18:
    print("A")

# Output is: prints "A", because 25 is greater than 18, so the condition is True.

#Question 2
"""score = 50

if score == 40:
    print("B")

- What's output?
B prints
Nothing prints"""

# Answer:
score = 50

if score == 40:
    print("B")
# Output is: nothing prints, because 50 is not equal to 40, so the condition is False.

# Question 3

"""temperature = 10

if temperature < 10:
    print("C")

- What's output?
C prints
Nothing prints"""

# Answer is:
temperature = 10

if temperature < 10:
    print("C")
# Output is: prints nothing, because 10 is not less than 10. They are equal. 

# Question 4
"""balance = 100

if balance >= 100:
    print("D")

What's output?
D prints
Nothing prints"""

# Answer is:
balance = 100

if balance >= 100:
    print("D")
# output is D prints, because balance The >= operator includes equality. 100 is equal to 100.

# Question 5
"""attempts = 3

if attempts != 3:
    print("E")

What is output?
E prints
Nothing prints"""

# Answer is:
attempts = 3

if attempts != 3:
    print("E")
# output is: prints nothing, because attempts is 3, so it is equal to 3, not different from it.


# OTHER EXERCISES

# Practice 2 — Write your own if statements
"""Now let's move from predicting code to writing it yourself.
For each task, write a small Python program. Use only a variable, if, a comparison operator, and print(). Do not use elif, else, or loops yet."""
# Challenge 1 — Age

"""Create a variable named age with the value 22.
If the age is greater than or equal to 18, print:"""

age = 22
if age >=18:
    print("Adult")

# Challenge 2 — Password length

"""Create a variable password_length = 12.
If the password length is greater than 8, print:"""
password_length = 12
if password_length >8:
    print("Password meets the length requirement.")

# Challenge 3 — Account status

"""Create a variable account_status = "locked".
If the account status is equal to "locked", print:"""

account_status = "locked"
if account_status == "locked":
    print("Account is locked.")

# Challenge 4 — Failed attempts

"""Create a variable failed_attempts = 4.
If the failed attempts are not equal to 0, print:"""

failed_attempts = 4
if failed_attempts != 0:
    print("Failed attempts detected")

# Challenge 5 — System capacity

"""Create a variable cpu_usage = 90.
If CPU usage is less than or equal to 90, print:"""

cpu_usage = 90
if cpu_usage <= 90:
    print("CPU usage is within the limit.")


# Level 2 — Cybersecurity Python Challenges

# Challenge 1 — Failed login attempts

"""A security system checks how many failed login attempts a user has made.
Your task: Print "Warning: Failed login attempts detected." only if the number of failed attempts is greater than 3.
Starting code: """
failed_attempets = 5
if failed_attempets >3:
    print("Failed login attempts detected")

# Test: What happens if failed_attempts = 3?
if failed_attempets <= 3:
    print("Failed login attempts detected")

# Challenge 2 — Password length

""" A system requires a password to contain at least 12 characters.
Your task: Print "Password length accepted." if the password length is greater than or equal to 12.
Starting code: """

password_length = 12
if password_length >= 12:
    print("Password length accepted.")

# Bonus: Think carefully: Why do we use >= instead of >?

# Challenge 3 — Account lock status

"""A system should display a warning if the account status is exactly "locked".
Your task: Write an if statement that compares the variable with the correct string."""

account_status = "locked"
if account_status == "locked":
    print("ALERT: Account is locked!")

# Extra test: Would "LOCKED" produce the same result as "locked"? Try to explain why.

if account_status == "LOCKED":
    print("ALERT: Account is locked!")
"""It appears that Python did not recognize "LOCKED" when the variable "locked" was in lowercase. Simply put, "LOCKED" was not equal to "locked"."""

#Challenge 4 — Suspicious network traffic

"""A monitoring system records network traffic in megabytes per second (MB/s). The alert threshold is 500.
Your task: Print "ALERT: Unusually high network traffic!" only when network traffic is greater than 500."""

network_traffic = 750
if network_traffic >500:
    print("ALERT: Unusually high network traffic!")

# Test these values separately: 500, 501, and 499. Predict the result before running the code.
network_traffic = 501

if network_traffic > 500:
    print("ALERT: Unusually high network traffic!")
# Prints: "ALERT: Unusually high network traffic!"

# Testing on 499
network_traffic = 499

if network_traffic > 500:
    print("ALERT: Unusually high network traffic!")
# Prints nothing

# Challenge 5 — Access permission

"""A user has a numerical access level. The system should print "Admin access granted." only if the access level is exactly 5."""
access_level = 5
if access_level == 5:
    print("Admin access granted.")
#Try changing access_level to 4 and then 6. Neither should produce the message.
"""Output is nothing on access_level 6, because it has to either less than 5 or equal to 5."""

# Challenge 6 — Security risk score

"""A security system assigns each event a risk score from 0 to 100. A score above 70 triggers an alert.
Your task: Print "HIGH RISK: Investigate this event." only when the score is greater than 70."""

risk_score = 100
if risk_score >70:
    print("HIGH RISK: Investigate this event.")



# Level 3 — Python Practice: Combining Conditions
"""In this level, you will practice using if statements with the comparison operators and the logical operators and and or.
Rules for this level:
- Use only variables, if, comparison operators, and, or, and print().
- Do not use elif, else, or loops.
- Write the code yourself before checking whether it works."""

# Challenge 1 — Secure Login
"""A system allows a user to log in only if their account is active and their password is correct.
Starting code:"""

account_active = True
password_correct = True

if account_active == True and password_correct ==True:
    print("Login successful.")

# Challenge 2 — Security Alert
"""A security monitoring system triggers an alert if a user has more than 3 failed login attempts or a risk score greater than 70.
Starting code:"""

failed_attempts = 5
risk_score = 100

if failed_attempts >3 or risk_score >70:
    print("Security alert!")

# Challenge 3 — Admin Access
"""A system grants administrator access only when the user's access level is exactly 5 and their account is active.
Starting code:"""

access_level = 5
account_active = True

if access_level == 5 and account_active == True:
    print("Admin access granted.")

# Challenge 4 — Suspicious Activity
""" A security system investigates suspicious activity when either of these conditions is met:
- Failed login attempts are greater than 5.
- The risk score is greater than 80."""

failed_attempts = 5
risk_score = 90
if failed_attempts > 5 or risk_score >80:
    print("Investigate activity.")

# Challenge 5 — Secure Administrative Login
"""A system grants access to a restricted administrative area only if all three conditions are met:
- The account is active.
- The password is correct.
- The user's access level is at least 5."""

account_active = True
password_correct = True
access_level = 6
if account_active == True and password_correct == True and access_level >= 5:
    print("Secure admin login approved.")

# Challenge 6 — High-Risk Event Detection
"""A monitoring system flags an event if either of the following is true:
- The risk score is greater than 85.
- The number of failed login attempts is greater than 10 and the account is active.
Starting code:"""

risk_score = 90
failed_attempts = 12
account_active = True

if risk_score >85 or failed_attempts >10 and account_active == True:
    print("HIGH-RISK EVENT DETECTED!")