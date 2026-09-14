print("Task 4 — Operator Precedence")

# * is evaluated before +  ->  2 + 12 = 14
expression_1 = 2 + 3 * 4

# Parentheses override precedence -> (5) * 4 = 20
expression_2 = (2 + 3) * 4

# / is evaluated before +  ->  4.0 + 3 = 7.0
expression_3 = 20 / 5 + 3

# Parentheses change the grouping -> 20 / 8 = 2.5
expression_4 = 20 / (5 + 3)

# Right-associative exponentiation -> 2 ** (3 ** 2) = 2 ** 9 = 512
expression_5 = 2 ** 3 ** 2

# Print each result inline with the expression that produced it.
print(f"2 + 3 * 4 = {expression_1}")            # 14
print(f"(2 + 3) * 4 = {expression_2}")          # 20
print(f"20 / 5 + 3 = {expression_3}")           # 7.0
print(f"20 / (5 + 3) = {expression_4}")         # 2.5
print(f"2 ** 3 ** 2 = {expression_5}")          # 512

print()
