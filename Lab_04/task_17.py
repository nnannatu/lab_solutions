# ============================================================
# Task 17 — Find the first divisible number
# ============================================================
numbers = [11, 17, 25, 28, 35, 41]

# Find the first number that is divisible by 7.
#
# If found:
#   print "Found: <number>"
#   stop the loop.
#
# If no number is divisible by 7:
#   print "Not found"
#
# Required:
# Use:
#   for
#   break
#   else
# ============================================================

for number in numbers:
    if number % 7 == 0:
        print("Found:", number)
        break
else:
    print("Not found")