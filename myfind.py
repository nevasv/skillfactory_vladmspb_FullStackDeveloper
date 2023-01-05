def find(array, element):
    """
    Поиск первого элемента в массиве перебором значений и сравнением с element O(n)
    :param array: массив значений через пробел
    :param element: какое значение искать
    :return: i порядковый номер element-1
    """
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


def count(array, element):
    """
    Число вхождений элемента в массив
    :param array: массив значений через пробел
    :param element: какое значение искать element
    :return: число  element в массиве
    """
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count


array = list(map(int, input("Вводите элементы массива разделяя их пробелом: ").split()))
element = int(input("Вводите элемент который нужно искать: "))

print(find(array, element))
print(count(array, element))


def binary_search(array, element, left, right):
    """
    Двоичный поиск O(log(n)) в отсортированном массиве array элемента element
    :param array: Здесь упорядоченная последовательность range(1, 100)
    :param element: Введите искомое число
    :return: Индекс в упорядоченном пронумерованом списке элементов массива

    Examples
    ________
    >>> array(1,8,16,17,21,19,32,33,54,67,87,92)
    """
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input("вводите число 1-99 ,которое будет искаться: "))
array = [i for i in range(1, 100)]  # 1,2,3,4,...99
# запускаем алгоритм на левой и правой границе
print(f'индекс этого числа в массиве: {binary_search(array, element, 0, 98)}')
