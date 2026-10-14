# Let's move on to else statements. We'll keep using cybersecurity examples so you learn how to apply Python, not just memorize syntax.

# Level 4 — Python if and else
"""1. What does else mean?
You already know that if executes code when a condition is True.
But what happens when the condition is False?
That's where else comes in.
- if = if the condition is true, do this.
- else = otherwise, do this.
Look at this example:"""

account_active = True
if account_active == True:
    print("Account access allowed.")
else:
    print("Account access denied.")

""" Because account_active is True, the output is:
- Output is: Account access allowed.

Now change the variable to False:"""
account_active = True
if account_active == False:
    print("Account access allowed.")
else:
    print("Account access denied.")
# The output becomes:Account access denied.

"""Important: Only one branch runs. If the if condition is true, Python skips else. If the condition is false, Python runs else."""

#Notice the colon : after both if and else. Both branches must be indented correctly.

# 2. Cybersecurity example — Password verification
# Imagine a simple program checking whether a password matches the expected password.

correct_password = "Secure123"
entered_password = "Secure123"

if entered_password == correct_password:
    print("Authentication successful.")
else:
    print("Authentication failed.")


# With the values shown, the output is: Authentication successful.
"""If you change entered_password to "Wrong123", the output becomes:"""
# Output is "Authentication failed."
print("==" * 30)

# Your practice challenges
# Write the code yourself. Use if, else, comparison operators, and print(). You may also use and and or where needed.

# Challenge 1 — Account status
""" Starting code:
Print "Account is active." if the account is active. Otherwise, print "Account is inactive."
Expected output: Account is inactive."""

account_active = False
if account_active:
    print("Account is active.")
else:
    print("Account is Login failed.")

#Challenge 2 — Password check
""" Starting code:
If the entered password matches the correct password, print "Login successful." Otherwise, print "Login failed."
Expected output: Login failed."""

correct_password = "Cyber2026"
entered_password = "Wrong123"

if correct_password == entered_password:
    print("Login successful.")
else:
    print("Login failed.")

#Challenge 3 — Admin access
""" Starting code:
Print "Admin access granted." only if the access level is at least 5 and the account is active. Otherwise, print "Admin access denied."
Expected output: Admin access denied."""

access_level = 4
account_active = True

if access_level >= 5 and account_active == True:
    print("Admin access granted.")
else: 
    print("Admin access denied.")

# Challenge 4 — Security risk
"""Starting code:
If the risk score is greater than 70, print "High risk detected." Otherwise, print "Risk level acceptable."
Expected output: High risk detected."""

risk_score = 85
if risk_score > 70:
    print("High risk detected.")
else:
    print("Risk level acceptable.")

# Challenge 5 — Secure login
""" Starting code:
Print "Login successful." only if the account is active and the password is correct. Otherwise, print "Login rejected."
Expected output: Login rejected."""

account_active = True
password_correct = False
if account_active and password_correct:
    print("Login successful.")
else: 
    print("Login rejected.")