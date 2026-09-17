# ============================================================
# Task 4 — continue in a while loop
# ============================================================
# Use a while loop to process numbers from 1 through 20.
#
# Skip numbers divisible by 3 using continue.
# Print all other numbers.
#
# IMPORTANT:
# Update the loop variable correctly so you do not create
# an infinite loop.

# Start from 1
i = 1

# Process numbers 1 through 20
while i <= 20:
    # Skip numbers divisible by 3
    if i % 3 == 0:
        i = i + 1
        continue
    print(i)
    i = i + 1