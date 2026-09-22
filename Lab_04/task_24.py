# ============================================================
# Task 24 — Password attempts
# ============================================================
# Use:
#
# correct_password = "python123"
#
# Give the user at most 3 attempts to enter the correct
# password.
#
# If the password is correct:
#   print "Access granted"
#   stop immediately.
#
# After 3 incorrect attempts:
#   print "Access denied"
#
# Required:
# Use:
#   while
#   break
# ============================================================

correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted")
        break
    attempts = attempts + 1

if attempts == 3:
    print("Access denied")