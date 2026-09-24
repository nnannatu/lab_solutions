# ============================================================
# Task 18 — **kwargs: configuration
# ============================================================
# Create a function:
#
#   show_settings(**settings)
#
# If no settings are given, print:
#   No settings
#
# Otherwise print each setting:
#
#   key = value
#
# Example:
#
# show_settings(
#     language="Python",
#     version=3.12,
#     debug=True
# )
#
# Possible output:
# language = Python
# version = 3.12
# debug = True

def show_settings(**settings):

    if not settings:
        print("No settings")
        return

    for key, value in settings.items():
        print(f"{key} = {value}")


show_settings(
     language="Python",
     version=3.12,
     debug=True
)

show_settings()