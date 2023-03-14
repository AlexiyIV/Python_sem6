# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума)

import random

arr_min = int(input('введите мин элемент массива '))
arr_max = int(input('введите макс элемент массива '))
n = int(input('введите количество элементов массива '))
r_st = int(input('введите начало диапазона '))
r_end = int(input('введите конец диапазона '))
array = [random.randint(arr_min,arr_max) for i in range(n)]
array_ind = []
for i in range(len(array)):
    if r_st<=array[i]<=r_end: array_ind.append(i)
print(array)
print(array_ind)