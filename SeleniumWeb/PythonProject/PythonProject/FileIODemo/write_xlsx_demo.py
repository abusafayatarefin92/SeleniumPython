from openpyxl import Workbook

work_book = Workbook()
work_sheet = work_book.active
# work_sheet['C2'] = 'ABC Academy'

# test_data = [['Name', 'City'], ['Karim', 'Dhaka'], ['Akbar', 'Feni'], ['Rahim', 'Chittagong']]
#
# for data in test_data:
#     work_sheet.append(data)

for i in range(1, 6):
    for j in range(1, 5):
        work_sheet.cell(row = i, column = j).value = i + j

work_book.save('demoexcel.xlsx')


