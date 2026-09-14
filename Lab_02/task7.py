print("Task 7 — Basic String Operations")

# Read two strings from the user.
first_name = input("First name: ")
last_name = input("Last name: ")

# Concatenation with + . We insert a space between the names.
full_name = first_name + " " + last_name

# len() gives the number of characters (including the space).
print(f"Full name: {full_name}")
print(f"Number of characters: {len(full_name)}")

# Index 0 is the first character.
print(f"First character: {full_name[0]}")

# Negative index -1 means "the last character".
print(f"Last character: {full_name[-1]}")

# Slicing [start:stop] returns a substring.
# [:3] means "from the beginning up to (not including) index 3".
print(f"First three characters: {full_name[:3]}")

# String repetition: full_name * 3 prints it three times.
print(full_name * 3)

print()