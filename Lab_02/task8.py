print("Task 8 — Useful print() Options")

language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"

# sep=" | " inserts " | " between each argument.
# Default sep is a single space.
print(language, course, university, sep=" | ")

# end=" " replaces the default newline (\n) with a space.
# So the next print() continues on the same line.
print(language, end=" ")
print("Programming")
# Combined output: "Python Programming"

print()
