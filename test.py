import math

print(round(float(11 * 2.5 / 3), 2))

print(round(math.pi / 2, 2))
colors = 'red blue green'

print(colors.split())
# ['red', 'blue', 'green']

path = '/home/user/documents/file.txt'

print(path.split('/'))  # разделитель можно указать в качестве аргумента
# ['', 'home', 'user', 'documents', 'file.txt']

colors_split = colors.split()  # список цветов по-отдельности

colors_joined = ' and '.join(colors_split)  # объединение строк
print(colors_joined)
# red and green and blue


a = 120
b = ""

print(id(a))
print(id(b))

a = None
b = None


def linear_solve(a, b):
    x = b / a
    return x


print(linear_solve(0, 1))
