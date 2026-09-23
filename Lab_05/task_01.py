# ============================================================
# Task 1 — Positional and keyword arguments
# ============================================================
# Create a function:
#
#   describe_student(name, age, city)
#
# The function should print:
#   Name: ...
#   Age: ...
#   City: ...
#
# Call the function three times:
# 1. using only positional arguments;
# 2. using only keyword arguments in a different order;
# 3. using one positional argument and the rest as keyword arguments.
#
# Example:
# describe_student("Anna", 23, "Novosibirsk")
#
# Output:
# Name: Anna
# Age: 23
# City: Novosibirsk

def describe_student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

print()

# Positional arguments
describe_student("Anna", 23, "Novosibirsk")
print()

# Keyword arguments
describe_student(age=17, name="Eva", city="Moscow")
print()

# one positional argument and the rest as keyword arguments
describe_student("Emeka", age=27, city="Abijan")

