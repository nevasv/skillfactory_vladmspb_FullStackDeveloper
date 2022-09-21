print(list(str(123456789)))
print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
for e in str(123456789):
    print(e, end="")
print(list(map(int, list(str(123456789)))))
print(5 in list(map(int, list(str(123456789)))))

n = 612345
m = str(n)
if int(m[0]) % 2 == 0:
    print("туту")
print("5" in str(n))


list_1 = [1, 2]

list_2 = [1, 2, 3]
val = list_2.pop()
print("........")
print(list_1 == list_2)
print(id(list_1) == id(list_2))


if int(input("Введи цену")) < 2700:
    print("покупаем")
else:
    print("дорого")
password = input("Введите пароль: ")
if password:
    pass1 = str(password)
else:
    print("Вы забыли ввести пароль")


a, b = 1, 2

min = a if a < b else b


one = 12
two = 30

print(min if one % 2 and two % 2 else None)

