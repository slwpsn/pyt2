# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# Блок-схемы — https://drive.google.com/file/d/11mGcB9Poc0QZqxjVP14_TOXe0RAnMXTu/view?usp=sharing

a = input('Введите первую букву на латинице: ')
b = input('Введите вторую букву на латинице: ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

a_pos = alphabet.index(a) + 1
b_pos = alphabet.index(b) + 1
difference = abs(a_pos - b_pos) - 1

print(f'Первая буква — {a_pos}-я в алфавите, а вторая — {b_pos}-я')
print(f'Между ними {difference} букв(ы)')
