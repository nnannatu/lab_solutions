print("Task 14 — String Methods")

text = "  Python Programming Course  "

# strip() removes leading and trailing whitespace.
cleaned = text.strip()

# Print transformations of the cleaned text.
print(f"Stripped:    {cleaned}")                    # "Python Programming Course"
print(f"Lowercase:   {cleaned.lower()}")            # "python programming course"
print(f"Uppercase:   {cleaned.upper()}")            # "PYTHON PROGRAMMING COURSE"
print(f"Replaced:    {cleaned.replace('Course', 'Lab')}")

# startswith() / endswith() return True or False.
print(f"Starts with 'Python': {cleaned.startswith('Python')}")   # True
print(f"Ends with 'Course':   {cleaned.endswith('Course')}")     # True

print()