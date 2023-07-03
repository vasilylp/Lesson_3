"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка содержит число X"""

# N = int(input("Введите число элементов массива : "))
# list_1 = []
# for i in range(N):
#     list_1.append(i)
# print(list_1)
# n = int(input("Введите число : "))
# if n in list_1 and list_1.index(n) != len(list_1)-1:
#     print(list_1[list_1.index(n) - 1], list_1[list_1.index(n) + 1])
# elif n in list_1 and list_1.index(n) == len(list_1)-1:
#     print(list_1[list_1.index(len(list_1)-2)])
# else:
#     print(list_1[list_1.index(len(list_1)-1)])

# 2 solution _________________________________________
N = int(input("Введите число элементов массива : "))
lst = [int(input("Введите массив : ")) for i in range(N)]
x = int(input("Введите число : "))
dif = abs(x - lst[0])
el = lst[0]
for i in lst:
    if abs(x - i) < dif:
        dif = abs(x - i)
        el = i
print(el)