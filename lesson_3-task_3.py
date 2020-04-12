# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

my_list = [random.randint(1, 101) for _ in range(10)]

maximum = my_list[0]
index_max = 0
minimum = my_list[0]
index_min = 0

for i in range(1, len(my_list)):

    if my_list[i] > maximum:
        maximum = my_list[i]
        index_max = i

    elif my_list[i] < minimum:
        minimum = my_list[i]
        index_min = i

print(*my_list, sep=', ')

my_list[index_max], my_list[index_min] = my_list[index_min], my_list[index_max]

print(*my_list, sep=', ')
