# ============================================================
# Task 11 — return versus print
# ============================================================
# The function below is not useful if later code needs
# to reuse the calculated value:
#
# def rectangle_area(width, height):
#     print(width * height)
#
# Rewrite it so that it RETURNS the area.
#
# Then:
#   store the result for width=5, height=4
#   print the result
#   calculate result * 2 and print it
#
# Goal:
# Demonstrate why return is different from print.

# Return the area so it can be reused later
def rectangle_area(width, height):
    return width * height


# Store the returned value
result = rectangle_area(5, 4)
print(result)

# Reuse the returned value
print(result * 2)