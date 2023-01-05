# map(function, iter1, iter2, ...)

L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))  # ['this', 'is', 'lower', 'string']


# def filter(func, cont):
#     outp = []
#     for x in cont:  # проходим циклом по итерируемому объекту
#         if func(x):  # проверяем условие для каждого элемента
#             outp.append(x)  # если True, добавляем в новый список
#     return outp


# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))  # [1, 2]

# map + filter
some_list = [i - 10 for i in range(20)]


def pow2(x): return x ** 2


def positive(x): return x > 0


print(some_list)
print(list(map(pow2, filter(positive, some_list))))
# То же

L = [i ** 2 for i in some_list if i > 0]
print(L)

# map(func, list1)  # итератор, но никаких вычислений не будет произведено
# list(map(...))  # только здесь появляется объект
#
# [func(i) for i in list1]  # сразу готовый объект
#
#
# [func(i) for i in list1] == list(map(func, list1))  # результат один и тот же

# # эти две функции выполняют одно и тоже складывают два числа
# def my_function(x1, x2):  # Обычная функция
#    return x2 + x1
#
# lambda x1, x2: x2 + x1  # Анонимная функция

d = {2: "c", 1: "d", 4: "a", 3: "b"}

# Чтобы отсортировать его по ключам нужно сделать так
print(dict(sorted(d.items())))  # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
# (вес, рост)
data = [
    (82, 1.91),
    (68, 1.74),
    (90, 1.89),
    (73, 1.79),
    (76, 1.84)
]
sorted(data, key=lambda x: x[0] / x[1] ** 2)
# свой рост в сантиметрах возвести в квадрат, потом массу тела в килограммах разделить на полученную цифру
print(data)
print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу

a10 = ["asd", "bbd", "ddfa", "mcsa"]
print( list(map(len, a10)))
print([str.upper(i) for i in a10])
