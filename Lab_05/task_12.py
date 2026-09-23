# ============================================================
# Task 12 — math module and list methods
# ============================================================
# Part A — math
#
# Import math.
#
# Ask the user for the radius of a circle.
# Calculate and print:
# - circumference = 2 * math.pi * radius
# - area = math.pi * radius ** 2
# - area rounded UP with math.ceil()
# - area rounded DOWN with math.floor()
#
# Example for radius 3:
# Circumference: 18.849...
# Area: 28.274...
# Area ceil: 29
# Area floor: 28
#
#
# Part B — list methods
#
# Start with:
# numbers = [10, 20, 20, 30]
#
# Perform these operations in order:
# 1. append 40
# 2. extend with [50, 60]
# 3. insert 15 at index 1
# 4. print how many times 20 appears
# 5. print the index of the first 30
# 6. remove the first 20
# 7. pop the last item and save it in removed
# 8. print numbers
# 9. print removed
#
# Do not use sorted() in this task.

import math as m

radius = float(input("Enter the Radius: "))
circumference = 2 * m.pi * radius

print("Circumference:", circumference)

area = m.pi * radius ** 2
print("Area:", area)

area1 = m.ceil(area)
print("Area ceil:", area1)

area2 = m.floor(area)
print("Area floor:", area2)


# Part B

numbers = [10, 20, 20, 30]

# append 40
numbers.append(40)

# extend with [50, 60]
numbers.extend([50, 60])

# 3. insert 15 at index 1
numbers.insert(1, 15)

# print how many times 20 appears
print("Count of 20:", numbers.count(20))

# print the index of the first 30
print("Index of first 30:", numbers.index(30))

# remove the first 20
numbers.remove(20)

# pop the last item and save it in removed
removed = numbers.pop()

# print numbers
print("Numbers:", numbers)

# print removed
print("Removed:", removed)