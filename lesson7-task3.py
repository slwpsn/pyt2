# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = 5

length_list = 2 * m + 1

array = [random.randint(0, 100) for i in range(length_list)]

print(f'Список: {array}')

length = len(array)

list_max = []

max_num = array[0]
n = 0

while n <= length // 2 - 1:
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
    list_max.append(max_num)
    array.remove(max_num)
    max_num = 0
    n += 1

list_min = array

median = list_min[0]

for k in range(len(list_min)):
    if list_min[k] > median:
        median = list_min[k]


print(f'Медиана — {median}')



