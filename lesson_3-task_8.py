# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

my_list = []

user_list = [int(i) for i in input('Введите 4 числа через пробел: ').split()]
my_list.append(user_list)
user_list = [int(i) for i in input('Введите еще 4 числа через пробел: ').split()]
my_list.append(user_list)
user_list = [int(i) for i in input('Введите еще 4 числа через пробел: ').split()]
my_list.append(user_list)
user_list = [int(i) for i in input('Введите еще 4 числа через пробел: ').split()]
my_list.append(user_list)

for i in range(4):

    my_list[i].append(my_list[i][0] + my_list[i][1] + my_list[i][2] + my_list[i][3])

for i in range(4):
    print(*my_list[i])
