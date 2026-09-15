# ============================================================
# EXTRA Task 28 — Simple password checker
# ============================================================
password = input("Enter password: ")

# A valid password must:
#   contain at least 8 characters
#   contain at least one digit
#   contain at least one uppercase English letter
#
# Do NOT use any().

digits = "0123456789"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

has_digit = False
has_uppercase = False

for ch in password:
    if ch in digits:
        has_digit = True
    if ch in uppercase:
        has_uppercase = True

if len(password) >= 8 and has_digit and has_uppercase:
    print("Valid password")
else:
    print("Invalid password")