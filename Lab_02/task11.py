print("Task 11 — Small Statistics Report")

scores = [78, 92, 85, 69, 88]

# len()  -> count
score_count = len(scores)

# min()  -> smallest score
minimum_score = min(scores)

# max()  -> largest score
maximum_score = max(scores)

# sum()  -> total
total_score = sum(scores)

# Mean = total / count
mean_score = total_score / score_count

# :.2f forces exactly two decimal places (82.4 -> "82.40").
print(f"Number of scores: {score_count}")
print(f"Minimum: {minimum_score}")
print(f"Maximum: {maximum_score}")
print(f"Mean: {mean_score:.2f}")

print()