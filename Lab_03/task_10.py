# ============================================================
# Task 10 — Search and stop
# ============================================================
# Search a list of names using a for loop.
#
# If the name is found, print "Found" and stop with break.
# If the name is not found, print "Not found".
#
# Do not use: if target in names

names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]

target = input("Enter a name: ")

# Boolean flag: starts False, set to True only if a match is found.
found = False

for name in names:
    if name == target:
        found = True
        break

# The flag determines which message is printed.
if found:
    print("Found")
else:
    print("Not found")