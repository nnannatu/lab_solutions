# ============================================================
# EXTRA Task 19 — Running balance
# ============================================================
transactions = [500, -120, -80, 250, -700, 300, -200]

# The starting balance is:
balance = 1000

# Process every transaction in order.
#
# Positive numbers mean money added.
# Negative numbers mean money spent.
#
# After each transaction print the current balance.
# At the end print the final balance and count
# deposits and withdrawals.

deposits = 0
withdrawals = 0

for amount in transactions:
    balance += amount
    print("Transaction:", amount)
    print("Balance:", balance)

    if amount >= 0:
        deposits += 1
    else:
        withdrawals += 1

print("Final balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)