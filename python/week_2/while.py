# Python While-Loop Exercises — Easy to Hard
# These six exercises are in English, arranged from beginner to more challenging. They will help you practise while loops, conditions, counters, and logical thinking.

# Exercise 1 - Count from 1 to 5
"""Goal: Practise a basic while loop and increasing a counter.
Write a program that prints the numbers from 1 to 5.
Expected output:
1
2
3
4
5"""

# Code: 
number = 1

while number <= 5:
    print(number)
    number = number + 1

# Exercise 2 — Countdown
"""Goal: Practise decreasing a counter.
Write a program that counts down from 5 to 1, then prints "Go!".
Expected output:

5
4
3
2
1
Go!
"""
# Code: 
number = 5

while number >= 1:
    print(number)
    number = number -1

print("GO!")


# Exercise 3 — Even or Odd
"""Goal: Combine while, if, else, and the modulo operator %.
Write a program that prints the numbers from 1 to 10. After each number, print whether it is even or odd.
Expected output:
1 Odd
2 Even
3 Odd
4 Even
5 Odd
6 Even
7 Odd
8 Even
9 Odd
10 Even"""

# Code:
number = 1

while number <= 10:
    if number % 2 == 0:
        print(number, "Even")
    else:
        print(number, "Odd")
    
    number = number + 1

# Exercise 4 — Sum of Numbers
""" Goal: Practise using a loop to calculate a total.
Write a program that adds all numbers from 1 to 10 and prints the final sum.
Expected output:
The total is: 55"""

# Codi: 
number = 1
total = 0

while number <= 10:
    total = total + number  
    number = number + 1    

print("The total is:", total)

# Exercise 5 - Password Attempts
"""
Goal: Combine loops, user input, conditions, and counters.
Write a program that asks the user to enter a password. The correct password is "python123".

Requirements:
- Give the user a maximum of three attempts.
- If the password is correct, print "Access granted!" and stop asking.
- If the password is incorrect, allow another attempt if any remain.
- If all three attempts fail, print "Access denied!".
Example:
Enter password: hello
Incorrect password.
Enter password: python
Incorrect password.
Enter password: python123
Access granted!
"""
# Codi: 
correct_password = "python123"
attempts = 0
max_attempts = 3
access_granted = False

while attempts < max_attempts and not access_granted:
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Access granted!")
        access_granted = True
    else:
        attempts = attempts + 1
        if attempts < max_attempts:
            print("Incorrect password.")

if not access_granted:
    print("Access denied!")

# Exercise 6 -Guessing Game
"""
Goal: Combine everything you've learned into a small program.

Write a program where the secret number is 7. The user has five attempts to guess it.

Requirements:
- Ask the user to guess a number.
- If the guess is too low, print "Too low!".
- If the guess is too high, print "Too high!".
- If the guess is correct, print "Correct! You win!" and stop the loop.
- If the user uses all five attempts without guessing correctly, print "Game over! The number was 7.".
Example:
Guess the number: 3
Too low!
Guess the number: 9
Too high!
Guess the number: 7
Correct! You win!
"""

# Codi:
secret_number = 7
attempts = 0
max_attempts = 5
has_won = False

while attempts < max_attempts and not has_won:
    # input() palauttaa merkkijonon, joten se täytyy muuttaa kokonaisluvuksi int()-funktiolla
    guess = int(input("Guess the number: "))
    attempts = attempts + 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You win!")
        has_won = True

if not has_won:
    print("Game over! The number was 7.")