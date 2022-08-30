# slice(start, stop, step)
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