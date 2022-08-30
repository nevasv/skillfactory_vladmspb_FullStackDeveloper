edibles = ["отбивные", "пельмени", "яйца", "орехи"]
for food in edibles:
    if food == "пельмени":
        print("Я не ем пельмени!")
        break  # Или  continue
    print("Отлично, вкусные " + food)
else:
    print("Хорошо, что не было пельменей!")
print("Ужин окончен.")

fibonacci = [0,1,1,2,3,5,8,13,21]
for i in range(len(fibonacci)):
    print(i,fibonacci[i])

colours = ["красный"]
for i in colours[:]:
    if i == "красный":
        colours += ["черный"]
    if i == "черный":
        colours += ["белый"]
print(colours)

List_name = {"Собака":"Домашнее животное", "Дрозд":"Птица", "Комар":"Насекомое"}
City_name = ["Воронеж", "Новгород", "Смоленск"]
for value in List_name.values():
    print(value)
for index, elem in enumerate(City_name):
    if index % 2 == 0:
        print(elem)      # [0] И [2]  Воронеж Смоленск
        