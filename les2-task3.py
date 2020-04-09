# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# Блок-схемы https://drive.google.com/file/d/1Sd1RMmLY01QV29HP8IGyy4Z54XGyRWx6/view?usp=sharing

a = input('Введите число: ')


def reverse(a):
    if int(a) % 10 == int(a):
        return a

    else:
        return str((int(a) % 10)) + reverse(a[:-1])


print(reverse(a))
