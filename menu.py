from datetime import datetime

student_id = "shefay9008"

print(f"{student_id}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

# Menu options stored in a list
menu_options = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
]

# option represents each menu item in the menu_options list
for option in menu_options:
    print(option)

choice = input("Please select an option (1-3): ")

# Validate user input
if choice in ["1", "2", "3"]:
    print(f"You selected {choice} at {datetime.now()}")
else:
    print("Error: Invalid choice selected.")
