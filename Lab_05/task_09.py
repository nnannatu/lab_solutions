# ============================================================
# Task 9 — Recursive countdown
# ============================================================
# Create a recursive function:
#
#   countdown(n)
#
# If n == 0:
#   print("Go!")
#   stop the function.
#
# Otherwise:
#   print n
#   call countdown(n - 1)
#
# Do NOT use a loop.
#
# Example:
# countdown(3)
#
# Output:
# 3
# 2
# 1
# Go!

def countdown(n):
    if n == 0:
        print("Go!")
        return None
    else:
        print(n)
        return countdown(n-1)

countdown(100)