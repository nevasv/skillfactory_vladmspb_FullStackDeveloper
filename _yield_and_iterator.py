'''******************** Герератор в одну строку*****************************************'''

a = [11, 22, 33]
l = [i**2 for i in range(10)]
g = (i**2 for i in range(10))
print(l)
print(g)
c = iter(a)
print(next(c))
print(next(c))
print(next(c))


print('''***********************************************************************************''')
def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step


my_gen = count(30, 10)

for i in range(5):
    print(next(my_gen))
'''*****************************************************************************'''


def repeat_list(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value


for i in repeat_list([1, 2, 3, 4]):
    print(i)
    if i == 4:
        break

# для примера возьмём строку
str_ = "my tst"
str_iter = iter(str_)

print(type(str_))  # строка
print(type(str_iter))  # итератор строки
# Получим первый элемент строки
print(next(str_iter))  # m

# Получим ещё несколько элементов последовательности
print(next(str_iter))  # y
print(next(str_iter))  #
print(next(str_iter))  # t
print(next(str_iter))  # s
print(next(str_iter))  # t
print("**************************************************************")


def my_gen_i():
    for i in range(3):
        yield i
    yield "Конец"


last_i = my_gen_i()
for i in range(4):
    print(next(last_i))
