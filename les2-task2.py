# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# Блок-схемы https://drive.google.com/file/d/1Sd1RMmLY01QV29HP8IGyy4Z54XGyRWx6/view?usp=sharing

a = input('Введите число: ')

even = 0
odd = 0

for i in range(len(a)):
    number = int(a[i])
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'Четных цифр в числе {even}, а нечетных — {odd}')
