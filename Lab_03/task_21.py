# ============================================================
# EXTRA Task 21 — Limited number guessing
# ============================================================
secret_number = 37

# Give the user at most 5 attempts to guess the secret number.
#
# After each incorrect guess:
#   if guess < secret_number: print "Too low"
#   if guess > secret_number: print "Too high"
#
# Correct guess:
#   print "Correct"
#   stop immediately
#
# If all 5 attempts are used without success:
#   print "Out of attempts"
#
# Do NOT use while.

for attempt in range(5):
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")
        # Stop the loop as soon as the guess is correct.
        break

# The for...else clause runs only when no break occurred.
else:
    print("Out of attempts")