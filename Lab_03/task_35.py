# ============================================================
# EXTRA Task 35 — Prime numbers from 2 to 100
# ============================================================
# Print every prime number from 2 through 100.
#
# Required:
# Use nested for loops.

for number in range(2, 101):
    is_prime = True

    # Test divisors from 2 up to number - 1.
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number)