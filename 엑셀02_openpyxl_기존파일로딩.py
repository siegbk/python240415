import openpyxl as op 

wb = op.load_workbook(r"c:\work\test.xlsx")

#새로운 시트 추가 
ws = wb.create_sheet("직원명부")

wb.save("test2.xlsx")

