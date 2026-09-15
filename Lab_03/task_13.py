# ============================================================
# BONUS Task 13 — FizzBuzz
# ============================================================
# Print numbers 1 through 30.
#
# If divisible by both 3 and 5 -> FizzBuzz
# If divisible only by 3       -> Fizz
# If divisible only by 5       -> Buzz
# Otherwise print the number.
#
# Hint:
# Check the most specific condition first.

for n in range(1, 31):
    # Check the combined condition first, otherwise numbers
    # like 15 would incorrectly print "Fizz" or "Buzz".
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)