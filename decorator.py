import time

def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, которые будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper


def my_function():
    print("Я - оборачиваемая функция!")
    return 0


print(my_function())

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
"""*********************************************************************"""


def decorator_time(fn):
    def wrapper():
        print(f"Запустилась функция {fn}")
        t0 = time.time()
        result = fn()
        dt = time.time() - t0
        print(f"Функция выполнилась. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы

    return wrapper


def pow_2():
    return 10000000 ** 2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458
