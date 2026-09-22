# ============================================================
# Task 28 — Running total until limit
# ============================================================
# Repeatedly ask the user to enter positive numbers.
#
# Add each number to a running total.
#
# Stop when the total becomes greater than or equal to 100.
#
# Print:
#
# Total: ...
# Numbers entered: ...
#
# Example:
#
# 20
# 35
# 10
# 40
#
# Total: 105
# Numbers entered: 4
#
# Required:
# Use a while loop.
# ============================================================

total = 0
count = 0

while total < 100:
    number = int(input("Enter a positive number: "))
    total = total + number
    count = count + 1

print("Total:", total)
print("Numbers entered:", count)