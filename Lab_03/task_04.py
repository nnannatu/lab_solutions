# ============================================================
# Task 4 — Access decision
# ============================================================
# Ask the user for:
#   age
#   whether they have a ticket: yes/no
#
# A person may enter only if:
#   age >= 18 AND they have a ticket.
#
# Print one of:
#   Access granted
#   Ticket required
#   Must be 18 or older

age = int(input("Enter your age: "))                    
has_ticket = input("Do you have a ticket? (yes/no): ").lower()   

if age < 18:                                            
    print("Must be 18 or older")
elif has_ticket != "yes":                               
    print("Ticket required")
else:                                                  
    print("Access granted")