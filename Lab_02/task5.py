print("Task 5 — Time Conversion")

# input() always returns a string, so we wrap it in int()
# to get a number we can do arithmetic with.
total_seconds = int(input("Enter a number of seconds: "))

# // integer (floor) division: how many whole minutes fit?
minutes = total_seconds // 60

# % remainder: how many seconds are left over?
remaining_seconds = total_seconds % 60

# Formatted output: "135 seconds = 2 minute(s) and 15 second(s)"
print(f"{total_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")

print()
