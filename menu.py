from datetime import datetime

student_id = "shefay9008"

def convertData(weightLbs):
    return weightLbs / 2.205

def getInput():
    numberOfEntries = int(input("How many entries are you inputting?\n"))

    for i in range(numberOfEntries):
        dateEntered = input("Enter a date:\n\n")
        weightLbs = float(input("Enter the weight in pounds for the inputted date:\n"))

        # convertData requires one numeric pounds argument and returns the kilograms value
        convertedValue = convertData(weightLbs)

        print(f"The following was saved at {datetime.now()} :")
        print(f"{dateEntered},{weightLbs},{convertedValue}")

print(f"{student_id}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

menu_options = [
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
]

for option in menu_options:
    print(option)

menuChoice = input()

if menuChoice == "1":
    print(f"You selected 1 at {datetime.now()}")
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")
