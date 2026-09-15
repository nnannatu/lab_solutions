# ============================================================
# EXTRA Task 15 — Largest of three numbers
# ============================================================
# Ask the user to enter three integers.
#
# Print the largest number.
#
# Do NOT use max().
#
# Think carefully about equal values.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Start by assuming the first number is the largest,
# then compare the others against it.
largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest:", largest)