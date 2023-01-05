import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счетчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count)


# 290698

def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


step = 0
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(len(array)):  # проходим по всему массиву

    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i + 1, len(array)):
        step += 1
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(step)

array2 = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array2)):
    for j in range(len(array2) - i - 1):
        if array2[j] > array2[j + 1]:
            array2[j], array2[j + 1] = array2[j + 1], array2[j]

print(array2)

count = 0

array4 = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(1, len(array4)):
    x = array4[i]
    idx = i
    while idx > 0:
        count += 1
        if array4[idx - 1] <= x:
            break
        array4[idx] = array4[idx - 1]
        idx -= 1
    array4[idx] = x

print(count)
