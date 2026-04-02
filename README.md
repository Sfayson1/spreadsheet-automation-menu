ZooData CSV Automation Project

A Python program that collects user input, stores the data in a CSV file, and generates Excel reports with charts using openpyxl.

--------------------------------------------------

Features

- Input multiple entries (date and weight in pounds)
- Automatically convert pounds to kilograms
- Save data to ZooData.csv
- View saved data from the CSV file
- Generate Excel reports with:
  - Bar charts
  - Line charts
- Choose data source for chart:
  - Pounds
  - Kilograms
- Dynamic chart title using Student ID and current date
- Uses try-except for error handling

--------------------------------------------------

How to Run

1. Run the Python file:
   python final_project.py

2. Select from the menu:

   1 → Input Data
   2 → View Current Data
   3 → Generate Report

3. If you select option 3:
   - Choose chart type (bar or line)
   - Choose data source (pounds or kilograms)
   - The program will generate an Excel file with a chart

--------------------------------------------------

Output

- CSV file:
  ZooData.csv (stores all entered data)

- Excel file:
  final.xlsx (contains data + generated chart)

--------------------------------------------------

Files Included

File                Description
--------------------------------------------------
final_project.py    Main program with menu + report generation
ZooData.csv         Data file (created/updated by program)
final.xlsx          Excel report with chart (generated after running program)
README.txt          Project description

--------------------------------------------------

Requirements

- Python 3.x
- openpyxl library

Install required library:
pip install openpyxl

--------------------------------------------------

Example Data Format (CSV)

Date, Pounds, Kilograms
10/01/2022,150,68.03
10/02/2022,155,70.29

--------------------------------------------------

Notes

- The Excel chart is automatically generated when selecting option 3
- The chart title format:
  <student_id> <current date>

  Example:
  shefay9008 04/01/2026

- Make sure ZooData.csv exists or is created in the same directory

--------------------------------------------------
