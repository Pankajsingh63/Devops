import openpyxl as Ex
import boto3
file = Ex.load_workbook("RITM1671490.xlsx")
sheet1 = file['AWS Build Specs']
rows1 = sheet1.rows
for row in rows1:
    print(row)