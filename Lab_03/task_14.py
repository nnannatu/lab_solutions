# ============================================================
# BONUS Task 14 — Limited login attempts
# ============================================================
# Give the user at most 3 attempts to enter the PIN.
#
# Use: for, range(), break
#
# Correct PIN:            Access granted
# Three wrong attempts:   Access denied
#
# Do NOT use a while loop.

correct_pin = "4821"

# At most three attempts, one per loop iteration.
for attempt in range(3):
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access granted")
        # Stop immediately on success.
        break

# The for...else clause runs only if the loop finished
# without hitting break (i.e. all three attempts failed).
else:
    print("Access denied")