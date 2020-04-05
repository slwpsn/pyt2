# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# Блок-схемы — https://drive.google.com/file/d/11mGcB9Poc0QZqxjVP14_TOXe0RAnMXTu/view?usp=sharing

a = int(input('Введите трехзначное число: '))

a_first = a // 100
a_second = a % 100 // 10
a_third = a % 10

print(f'Сумма цифр: {a_first + a_second + a_third}, а произведение — {a_first * a_second * a_third}')
