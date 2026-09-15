# ============================================================
# Task 9 — Student results
# ============================================================
# Count passed students (score >= 60) and failed students
# (score < 60), then print the average of all scores.
#
# Required:
# Use a loop to calculate the total.
#
# Expected:
# Passed: 5
# Failed: 3
# Average: 69.38

scores = [85, 42, 67, 91, 58, 73, 100, 39]

passed = 0
failed = 0
total = 0

# Single pass over the list: accumulate the total and
# count how many scores fall into each category.
for score in scores:
    total += score

    if score >= 60:
        passed += 1
    else:
        failed += 1

# Average = sum of scores divided by the number of scores.
average = total / len(scores)

print("Passed:", passed)
print("Failed:", failed)
print(f"Average: {average:.2f}")