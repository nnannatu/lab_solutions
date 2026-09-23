# ============================================================
# Task 3 — Early return
# ============================================================
# Create a function:
#
#   safe_divide(a, b)
#
# If b is 0, return None immediately.
# Otherwise return a / b.
#
# Test:
# safe_divide(10, 2)  -> 5.0
# safe_divide(10, 0)  -> None

def safe_divide(a, b):
    if b == 0:
        return None
    else:
        return a/b


print()

print(safe_divide(10, 2))
print(safe_divide(10, 0))