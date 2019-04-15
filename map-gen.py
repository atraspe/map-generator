from openpyxl import load_workbook

# Load entire spreadsheet/workbook into this object
wb = load_workbook('Example_Spec_v1.0.xlsx')

# Print all workbook sheets
print(f'Sheets available:\n{wb.sheetnames}\n')

# Obtain information from Title sheet
title_sheet = wb['Title']

for i in range(2, 11):
    for j in range(1, 3):
        print(title_sheet.cell(row=i, column=j).value, end=' ')
    print()

udf_sheet = wb['UDF']
