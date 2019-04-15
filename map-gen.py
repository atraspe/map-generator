# Import load_workbook from openpyxl module to handle 
# how the maps specs is parsed (usually an Excel spreadsheet)
from openpyxl import load_workbook

# Load entire spreadsheet/workbook into this object
wb = load_workbook('Example_Spec_v1.0.xlsx')

# Print all workbook sheets
print(f'Sheets available:\n{wb.sheetnames}\n')
