# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

my_dict = {a: 0 for a in range(2, 10)}

for i in range(2, 100):

    if i % 2 == 0:
        my_dict[2] += 1
        if i % 4 == 0:
            my_dict[4] += 1
            if i % 8 == 0:
                my_dict[8] += 1

    if i % 3 == 0:
        my_dict[3] += 1
        if i % 6 == 0:
            my_dict[6] += 1
        if i % 9 == 0:
            my_dict[9] += 1

    if i % 5 == 0:
        my_dict[5] += 1

    if i % 7 == 0:
        my_dict[7] += 1

print(*my_dict.items())
