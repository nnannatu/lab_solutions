# ============================================================
# EXTRA Task 30 — Pair with target sum
# ============================================================
numbers = [2, 4, 7, 11, 15, 3]
target = 10

# Find two DIFFERENT elements whose sum equals target.
#
# Required:
# Use nested for loops and stop on the first match.

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")
            found = True
            # Stop both loops once the first pair is found.
            break
    if found:
        break