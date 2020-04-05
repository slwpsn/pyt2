# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# Блок-схемы — https://drive.google.com/file/d/11mGcB9Poc0QZqxjVP14_TOXe0RAnMXTu/view?usp=sharing

a = int(input('Первое число: '))
b = int(input('Второе число (числа не повторяются): '))
c = int(input('Третье число (числа не повторяются): '))

if a > b:
    m = a
    k = b
else:
    m = b
    k = a

if c > m:
    print('Среднее число:', m)
elif k < c < m:
    print('Среднее число:', c)
else:
    print('Среднее число:', k)
