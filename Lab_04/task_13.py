# ============================================================
# Task 13 — Integrated task: validated average
# ============================================================
# Write a function:
#
#   average(total, count)
#
# Rules:
#   if count == 0:
#       return None
#   otherwise:
#       return total / count
#
# Then write a loop that asks the user for count until
# the user enters a value >= 0.
#
# Ask once for total.
#
# Call average(total, count).
#
# If the returned result is None:
#   print "Cannot calculate average"
#
# Otherwise:
#   print the average with 2 decimal places.
#
# Required:
# Use:
#   function
#   while loop
#   condition
#   return
#   is None

# Return None if count is 0, otherwise return the average
def average(total, count):
    if count == 0:
        return None
    return total / count


# Ask for the total
total = float(input("Enter the total: "))

# Keep asking until count is >= 0
count = int(input("Enter the count (>= 0): "))
while count < 0:
    count = int(input("Enter the count (>= 0): "))

# Calculate and validate the result
result = average(total, count)

if result is None:
    print("Cannot calculate average")
else:
    print(f"{result:.2f}")