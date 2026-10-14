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
if account_active == True and password_correct == True and access_level <= 5:
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