# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

# Блок-схемы https://drive.google.com/file/d/1Sd1RMmLY01QV29HP8IGyy4Z54XGyRWx6/view?usp=sharing

n = int(input('Введите число: '))
a = 1
sum = 1

for i in range(n - 1):
    a = a / (-2)
    sum += a

print(sum)
