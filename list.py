List_name = [
    1,
    2,
    3,
    ['Имя', 'Фамилия', 'Отчество'],
]
print(List_name[3][1])          # Фамилия
print(List_name[1:4])           #  [2, 3, ['Имя', 'Фамилия', 'Отчество']]
print(List_name[1:])             #  то же
print(List_name[:3])             #  1,2,3
print(List_name[::2])            #  1,3       шаг равен два
print(List_name[-3])             #  2         считаем с лева
print(List_name[-3:-1])          #  2, 3   
print(List_name[::-1])           # (4,5,6),3,2,1   или  List_name.revers()  
print("это порядковый номер в списке элемента \"3\"= " + str(List_name.index(3)))      # это порядковый номер в списке

people = [['Alice', 25, 'blonde'],
           ['Bob', 33, 'black'],
           ['Ann', 18, 'purple']]
for person in people:
    print("|", end=" ")
    for item in person:
        if person.index(item) == len(person)-1:
            print(item, end='')
            continue
        print(item, end=" * ")
    print("|")
# '''
# list.append(x)                Добавляет элемент в конец списка
# list.extend(L)                Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x)             Вставляет на i-ый элемент значение x
# list.remove(x)                Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i])                 Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]])Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x)                 Возвращает количество элементов со значением x
# list.sort([key=функция])	    Сортирует список на основе функции
# list.reverse()                Разворачивает список
# list.copy()                   Поверхностная копия списка
# list.clear()                  Очищает список
# '''
#
import  copy
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
z = copy.deepcopy(x)
x[2][2] = 'Hello'
print(x)
print(z)
