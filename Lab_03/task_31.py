# ============================================================
# EXTRA Task 31 — Grade distribution
# ============================================================
scores = [95, 82, 67, 73, 58, 91, 49, 88, 76, 100, 61]

# Count how many students received:
#
# A    -> 90–100
# B    -> 75–89
# C    -> 60–74
# Fail -> below 60
#
# Then determine which category has the most students.

a_count = 0
b_count = 0
c_count = 0
fail_count = 0

for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 75:
        b_count += 1
    elif score >= 60:
        c_count += 1
    else:
        fail_count += 1

print("A:", a_count)
print("B:", b_count)
print("C:", c_count)
print("Fail:", fail_count)

# Track the highest count and its label using a small
# manual maximum scan (no max() needed for clarity here).
most_common = "A"
highest = a_count

if b_count > highest:
    highest = b_count
    most_common = "B"

if c_count > highest:
    highest = c_count
    most_common = "C"

if fail_count > highest:
    highest = fail_count
    most_common = "Fail"

print("Most common:", most_common)