# Работа со строками
# Подсчет вхождений
Vhojdeniya = {}
for letter in "Mississippi":
    Vhojdeniya[letter] = Vhojdeniya.get(letter, 0) + 1
print(Vhojdeniya)  # Ответ {'M': 1, 'i': 4, 's': 4, 'p': 2}
# Срезы
numbers = [0, 1, 6, 3, 4, 5, 6, 15, 8, 2, 4]
new_numbers = numbers[::3]
print(new_numbers)  # Ответ [0, 3, 6, 2]
print(sum(numbers[::3]))  # Ответ 11
print(list(filter(lambda x: x % 3 == 0, numbers)))  # Ответ [0, 6, 3, 6, 15]
print(list(map(lambda x: x % 3 == 0,
               numbers)))  # Ответ [True, False, True, True, False, False, True, True, False, False, False]
# Круговой сдвиг
print(numbers[-1:] + numbers[:-1])  # Ответ [4, 0, 1, 6, 3, 4, 5, 6, 15, 8, 2]
Posledniy = numbers.pop()
print(Posledniy)
numbers.insert(0, Posledniy)  # Ответ 4
print(numbers)
# Функция Lambda и reduce
from functools import reduce

print(reduce(lambda x, y: y - x, numbers))  # Ответ 5
'''1-0=1
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

# Сумма при условии леление на три нацело
s = sum(I for I in numbers if I % 3 == 0)
print(s)  # Ответ 30  6+3+6+15

