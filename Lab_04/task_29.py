# ============================================================
# BONUS Task 29 — Prime number checker
# ============================================================
# Write a function:
#
#   is_prime(number)
#
# A prime number:
#   is greater than 1
#   has no divisors except 1 and itself
#
# Examples:
#
# is_prime(2)  -> True
# is_prime(7)  -> True
# is_prime(8)  -> False
# is_prime(1)  -> False
#
# Use a loop to test possible divisors.
#
# Required:
# Use:
#   function
#   for loop
#   break
#   return
#
# Do not use any external libraries.
# ============================================================

def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

print(is_prime(2))
print(is_prime(7))
print(is_prime(8))
print(is_prime(1))