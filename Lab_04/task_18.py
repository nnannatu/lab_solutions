# ============================================================
# Task 18 — Simple menu with while True
# ============================================================
# Create this menu:
#
# 1 - Say hello
# 2 - Show a number
# 3 - Exit
#
# Repeatedly ask the user to choose an option.
#
# If the user enters 1:
#   print "Hello!"
#
# If the user enters 2:
#   ask for a number and print it.
#
# If the user enters 3:
#   print "Goodbye!"
#   stop the program.
#
# For any other value:
#   print "Invalid option"
#
# Required:
# Use:
#   while True
#   if / elif / else
#   break
# ============================================================

while True:
    print("1 - Say hello")
    print("2 - Show a number")
    print("3 - Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        number = input("Enter a number: ")
        print("You entered:", number)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option")