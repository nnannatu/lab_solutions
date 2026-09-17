# ============================================================
# BONUS Task 14 — Guess the number
# ============================================================
# Use:
# secret_number = 37
#
# Repeatedly ask the user to guess the number.
#
# Print:
#   Too low
#   Too high
#   Correct
#
# Stop only when the guess is correct.
#
# Also count how many attempts were needed.
#
# Required:
# Use a while loop.

# The secret number to guess
secret_number = 37
attempts = 0
guess = 0

# Keep guessing until correct
while guess != secret_number:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1  # count each attempt

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")

# Show total attempts
print("Attempts:", attempts)