# ============================================================
# Task 12 — Dictionary iteration
# ============================================================
# Iterate over a dictionary with .items().
# Print each student as "Name: Pass" or "Name: Fail",
# then print how many students passed.
#
# Score >= 60 means Pass.

student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

passed = 0

# .items() yields (key, value) pairs for unpacking.
for name, score in student_scores.items():
    if score >= 60:
        print(f"{name}: Pass")
        passed += 1
    else:
        print(f"{name}: Fail")

print("Passed:", passed)