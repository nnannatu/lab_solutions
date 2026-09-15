# ============================================================
# EXTRA Task 23 — Prime number check
# ============================================================
# Ask the user to enter an integer greater than 1.
#
# Determine whether the number is prime.
#
# Required:
# Use a for loop to test divisors.
# Do NOT use any library.

number = int(input("Enter an integer greater than 1: "))

is_prime = True

# Any divisor other than 1 and the number itself means
# the number is not prime.
for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        # No need to keep testing once a divisor is found.
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")