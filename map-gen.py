from openpyxl import load_workbook

# Load entire spreadsheet/workbook into this object
wb = load_workbook('Example_Spec_v1.0.xlsx')

# Print all workbook sheets
print(f'Sheet names:{wb.sheetnames}\n')

# Obtain information from Title sheet
title_sheet = wb['Title']

# Build the map name based on information from Title Sheet
# Map name convention: 5-digit client ID + direction + document type + document version + s(source)/t(target) + .mdl
for i in range(2, 11):
    for j in range(1, 3):
        if j == 2:
            key = title_sheet.cell(row=i, column=j-1).value.lower()
            value = title_sheet.cell(row=i, column=j).value
            if key == 'client solution id:':
                client_id = value
            if key == 'edi transaction:':
                doc_type = value
            if key == 'edi version:':
                doc_version = value
            if key == 'direction:':
                dir_io = 'o' if value.lower() == 'outbound' else 'i'
                s_or_t = 's' if value.lower() == 'outbound' else 't'
        

map_name = client_id + dir_io + str(doc_type) + str(doc_version) + s_or_t + '.mdl'
print(f'Map Name: {map_name}')


# Obtain information from UDF (User-Defined Format) sheet
udf_sheet = wb['UDF']
udf_max_row = udf_sheet.max_row
udf_max_col = udf_sheet.max_column

print(f'Max row: {udf_max_row}')
print(f'Max col: {udf_max_col}')

def get_cell_value(sheet, row, col):
    return sheet.cell(row=row, column=col).value

# To be able to manage potentially large specs, each row will be stored in a generator object
all_UDF_rows = (
    (get_cell_value(udf_sheet, i, j) for j in range(1, udf_max_col + 1)) for i in range(2, udf_max_row + 1)
    )

for x in all_UDF_rows:
    for y in x:
        print(y)


