print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True

# Comparisons return True or False.
print(f"age >= 18:                         {age >= 18}")              # True
print(f"score >= 60:                       {score >= 60}")            # True

# `and` is True only if BOTH sides are True.
print(f"score >= 60 and is_master_student: {score >= 60 and is_master_student}")   # True

# `or` is True if AT LEAST ONE side is True.
print(f"score < 60 or age < 18:            {score < 60 or age < 18}")             # False

# `not` flips the boolean value.
print(f"not is_master_student:             {not is_master_student}")              # False

# bool() converts any value to True/False.
# Falsy values: 0, 0.0, "", [], {}, set(), None.
# Everything else is truthy.
print(f"bool(0):        {bool(0)}")           # False
print(f"bool(1):        {bool(1)}")           # True
print(f"bool(''):       {bool('')}")          # False
print(f"bool('Python'): {bool('Python')}")    # True
print(f"bool([]):       {bool([])}")          # False
print(f"bool([1, 2]):   {bool([1, 2])}")      # True

print()
