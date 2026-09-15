# ============================================================
# Task 21 — Student Data Record
# ============================================================

print("Task 21 — Student Data Record")

# --- Read each field with the correct type ---
student_name = input("Name: ")
student_age = int(input("Age: "))
university = input("University: ")

# Scores are floats so decimals are allowed.
score_1 = float(input("Score 1: "))
score_2 = float(input("Score 2: "))
score_3 = float(input("Score 3: "))

# --- Collect scores into a list ---
scores = [score_1, score_2, score_3]

# --- Build the student dict ---
# A dict groups related fields under named keys.
student = {
    "name": student_name,
    "age": student_age,
    "university": university,
    "scores": scores,           # the value is the list we just made
}

# --- Compute statistics using built-ins ---
score_count = len(scores)
minimum_score = min(scores)
maximum_score = max(scores)
mean_score = sum(scores) / score_count

# --- Print a formatted report ---
# Access dict values by key inside the f-string.
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"University: {student['university']}")
print(f"Scores: {student['scores']}")
print(f"Number of scores: {score_count}")
print(f"Minimum: {minimum_score:.2f}")
print(f"Maximum: {maximum_score:.2f}")
print(f"Mean: {mean_score:.2f}")

print()