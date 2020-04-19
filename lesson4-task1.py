# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# Меняю условие с ввода на генерирование списка

# Признаюсь, у меня не получается сделать хоть сколько-то полезных выводов из полученной картины. Пару дней
# провозился с разными задачами, но наглядных данных как в уроке не выходит.

import random
import timeit
import cProfile


# Способ первый, цикл

def evenodd(size):

    my_list = [random.randint(1,101) for i in range(size)]
    even = 0
    odd = 0

    for i in range(size):
        if my_list[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    return f'Четных — {even}, нечетных — {odd}'

# print(evenodd(15)) # для проверки

print(timeit.timeit('evenodd(5)', number=100, globals=globals())) # 0.0014007789999999978
print(timeit.timeit('evenodd(10)', number=100, globals=globals())) # 0.002947551999999999
print(timeit.timeit('evenodd(15)', number=100, globals=globals())) # 0.0038863199999999987
print(timeit.timeit('evenodd(20)', number=100, globals=globals())) # 0.0046175020000000025
print(timeit.timeit('evenodd(25)', number=100, globals=globals())) # 0.005888375000000001

cProfile.run('evenodd(5)') # 1    0.000    0.000    0.000    0.000 les2-task2 2.py:12(evenodd)
cProfile.run('evenodd(10)') # 1    0.000    0.000    0.000    0.000 les2-task2 2.py:12(evenodd)
cProfile.run('evenodd(15)') # 1    0.000    0.000    0.000    0.000 les2-task2 2.py:12(evenodd)
cProfile.run('evenodd(20)') # 1    0.000    0.000    0.000    0.000 les2-task2 2.py:12(evenodd)
cProfile.run('evenodd(25)') # 1    0.000    0.000    0.000    0.000 les2-task2 2.py:12(evenodd)

# Способ второй, цикл с дополнительными списками

my_list5 = [random.randint(1,101) for i in range(5)]
my_list10 = [random.randint(1,101) for i in range(10)]
my_list15 = [random.randint(1,101) for i in range(15)]
my_list20 = [random.randint(1,101) for i in range(20)]
my_list25 = [random.randint(1,101) for i in range(25)]
even = 0
odd = 0

def evenodd2(list):

    even_list = []
    odd_list = []

    for item in list:
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)

    return f'Четных — {len(even_list)}, нечетных — {len(odd_list)}'

# print(evenodd2(my_list15)) # для проверки

print(timeit.timeit('evenodd2(my_list5)', number=100, globals=globals())) # 0.0001815680000003539
print(timeit.timeit('evenodd2(my_list10)', number=100, globals=globals())) # 0.00026748400000009553
print(timeit.timeit('evenodd2(my_list15)', number=100, globals=globals())) # 0.0003606129999997876
print(timeit.timeit('evenodd2(my_list20)', number=100, globals=globals())) # 0.00042545699999996245
print(timeit.timeit('evenodd2(my_list25)', number=100, globals=globals())) # 0.0005167500000000658

cProfile.run('evenodd2(my_list5)') # 1    0.000    0.000    0.000    0.000 les2-task2 3.py:20(evenodd2)
cProfile.run('evenodd2(my_list10)') # 1    0.000    0.000    0.000    0.000 les2-task2 3.py:20(evenodd2)
cProfile.run('evenodd2(my_list15)') # 1    0.000    0.000    0.000    0.000 les2-task2 3.py:20(evenodd2)
cProfile.run('evenodd2(my_list20)') # 1    0.000    0.000    0.000    0.000 les2-task2 3.py:20(evenodd2)
cProfile.run('evenodd2(my_list25)') # 1    0.000    0.000    0.000    0.000 les2-task2 3.py:20(evenodd2)

# Способ третий, цикл с вычитанием

def evenodd3(size):

    my_list = [random.randint(1,101) for i in range(size)]
    even = 0

    for i in range(size):
        if my_list[i] % 2 == 0:
            even += 1

    odd = size - even

    return f'Четных — {even}, нечетных — {odd}'

# print(evenodd3(15)) # для проверки

print(timeit.timeit('evenodd3(5)', number=100, globals=globals())) # 0.001554220000000002
print(timeit.timeit('evenodd3(10)', number=100, globals=globals())) # 0.0028617569999999995
print(timeit.timeit('evenodd3(15)', number=100, globals=globals())) # 0.004005931999999997
print(timeit.timeit('evenodd3(20)', number=100, globals=globals())) # 0.0052838409999999975
print(timeit.timeit('evenodd3(25)', number=100, globals=globals())) # 0.006087327999999996

cProfile.run('evenodd3(5)') # 1    0.000    0.000    0.000    0.000 les2-task2.py:11(evenodd3)
cProfile.run('evenodd3(10)') # 1    0.000    0.000    0.000    0.000 les2-task2.py:11(evenodd3)
cProfile.run('evenodd3(15)') # 1    0.000    0.000    0.000    0.000 les2-task2.py:11(evenodd3)
cProfile.run('evenodd3(20)') # 1    0.000    0.000    0.000    0.000 les2-task2.py:11(evenodd3)
cProfile.run('evenodd3(25)') # 1    0.000    0.000    0.000    0.000 les2-task2.py:11(evenodd3)
