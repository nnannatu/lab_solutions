# ============================================================
# BONUS Task 30 — Mini calculator
# ============================================================
# Write a function:
#
#   calculate(a, b, operation)
#
# operation can be:
#
#   "+"
#   "-"
#   "*"
#   "/"
#
# Return the result of the operation.
#
# If the user tries to divide by zero:
#   return None
#
# Then create a program that repeatedly:
#
#   asks for two numbers
#   asks for an operation
#   calls calculate()
#   prints the result
#
# After each calculation ask:
#
# Continue? yes/no
#
# Stop when the user enters:
#   no
#
# Required:
# Use:
#   function
#   return
#   while loop
#   conditions
# ============================================================

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return None
        return a / b
    else:
        return None

while True:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    result = calculate(a, b, operation)
    print("Result:", result)

    again = input("Continue? yes/no: ")
    if again == "no":
        break