print("Optional Challenge — Student Score Summary")

# Read the student's name (string).
student_name = input("Student name: ")

# Read three scores as floats so decimals work.
score_1 = float(input("Score 1: "))
score_2 = float(input("Score 2: "))
score_3 = float(input("Score 3: "))

# Store the scores in a list — easier to apply built-ins.
scores = [score_1, score_2, score_3]

# Compute statistics using built-ins.
minimum_score = min(scores)
maximum_score = max(scores)
mean_score = sum(scores) / len(scores)

# Formatted report. Print the list as-is (Python shows the floats).
print(f"Student: {student_name}")
print(f"Scores: {scores}")
print(f"Minimum: {minimum_score:.2f}")
print(f"Maximum: {maximum_score:.2f}")
print(f"Mean: {mean_score:.2f}")

print()