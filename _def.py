x: int = 3


def func():
    global x  # объявляем, что переменная является глобальной
    print(x)
    x = 5
    x += 5

    return x


print(func())
''' ********************************************************************************'''


def get_my_func():
    def hello_world():
        print("Hello")

    return hello_world


hello_world_func = get_my_func()  # получить функцию в качестве результата

print(type(hello_world_func))  # <class 'function'>
hello_world_func()  # Hello
'''*********************************************************************************'''


def get_mul_func(m):
    nonlocal_m = m

    def local_mul(n):
        return n * nonlocal_m

    return local_mul


two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
d = two_mul(5)  # 5 * 2
print(str(d) + "  # 5 * 2")
"""***********************************************************************************"""


def my_func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


my_func()
# <class 'tuple'>
# <class 'dict'>
'''************ Рекурсивный вызов ***************************************************'''


def reverse_str(string):
    if len(string) == 0:
        return ''
    else:
        return string[-1] + reverse_str(string[:-1])


t = reverse_str('Test')  # tseT
print(t)
