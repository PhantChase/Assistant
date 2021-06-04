import xlwt

workbook = xlwt.Workbook()

sheet = workbook.add_sheet("Sheet Name")

# Applying multiple styles 
style = xlwt.easyxf('font: bold 1, color red;')

# Writing on specified sheet 
sheet.write(0, 1, 'SAMPLE', style)
sheet.write(0, 2, 'SAMPLE', style)

workbook.save("sample.xls") 