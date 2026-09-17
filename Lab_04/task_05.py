# ============================================================
# Task 5 — Search with loop else
# ============================================================

# Search for the first odd number.
#
# If an odd number is found:
#   print "First odd number: <value>"
#   stop using break.
#
# If the loop finishes without finding any odd number:
#   print "All values are even"
#
# Required:
# Use:
#   for
#   break
#   else

# List of numbers to search
numbers = [4, 8, 12, 16, 21, 24]

# Search for the first odd number
for num in numbers:
    if num % 2 != 0:
        print("First odd number:", num)
        break
else:
    # Runs only if break was never hit
    print("All values are even")