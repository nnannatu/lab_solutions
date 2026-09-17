# ============================================================
# Task 3 — Valid input with while True
# ============================================================
# Repeatedly ask the user for an integer from 1 to 10.
#
# If the value is outside this range:
#   print "Invalid value"
#   ask again.
#
# When the user enters a valid value:
#   print "Accepted"
#   stop the loop with break.
#
# Required:
# Use:
#   while True
#   break

# Loop forever until a valid value is entered
while True:
    value = int(input("Enter an integer from 1 to 10: "))

    # Check if the value is out of range
    if value < 1 or value > 10:
        print("Invalid value")
    else:
        print("Accepted")
        break