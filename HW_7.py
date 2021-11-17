# 1
import random


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                flag = False

        if flag == True:
            break
    return array


size = 50
min = -100
max = 100
array = [random.randint(min, max) for _ in range(size)]

print('Массив:', array, sep='\n')
bubble_sort(array)
print('После сортировки:', array, sep='\n')


# 2

import random


def merge_sort(a):
    if len(a) < 2:
        return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:len(a)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a[k] = right[j]
        j = j + 1
        k = k + 1
    return a


SIZE = 12
array = [random.uniform(0, 50) for i in range(SIZE)]
print('Массив:', array, sep='\n')
print('После сортировки:', merge_sort(array), sep='\n')

# 3 ...