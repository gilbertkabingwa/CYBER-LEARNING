# WHat is INPUT?
#print () dispaly something to users but INPUT() gets something from users.
#It's built-in Python function that stops your program to get user input. 

#Example:
"""Input is used almost in any application or website you are interacting with. On of them can be ex. chatgpt. The place where you go and ask something. """

# ASk the user to input their name
input("Enter Your Name:")

#INPUT() and Variable
"""Using INPUT() alone reads the user's response but immediately discards it. To keep the value, assign it to a variable!"""
name = input("Enter Your Name:")
print("You are", name)

# What is hard-coded values and dynamic values?
name = input("Enter Your Name:")
country = "Finland"
print("You are", name)

"""Hard-coded (static) value fixed a piece of data written direclty into your code that never changes at runtime. In this case is 'Finland'. """
"""Dynamic values data entered by the user that can vary each time program runs."""
name = input("Enter Your Name:")
country = "Finland"
print(name, "comes from", country)

#INPUT() makes your programm interactive. Input lets your program ask questions and react to what the user types, making it feel alive. 