# ============================================================
# EXTRA Task 20 — Find first number divisible by 7 and 11
# ============================================================
# Search numbers from 1 through 500.
#
# Find the FIRST number divisible by both 7 and 11.
#
# Required: for, range(), break

for n in range(1, 501):
    if n % 7 == 0 and n % 11 == 0:
        print(n)
        # Stop immediately after the first match.
        break