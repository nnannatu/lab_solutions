# ============================================================
# Task 2 — Repeat until zero
# ============================================================
# Repeatedly ask the user to enter an integer.
#
# Stop when the user enters 0.
#
# Before 0 is entered:
#   count how many non-zero numbers were entered;
#   calculate their sum.
#
# At the end print:
#   Count: ...
#   Sum: ...
#
# Example:
# Input: 5, -2, 7, 0
# Count: 3
# Sum: 10

# Initialize counters
count = 0
total = 0

# Ask for the first number
number = int(input("Enter an integer: "))

# Keep looping until the user enters 0
while number != 0:
    count = count + 1
    total = total + number
    number = int(input("Enter an integer: "))

# Print final results
print("Count:", count)
print("Sum:", total)