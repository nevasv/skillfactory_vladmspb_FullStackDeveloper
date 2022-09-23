# pip install pandas openpyxl xlsxwriter xlrd
# Импортируем как Pd и в переменную датафрэйм помещаем словаль , например
import pandas as pd
df = pd.DataFrame({
    'Full name': ['Ivanov Ivan', 'Sidorov Sidor', 'Petrov Petr'],
    'Department': ['Economics', 'Maths', 'Geography'],
    'Budget': [2000000, 1000000,500000]
})
df.to_excel('test.xlsx')

# def example():
#     """
#     Создание xlsx файла и запись в него
#     """
#     # создаю книгу
#     book = openpyxl.Workbook()
#
#     # по умолчанию создается с таблицей Sheet
#     # print(book.sheetnames)
#
#     sheet_0 = book.active
#     book.remove(sheet_0)
#     # создаю таблицы
#     # book.active.title = "Коллеги"
#     sheet_1 = book.create_sheet("Коллеги")
#     sheet_2 = book.create_sheet("Клиенты")
#     sheet_3 = book.create_sheet("Черный список", 0)  # таблица будет первой
#     data_values = [
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
#         [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
#
#     ]
#     sheet_1.append(data_values)  # записываю данные в строки таблиц
#
#     book.save("test.xlsx")
#     book.close()
