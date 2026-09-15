# ============================================================
# EXTRA Task 33 — Closest number to target
# ============================================================
numbers = [5, 17, 23, 41, 8, 31]
target = 20

# Find the number closest to target.
# You may use abs().
# Do NOT use min().

closest = numbers[0]
smallest_difference = abs(numbers[0] - target)

for n in numbers:
    difference = abs(n - target)
    if difference < smallest_difference:
        smallest_difference = difference
        closest = n

print("Closest:", closest)