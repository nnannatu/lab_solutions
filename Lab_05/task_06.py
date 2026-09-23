# ============================================================
# Task 6 — **kwargs: profile
# ============================================================
# Create a function:
#
#   show_profile(**details)
#
# Print each key and value in this form:
#   key: value
#
# Example call:
# show_profile(name="Anna", city="Novosibirsk", year=1)
#
# Possible output:
# name: Anna
# city: Novosibirsk
# year: 1


def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


show_profile(name="Anna", city="Novosibirsk", year=1)
