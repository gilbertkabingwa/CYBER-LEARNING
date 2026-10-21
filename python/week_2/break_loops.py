# Break loops
"""Break which exits a loop.
- break exits a loop.
- continue skips to the next loop iteration.
- return exits the current function and optionally returns a value.
You can learn return after you are comfortable with functions."""

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

"""1. while loops
Repeat code while a condition remains true. Learn how to avoid infinite loops.

2. for loops and range()
Repeat an action a specific number of times or iterate over items.

3. break and continue
Stop a loop early or skip an iteration."""