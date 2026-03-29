from datetime import datetime

student_id = "shefay9008"


# Converts a weight in pounds to kilograms.
def convertData(weightLbs):
    return weightLbs / 2.205


# Inserts comma-separated data into a CSV file, creating the file if it does not exist.
def insertData(path, data):
    try:
        with open(path, "a") as file:
            file.write(data + "\n")
    except Exception as e:
        print("Error writing to file:", e)


# Displays the file path and contents of the CSV file.
def viewData(path):
    try:
        print(f"The file {path}")
        with open(path, "r") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print("Error reading file:", e)


# Gets user input, converts pounds to kilograms, and saves the data to ZooData.csv.
def getInput(path):
    try:
        numberOfEntries = int(input("How many entries are you inputting?\n"))

        for i in range(numberOfEntries):
            dateEntered = input("Enter a date:\n\n")
            weightLbs = float(input("Enter the weight in pounds for the inputted date:\n"))

            # convertData requires one numeric pounds argument and returns the kilograms value
            convertedValue = convertData(weightLbs)

            data = f"{dateEntered},{weightLbs},{convertedValue}"
            insertData(path, data)

            print(f"The following was saved at {datetime.now()} :")
            print(data)

    except Exception as e:
        print("Error entering data:", e)


# Displays the main menu and handles the user's selection.
def main():
    path = "ZooData.csv"

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
        getInput(path)
    elif menuChoice == "2":
        print(f"You selected 2 at {datetime.now()}")
        viewData(path)
    elif menuChoice == "3":
        print("Generate Report is not implemented yet.")
    else:
        print("Error: Invalid menu option selected.")


main()
