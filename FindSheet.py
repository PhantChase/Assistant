import xlrd
import xlwt

file_location = "output.xls"
wb = xlrd.open_workbook(file_location)
sheet1 = wb.sheet_by_index(0)
hang = sheet1.nrows
cot = sheet1.ncols
print('số hàng trong Excel:')
print(sheet1.nrows)
print('số cột trong Excel:')
print(sheet1.ncols)
i=0
dem=0
workbook = xlrd.open_workbook('driendlist.xlsx')
sheet = workbook.sheet_by_index(0)
data = [sheet.cell_value(0, 1) for col in range(sheet.ncols)]
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Friend')
mangtim = []
linktim = []
while i < hang:
    nickname = sheet1.cell_value(i, 0).upper()
    link = sheet1.cell_value(i, 1)

    b = nickname.split()
    count = len(b)
    if 'HUY' in b:
        d = ' '.join(b)
        link1 = link.lstrip('https://www.faceboo')
        link2 = link1.lstrip('k.com')
        link3 = link2.lstrip('/')
        kiemtra = link3.startswith('profile.php?id=')
        if kiemtra == True:
           link4 = link3.lstrip('profile.php?id=')
           mangtim.append(d)
           linktim.append(link4)
    i+=1
print(mangtim)
print(linktim)