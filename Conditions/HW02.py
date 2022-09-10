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

print(list_1 == list_2)