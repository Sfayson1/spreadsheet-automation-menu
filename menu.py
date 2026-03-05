from datetime import datetime

student_id = "shefay9008"

print(f"{student_id}'s Excel Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")


option = input("Please select an option (1-3): ")

print(f"You selected {option} at {datetime.now()}")
