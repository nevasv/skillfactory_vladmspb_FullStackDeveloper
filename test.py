import math
print(round(float(11*2.5/3), 2))

print(round(math.pi/2, 2))
colors = 'red blue green'

print(colors.split())
# ['red', 'blue', 'green']

path = '/home/user/documents/file.txt'

print(path.split('/'))      # разделитель можно указать в качестве аргумента
                            # ['', 'home', 'user', 'documents', 'file.txt']

colors_split = colors.split() # список цветов по-отдельности

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue


a = 5
b = 3+2

print(id(a))
print(id(b))

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(list_id_before == list_id_after)
