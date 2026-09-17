# ============================================================
# Task 1 — Countdown with while
# ============================================================
# Ask the user for a positive integer.
#
# Use a while loop to print from that number down to 1.
# Then print:
#   Go!
#
# Example:
# Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
#
# Make sure the loop variable changes.

# Ask the user for a positive integer
num = int(input("Enter a positive integer: "))

# Count down from num to 1
while num >= 1:
    print(num)
    num = num - 1

# Print final message
print("Go!")