# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

def bubble_sort(arr):

    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print(arr)
        n += 1

    return arr

size = 10
array = [random.randint(-100, 99) for i in range(size)]

print(array)
print(bubble_sort(array))



