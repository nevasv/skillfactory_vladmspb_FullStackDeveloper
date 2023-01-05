# pip install pandas openpyxl xlsxwriter xlrd
# Импортируем как Pd и в переменную датафрэйм помещаем словаль , например
import pandas as pd
from openpyxl import load_workbook


df = pd.DataFrame({
    'Full name': ['Ivanov Ivan', 'Sidorov Sidor', 'Petrov Petr'],
    'Department': ['Economics', 'Maths', 'Geography'],
    'Budget': [2000000, 1000000, 500000]
})
df.to_excel('test.xlsx')

book = load_workbook(filename='test.xlsx')
sheet = book['Sheet1']
for i in range(1, 5):
    print(sheet['A' + str(i)].value,
          sheet['B' + str(i)].value,
          sheet['C' + str(i)].value,
          sheet['D' + str(i)].value,
          sheet['E' + str(i)].value,)




