# Let's move on to elif statements. We'll keep using cybersecurity examples so you learn how to apply Python, not just memorize syntax.
"""elif stands for "else if" and is used to check multiple alternative conditions sequentially within a conditional block. It allows a program to execute a specific piece of code when the preceding if statement evaluates to False, but a new condition evaluates to True.

if
Check the first condition.

elif
If the previous condition was False, check another condition.

else
If no previous condition was True, run this block.

An important rule: Python executes only the first branch that meets the condition. Once one branch has been executed, it skips the remaining branches in the same structure."""

# Example: 
risk_score = 65

if risk_score > 80:
    print("High risk")
elif risk_score > 50:
    print("Medium risk")
else:
    print("Low risk")


# Challenge 1 — Risk classification

"""Task: Classify the security risk based on the risk score.
- If the score is greater than 80, print "High risk."
- Else if the score is greater than 50, print "Medium risk."
- Otherwise, print "Low risk."

Goal: Write one if, one elif, and one else."""

risk_score = 65

if risk_score > 80:
    print("High risk.")
elif risk_score > 50:
    print("Medium risk.")
else:
    print("Low risk.")

# Challenge 2 — Account permissions

""" Task: Determine the user's permission level.
- If access_level is 5 or higher, print "Administrator access."
- Else if access_level is 3 or higher, print "Standard access."
- Otherwise, print "Limited access."

Goal: Use comparison operators correctly."""

access_level = 4 
if access_level >= 5:
    print("Administrator access.")
elif access_level >= 3:
    print("Standard access.")
else:
    print("Limited access.")

# Challenge 3 — Login attempts

""" Task: Check the number of failed login attempts.
- If attempts are 10 or more, print "Account locked."
- Else if attempts are 5 or more, print "Warning: suspicious activity."
- Otherwise, print "Login attempts acceptable."

Goal: Pay attention to the order of the conditions.""" 
failed_attempts = 7
if failed_attempts >= 10:
    print("Account locked.")
elif failed_attempts >= 5:
    print("Warning: suspicious activity.")
else:
    print("Login attempts acceptable.")

# Challenge 4 — Secure login decision

""" Task: Determine whether a login is permitted.
- If the account is inactive, print "Login denied: inactive account."
- Else if the password is incorrect, print "Login denied: incorrect password."
- Otherwise, print "Login successful."

Goal: Use Boolean variables directly in your conditions. Do not combine everything into one condition."""
account_active = True
password_correct = False

if account_active == False:
    print("Login denied: inactive account.")
elif password_correct == False:
    print("Login denied: incorrect password.")
else:
    print("Login successful.")

# Challenge 5 — Network security decision

""" Task: Decide whether a network connection should be allowed.
- If the device is not trusted, print "Connection blocked: untrusted device."
- Else if the account is inactive, print "Connection blocked: inactive account."
- Else if the risk score is greater than 80, print "Connection blocked: high risk."
- Otherwise, print "Connection approved."

Goal: Write four possible outcomes in the correct order."""
device_trusted = True
account_active = True
risk_score = 90

if device_trusted == False:
    print("Connection blocked: untrusted device.")
elif account_active == False:
    print("Connection blocked: inactive account.")
elif risk_score > 80:
    print("Connection blocked: high risk.")
else:
    print("Connection approved.")

# Challenge 6 — Debug the security rules

""" Task: A developer wrote the following code to classify risk scores.

risk_score = 90

if risk_score > 50:
    print("Medium risk.")
elif risk_score > 80:
    print("High risk.")
else:
    print("Low risk.")

Your tasks:
1. Explain why the program produces the wrong result.
2. Correct the order of the conditions.
3. Test your corrected code with risk_score = 40, risk_score = 65, and risk_score = 90.

Goal: Understand why condition order matters in an if/elif/else structure."""

# 1. Explain why the program produces the wrong result.
"""Python executes only the first branch that meets the condition. Once one branch has been executed, it skips the remaining branches in the same structure. In this case, it start with > 50, i could have put the expected output first. In that case could have start with if risk_score is > 80, print("High risk.)"""
# 2. Correct the order of the conditions.
risk_score = 90

if risk_score > 80:
    print("High risk.")
elif risk_score > 50:
    print("Medium risk.")
else:
    print("Low risk.")
# 3. Test your corrected code with risk_score = 40, risk_score = 65, and risk_score = 90.
risk_score = 40

if risk_score > 80:
    print("High risk.")
elif risk_score > 50:
    print("Medium risk.")
else:
    print("Low risk.")