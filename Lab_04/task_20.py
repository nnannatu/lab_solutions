# ============================================================
# Task 20 — Number of digits
# ============================================================
# Ask the user for a positive integer.
#
# Use a while loop to count how many digits the number has.
#
# Example:
# Input: 58372
# Digits: 5
#
# Hint:
# Integer division by 10 removes the last digit.
#
# Example:
# 58372 // 10 -> 5837
#
# Do not convert the number to a string.
# ============================================================

number = int(input("Enter a positive integer: "))

digit_count = 0

while number > 0:
    number = number // 10
    digit_count = digit_count + 1

print("Digits:", digit_count)