# ============================================================
# Task 23 — Find a value and its position
# ============================================================
numbers = [12, 7, 19, 4, 7, 25]

# Ask the user for a number to search for.
#
# Find the FIRST occurrence of that number.
#
# If found, print:
#
# Found at position: ...
#
# Positions should start from 1.
#
# Example:
# Searching for 19:
# Found at position: 3
#
# If the number does not exist:
# print:
# Not found
#
# Do not use:
#   index()
#   in
#
# Use a loop and break.
# ============================================================

search_value = int(input("Enter a number to search for: "))

position = 0
found = False

for index in range(len(numbers)):
    if numbers[index] == search_value:
        position = index + 1
        found = True
        break

if found:
    print("Found at position:", position)
else:
    print("Not found")