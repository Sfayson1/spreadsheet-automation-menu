from datetime import datetime
import csv
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference

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

        # This loop runs once for each data entry the user wants to add.
        # It collects the date and pounds value, converts pounds to kilograms,
        # then saves all three values into the CSV file.
        for i in range(numberOfEntries):
            dateEntered = input("Enter a date:\n")
            weightLbs = float(input("Enter the weight in pounds for the inputted date:\n"))

            convertedValue = convertData(weightLbs)

            data = f"{dateEntered},{weightLbs},{convertedValue}"
            insertData(path, data)

            print(f"The following was saved at {datetime.now()} :")
            print(data)

    except Exception as e:
        print("Error entering data:", e)


# Creates an Excel report and chart from CSV data.
# Arguments:
# path (str): the path to the CSV data file
# chartType (str): the type of chart to create, either "bar" or "line"
# Return value: none
def createChart(path, chartType):
    try:
        sourceChoice = input(
            "Choose the data source for the chart:\n"
            "1. Pounds\n"
            "2. Kilograms\n"
        )

        if sourceChoice == "1":
            data_column = 2
            y_axis_label = "Weight in Pounds"
        elif sourceChoice == "2":
            data_column = 3
            y_axis_label = "Weight in Kilograms"
        else:
            print("Error: Invalid data source selected.")
            return

        rows = []

        with open(path, "r") as file:
            reader = csv.reader(file)

            # This loop reads each row from the CSV file, converts the numeric
            # values to floats, and stores the cleaned data so it can be written
            # into Excel and used to build the chart.
            for row in reader:
                if len(row) == 3:
                    date_value = row[0]
                    pounds_value = float(row[1])
                    kilograms_value = float(row[2])
                    rows.append([date_value, pounds_value, kilograms_value])

        if len(rows) == 0:
            print("No data found in the CSV file.")
            return

        wb = Workbook()
        ws = wb.active
        ws.title = "Report"

        ws.append(["Date", "Pounds", "Kilograms"])

        for row in rows:
            ws.append(row)

        if chartType == "bar":
            chart = BarChart()
        else:
            chart = LineChart()

        values = Reference(ws, min_col=data_column, min_row=1, max_row=len(rows) + 1)
        labels = Reference(ws, min_col=1, min_row=2, max_row=len(rows) + 1)

        chart.add_data(values, titles_from_data=True)
        chart.set_categories(labels)
        chart.title = f"{student_id} {datetime.now().strftime('%m/%d/%Y')}"
        chart.x_axis.title = "Date"
        chart.y_axis.title = y_axis_label

        ws.add_chart(chart, "E2")

        wb.save("final.xlsx")
        print("Report saved as final.xlsx")

    except Exception as e:
        print("Error creating chart:", e)


# Prompts the user for the graph type and generates the Excel report.
# Arguments:
# path (str): the path to the CSV data file
# Return value: none
def generateReport(path):
    try:
        graphChoice = input(
            "Which graph type would you like to create?\n"
            "Enter 'bar' for a bar chart or 'line' for a line chart:\n"
        ).lower()

        if graphChoice == "bar" or graphChoice == "line":
            createChart(path, graphChoice)
        else:
            print("Error: Invalid graph type selected.")
    except Exception as e:
        print("Error generating report:", e)


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
        print(f"You selected 3 at {datetime.now()}")
        generateReport(path)
    else:
        print("Error: Invalid menu option selected.")


main()
