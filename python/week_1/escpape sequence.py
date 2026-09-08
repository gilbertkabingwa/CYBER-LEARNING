#Normaali chtaracters:

# In Python there's normaalo characters 

#example A, B, C, 5 9 0, @ ? and so on and a lot of symbols treated as normaali text. 

# There are also Special characters that have special meaning, they all start with blacklast and once Python sees those characters, its going to understand immediately "we have to do something extra"
# They have speciall purpose.

# example:
# NORMAL character; abc@1889n.com

# SPECIAL character;  \", \' ,  \\  \n , \t


# Escape Sequences 
# 1. \"" bouble quote
# 2. \' single quote
 # we use them in order to include those quotes in text. 
# 3. \\ blackslash 
# blackslash is in order include a real blacklash
# 4. \n New Line
# is used is in order to create a new line in the output
# 5. \t Tab
# in order to add horizantal tab
# 6. \b backspace

#REAL EXAMPLE

# How does Python read this code?
print ("Hi \"Python\"")
# \" escape double quote allows you to include a " without ending it.
# Other way of using double code 
print('Hi "Python"')
print('Hi \'Gilbert\'')
print("Long: C:\\Users\\Gilbert")
# use real blackslach \ not as start of an escape sequence

# New line
print ("big boss1")
print()
print("big boss2")
# Emppty print simply prints a blank (NEw Line)
#other wway
print("Big man\n")
print("Big man2")
# \n escape new line adds a new line, it moves the text that comes after it to the next line.
#Other way 
print("Beautiful lady1\n")
print("Beautiful lady2\n")
print("Beautiful lady3")
#You can use \n as many as you want
# Other way
print("Beautiful lady1\nBeautiful lady2\nBeautiful lady3")

#\t escape tab adds a Tab space
# Example

print("Beautiful lady1\tBeautiful lady2")