# Control Flow Statements

# 1. What is control flow?

"""Control flow describes the order in which Python executes instructions in a program.

Normally, Python executes code from top to bottom, one line at a time. However, real programs often need to make decisions, repeat tasks, or skip certain instructions depending on what happens.

This is where control flow statements become important.

For example, imagine a cybersecurity program that checks whether a user is allowed to access a system:

If the password is correct, allow access.

If the password is incorrect, deny access.

If the user makes several incorrect attempts, stop asking for a password.

To build this program, you need to control which instructions run and when.

The main categories of control flow are:

Conditional statements — make decisions.

Loops — repeat instructions.

Loop control statements — change how loops behave.

Other flow-control statements — affect execution, such as pass, return, and match.

You should learn these gradually. Start with conditional statements, then loops, and finally the more advanced statements. """

# 2. Conditional Statements

""" Conditional statements allow Python to make decisions based on whether a condition is true or false.

The main conditional keywords are:

if

elif

else
"""
print("==" * 30)
print()
# 2.1 The if statement
print("==" * 15)
print()
# The if statement executes a block of code only when a specified condition is true.

# Example
age = 20

if age >= 18:
    print("You are an adult.")

# Output:

""" You are an adult.

Let's break down the code:

age = 20 stores an integer in a variable.

if begins a conditional statement.

age >= 18 is the condition being checked.

: marks the beginning of the code block.

The indented print() statement runs if the condition is true.

Because 20 >= 18 is true, Python executes the print() statement. """

# Now consider this example:

age = 15

if age >= 18:
    print("You are an adult.")

"""Output: nothing.

The condition is false, so Python skips the indented block.

Important: An if statement does not automatically require an else. Sometimes you only want something to happen when a condition is true."""

# Another example
account_balance = 500

if account_balance > 0:
    print("Your account has a positive balance.")

# This is useful when you want a program to check a condition before performing an action.

# 2.2 Comparison operators

# Conditional statements often use comparison operators to compare values.
"""     Operator            Meaning                     Example         Result
        ==                  Equal to                    5 == 5          True
        !=                  Not equal to                5 != 3          True
        >                   Greater than                8 > 4           True
        >                   Less than                   2 < 7           True
        >=                  Greater than or equal to    5 >= 5          True
        <=                  Less than or equal to       3 <= 5          True

These operators produce a Boolean result: True or False."""


# Example
password_attempts = 3

print(password_attempts == 3)
print(password_attempts != 3)
print(password_attempts > 5)

"""Output:

True
False
False 

# A critical distinction: = versus ==

These operators have different purposes.

age = 20

The single equals sign assigns a value to a variable.

age == 20

The double equals sign checks whether the value equals 20.

A common beginner error is writing:

if age = 20:
    print("Age is 20.")

This is invalid Python syntax. Use == for the comparison. """

print("==" * 30)
print()
# 2.3 The else statement
print("==" * 15)
print()
# The else statement executes when the preceding if condition is false.

# Example
age = 16

if age >= 18:
    print("Access allowed.")
else:
    print("Access denied.")

""" Output:

Access denied.

The logic is:

Is age >= 18?
       |
    ┌──┴──┐
   Yes     No
    |       |
 Allow    Deny

An else does not have its own condition. It handles the remaining case.

When should you use else?

Use it when you want a default outcome if the condition is not satisfied."""

# For example:

password_correct = False

if password_correct:
    print("Login successful.")
else:
    print("Login failed.")

# Python treats the Boolean value False as a false condition.
print("==" * 30)
print()
# 2.4 The elif statement
print("=="*15)
print()

#elif means else if. It allows you to check another condition if the previous condition was false.

# Example
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

""" Output:

Grade C

Python checks the conditions in order:

Is 75 >= 90? No.

Is 75 >= 80? No.

Is 75 >= 70? Yes.

Print Grade C and skip the remaining branches.

Important: Python executes the first matching branch and then skips the rest of that conditional chain.

This means the order of conditions matters.
"""

# Example of incorrect ordering
score = 95

if score >= 70:
    print("Grade C")
elif score >= 90:
    print("Grade A")

""" Output:

Grade C

Why? Because 95 >= 70 is already true. Python never reaches the second condition.
"""

# Correct ordering
score = 95

if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade C")

""" Output:

Grade A

Start with the most specific or highest-threshold condition when using ranges like these.
"""

# 3. Logical Operators

""" Logical operators allow you to combine conditions or reverse their truth values.

The three main operators are:

and

or

not

These are particularly important when conditions become more complex.
"""

# 3.1 The and operator

# and returns true when both conditions are true.

age = 25
has_account = True

if age >= 18 and has_account:
    print("Access allowed.")

""" Output:

Access allowed.

Both conditions are true, so the code executes.
"""

# Consider:

age = 16
has_account = True

if age >= 18 and has_account:
    print("Access allowed.")

"""The condition is false because the user is under 18, even though has_account is true.

Think of and as requiring every condition to be satisfied.
"""

# 3.2 The or operator

# or returns true when at least one condition is true.

is_admin = False
is_authorized = True

if is_admin or is_authorized:
    print("The condition is satisfied.")

""" Output:

The condition is satisfied.

Only one of the conditions needs to be true.
"""

# 3.3 The not operator

# not reverses a Boolean value.

is_locked = False

if not is_locked:
    print("The account is unlocked.")

"""Output:

The account is unlocked.

Because is_locked is False, not is_locked evaluates to True.

Quick comparison

Expression              When it is true

A and B                 Both A and B are true
A or B                  At least one is true
not A                   A is false
"""
# Practical cybersecurity example
username = "admin"
password_correct = True
account_locked = False

if username == "admin" and password_correct and not account_locked:
    print("Login successful.")
else:
    print("Login denied.")

""" This illustrates how multiple conditions can control one action.

It is only a learning example, not a secure authentication system."""

# 4. Nested Conditional Statements

"""A nested conditional is an if statement placed inside another conditional block.

This is useful when one decision depends on the result of another decision.
"""

# Example
username = "gilbert"
password_correct = True

if username == "gilbert":
    if password_correct:
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Unknown username.")

""" Output:

Login successful.

Python first checks the username. Only if the username matches does it check the password.

The structure looks like this:

Check username
    |
    ├── Incorrect → Unknown username
    |
    └── Correct
          |
          ├── Password incorrect → Error
          |
          └── Password correct → Login successful

You can often simplify nested conditions using and, but nesting can make a step-by-step decision process easier to understand.

For now, focus on making the logic clear rather than making the code as short as possible.
"""

# 5. Indentation and Code Blocks

""" Indentation is one of the most important Python rules.

Python uses indentation to determine which instructions belong to a conditional or loop."""

# Correct
age = 20

if age >= 18:
    print("Adult")
    print("Access allowed.")

print("Program finished.")

# Both indented statements belong to the if block. The final statement is outside it, so it executes regardless of the age.

""" Incorrect
age = 20

if age >= 18:
print("Adult")

 This produces an IndentationError.

Use four spaces for each indentation level, which is the standard Python convention.

Why indentation matters"""

# Compare these two examples.

if age >= 18:
    print("Adult")
    print("Access allowed.")

# Both messages are conditional.

if age >= 18:
    print("Adult")

print("Access allowed.")

"""Only the first message is conditional. The second prints regardless of the condition.

Understanding indentation is essential before moving to loops and functions."""

# 6. Loops: Repeating Code

""" Conditional statements make decisions. Loops repeat instructions.

Imagine you want a program to print the same message 100 times. You could write 100 print() statements, but that would be inefficient.

Loops allow you to repeat a block of code.

Python has two main loop types:

while

for

6.1 The while loop

A while loop repeats a block of code as long as its condition remains true.
"""
# Example
count = 1

while count <= 5:
    print(count)
    count = count + 1

"""Output:

1
2
3
4
5

Let's understand each step:

count = 1 initializes the variable.

while count <= 5: checks the condition.

print(count) displays the current value.

count = count + 1 increases the value by one.

Python checks the condition again.

When count becomes 6, the condition is false and the loop ends.

A shorter way to increase a variable
count += 1

This means the same as:

count = count + 1

You do not need to memorize the shorter form immediately.

Infinite loops

Consider:

count = 1

while count <= 5:
    print(count)

This code never changes count. Since count remains 1, the condition remains true forever.

This is called an infinite loop.

Always check whether a while loop can eventually reach a condition that becomes false, unless you intentionally design a loop that runs continuously.
"""

# 6.2 The for loop
"""
A for loop iterates over items in a sequence or other iterable object.

It is commonly used when you want to process each item in a collection or repeat an action a specified number of times.
"""
# Example with range()
for number in range(5):
    print(number)

"""Output:

0
1
2
3
4

range(5) produces the sequence of integers starting at 0 and stopping before 5.

This means it produces five values, not six.
"""
# Starting at a different number
for number in range(1, 6):
    print(number)

"""Output:

1
2
3
4
5

Here, range(1, 6) starts at 1 and stops before 6.
"""
# Using a for loop with strings
name = "Python"

for letter in name:
    print(letter)

"""Output:

P
y
t
h
o
n

Python processes each character in the string.
"""
# Using a for loop with a list
tools = ["Python", "Linux", "Git"]

for tool in tools:
    print(tool)

"""Output:

Python
Linux
Git

This is one reason lists will become useful in your future exercises."""

# 7. Choosing Between while and for

# Both loops repeat code, but they are often used for different purposes.

# while loop                                                          for loop

# Repeats while a condition is true                                 Iterates through items or a range
# Useful when the number of repetitions is not known in advance     Useful when processing a known sequence
# Requires care to avoid accidental infinite loops                  Often ends automatically when the sequence is exhausted
# Can run until a user chooses to quit                              Can process each item in a list

# Example: while

# A menu that continues until the user chooses to quit:

choice = ""

while choice != "quit":
    choice = input("Type 'quit' to exit: ")

print("Program closed.")

# Example: for

# Print a message three times:

for attempt in range(3):
    print("Checking system...")

# The best loop depends on what you want the program to accomplish.

# 8. Loop Control Statements

""" Python provides statements that change how a loop behaves.

The three important ones to understand are break, continue, and pass."""

# 8.1 break

# break immediately terminates the nearest enclosing loop.

for number in range(1, 10):
    if number == 5:
        break

    print(number)

"""Output:

1
2
3
4

When number becomes 5, the condition is true and break ends the loop.

The numbers after 5 are never processed."""

# Practical example

while True:
    command = input("Enter a command (or 'quit'): ")

    if command == "quit":
        break

    print("Command received:", command)

print("Program closed.")

# while True creates a loop that continues until something stops it. Here, break stops it when the user enters "quit".

# 8.2 continue

# continue skips the rest of the current iteration and moves to the next iteration.

for number in range(1, 6):
    if number == 3:
        continue

    print(number)

"""Output:

1
2
4
5

When the value is 3, Python skips print(number) for that iteration.

Unlike break, continue does not terminate the loop.

Difference between break and continue

break — stop the loop completely.

continue — skip this iteration and keep looping. """

# 8.3 pass

# pass does nothing. It acts as a placeholder when Python requires a statement but you have not implemented the behavior yet.

if True:
    pass

# This is valid Python.

# It can be useful when planning a program:

def check_security_status():
    pass

"""The function has a body, but it does not perform any action yet.

For your current stage, it is enough to understand that pass is a placeholder, not a decision or a loop."""

# 9. Combining Conditionals and Loops

# The real power of control flow becomes clear when you combine different statements.

# Example: A simple access system

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print("Incorrect password.")

if attempts == max_attempts:
    print("Maximum attempts reached.")

# This example combines:

"""Variables

input()

Comparison operators

if and else

A while loop

break

Integer arithmetic

It also introduces an important idea: the state of a program can change over time.

At the beginning, attempts is 0. Every incorrect password increases the number. That change affects whether the loop continues.

Note that this is only a beginner exercise. Real authentication systems need secure password storage, rate limiting, and other protections."""

# 10. Truthy and Falsy Values

""" Python conditions do not always need an explicit comparison such as age >= 18.

Python can also evaluate values directly."""

# For example:

name = ""

if name:
    print("Name provided.")
else:
    print("Name is empty.")

"""Output:

Name is empty.

An empty string evaluates as false in a condition.

Common falsy values include:

False

None

0

0.0

"" — empty string

— empty list

Most other values are truthy, including non-empty strings such as "False"."""

# Important difference
is_student = False

# This stores a Boolean value.

is_student = "False"

# This stores a string. Because the string is not empty, it is truthy.

# Therefore:

is_student = "False"

if is_student:
    print("This condition is true.")

"""The message prints.

This is a useful lesson in data types: what a value looks like is not always the same as its data type or its Boolean meaning."""

# 11. return and Function Control Flow

# As you progress, you will learn functions. A return statement ends a function's execution and sends a result back to the code that called it.

# Example
def check_age(age):
    if age >= 18:
        return "Adult"

    return "Minor"


result = check_age(20)
print(result)

"""Output:

Adult

When Python reaches return "Adult", the function ends immediately. It does not continue to the next return.

This is different from break, which exits a loop.

break exits a loop.

continue skips to the next loop iteration.

return exits the current function and optionally returns a value"""

print()
print("=="*30)
"""Please note that most of this information was generated using AI but filtered through my own words."""
print()
print("=="*30)