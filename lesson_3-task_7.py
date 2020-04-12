# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

my_list = [int(i) for i in input('Введите числа через пробел: ').split()]

for el in my_list:
    el = int(el)

m = my_list[0]

for i in range(len(my_list)):

    if my_list[i] < m:
        m = my_list[i]

my_list.remove(m)

n = my_list[0]

for k in range(len(my_list)):

    if my_list[k] < n:
        n = my_list[k]

print(f'Самые маленькие числа в списке: {m} и {n}.')
