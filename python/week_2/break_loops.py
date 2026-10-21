# Break loops
"""Break which exits a loop.
- break exits a loop.
- continue skips to the next loop iteration.
- return exits the current function and optionally returns a value."""

# 1. What are Loop Control Statements?
"""When you write a loop (like a while loop or a for loop), Python normally runs the code block from top to bottom, repeats it until the main condition becomes false, or finishes going through an entire collection.

However, sometimes you want more control inside the loop. 
- You might want to:Stop the loop completely before it finishes naturally.
- Skip just one specific step and move straight to the next round.
- Exit an entire function that contains the loop.

This is where break, continue, and return come in."""

# 2. The Three Control Keywords

# Break (Stop the loop immediately)
"""- How it works: The moment Python hits a break statement, it terminates (kills) the loop instantly, completely ignoring any remaining iterations or code left inside the loop block.
- Real-world analogy: Imagine you are searching through a box of 100 markers for a red one. Once you find the red marker on marker #3, you break out of the search process and stop looking through the rest of the box."""

# Continue (Skip this one round)
"""- How it works: When Python hits continue, it skips the rest of the code for the current iteration only and jumps right back to the top of the loop to start the next round.
- Real-world analogy: Imagine a teacher handing out homework, but they decide to skip student number 4 because that student is absent. The teacher says "skip this person" (continue) and immediately moves on to grade student number 5."""

# Return (Exit the function)
"""- How it works: This exits the entire function that the loop lives inside, optionally sending a value back.
- When to use: You typically use return only when your loop is wrapped inside a custom function (using def). Once you are comfortable writing functions, return becomes a natural way to finish a function's job early (for example, finding a search result inside a loop and returning it immediately)."""

# Quick Summary: 


# let’s dig deeper to understand more


"""1. while loops
Repeat code while a condition remains true. Learn how to avoid infinite loops.

2. for loops and range()
Repeat an action a specific number of times or iterate over items.

3. break and continue
Stop a loop early or skip an iteration."""

# Python — Lesson 1: while loops
""" 1. First, understand the idea
Imagine I ask you to print "Hello" five times.

Without a loop, you would write:"""

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

"""That works, but imagine printing it 100 or 1,000 times. Writing the same instruction repeatedly would be inefficient.
A loop allows you to repeat code without writing
 it again and again."""

# 2. What is a while loop?
""" A while loop repeats a block of code as long as a condition is True.

Here is the basic structure:
The structure of a while loop"""
# while condition:
    #code to repeat
"""
- while tells Python to start a loop.
- condition is something Python checks to see whether it is True or False.
- : marks the beginning of the loop's body.
- The indented code is what Python repeats.
From if statements, A while loop uses the same idea, except it checks the condition again after each repetition."""

# Look at this example:
count = 1

while count <= 5:
    print(count)
    count = count + 1
# OUTPUT: 1, 2, 3, 4, 5

# Let's understand exactly why.
"""
Follow the loop step by step
Each time Python reaches the bottom, it checks the condition again.
Step	count	count <= 5	Action
1	    1	    True	    Print 1
2	    2	    True	    Print 2
3	    3	    True	    Print 3
4	    4	    True	    Print 4
5	    5	    True	    Print 5
6	    6	    False	    Stop    """

# The important line is: count = count + 1


""" It increases count by one every time the loop runs.
- Start at 1.
- Print the current number.
- Increase it by one.
- Check the condition again.
- Stop when count becomes 6, because 6 <= 5 is False.
Remember this: A while loop needs a condition, and you often need to change a variable inside the loop so that the condition eventually becomes false."""

# Exercise 1

number = 2

while number <= 6:
    print(number)
    number = number + 2
# output is:
"""
2
4
6

The key lesson: Python checks the condition before each repetition. When number becomes 8, the condition 8 <= 6 is false, so 8 is not printed.
You understood the loop correctly. Now let's practise predicting what happens when the loop changes its number by a different amount."""

# Exercise 2
count = 1

while count < 5:
    print(count)
    count = count + 1

# Output is:
"""
1
2
3
4
Important concept: < 5 means strictly less than 5. When count becomes 5, the condition is false, so Python stops before printing it.

Compare these two conditions:
- count < 5 — does not include 5.
- count <= 5 — includes 5."""

# Exercise 3
count = 1

while count <= 3:
    print(count)
"""
The loop checks whether count <= 3. Since count starts at 1, the condition is True.
The problem is that count never changes. There is no line such as count = count + 1.
So Python repeats the same action forever. This is called an infinite loop """

# Exercise 4
number = 1

while number <= 3:
    print(number)
    number = number + 1

print("Finished")

"""Step 1: Python starts the loop
number = 1

Python checks number <= 3. This is True, so it prints 1 and increases number to 2.
Step 2: The loop repeats
The same process happens for 2 and 3. After printing 3, the counter increases to 4.
Step 3: The loop stops
Python checks 4 <= 3. This is False, so the loop ends.
Step 4: Python continues after the loop
print("Finished") is not indented, so it is outside the loop. Python executes it once the loop finishes.

The output is:
1
2
3
Finished
"""