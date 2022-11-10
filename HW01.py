L = ['Hello', 'world']
M = L
print(M is L)  # True
M.append('!')
print(L)  # ['Hello', 'world', '!']
M = L.copy()
print(M is L)  # False

# Работа со строками
# Функция Lambda и reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x, y: y - x, numbers))  # Ответ 5 .
'''     1-0=1
        2-1=1
        3-1=2
        4-2=2
        5-2=3
        6-3=3
        7-3=4
        8-4=4
        9-4=5
        10-5=5 '''
# Сортировка sorted  метод a.sort(_)
print(reduce(lambda x, y: y + x, numbers))  # Ответ 54
f = lambda z: abs(z)
a = sorted(numbers, key=f)
print(a)  # Ответ [0, 1, 2, 3, 4, 4, 5, 6, 6, 8, 15]

# Домен
email = "nevasv@yandex.ru"
domain = email.split("@")[1]
print(domain)  # Ответ  yandex.ru

# Сумма при условии Деление на три нацело
s = sum(I for I in numbers if I % 3 == 0)
print(s)  # Ответ 30  6+3+6+15

fib1, fib2 = 1, 1

n_input = 201
if 100 < n_input < 999:
    if n_input % 2 != 0:
        print("не делится на 2 ")
    elif n_input % 3 != 0:
        print("число не делится на 3 ")
    else:
        print("число удовлетворяет")
else:
    print("Число не в диапазоне")

T = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(T)

