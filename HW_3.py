# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j - 2] += 1
i = 0
while i < len(a):
    print(i + 2, ' - ', a[i])
    i += 1

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
# 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с
# нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

first_array = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {first_array}')
last_array = []
for i in first_array:
    if i % 2 == 0:
        last_array.append(first_array.index(i))
print(f'Четные индексы элементов первого массива: {last_array}')

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

array = [random.randint(0, 99) for _ in range(10)]
print(f'Дан массив: {array}')
max = array[0]
min = array[0]
for i in array:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = array.index(min)
max_index = array.index(max)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Массив, после изменения элементов {min_index} и {max_index}: {array}')

# 4. Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(0, 12) for _ in range(60)]
max_index = 0
for i in array:
    if array.count(max_index) < array.count(i):
        max_index = array.index(i)
print(f'В массиве: {array}\nЧисло {array[max_index]}, встречается {array.count(max_index)} раз')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

array = [random.randint(-88, 50) for _ in range(48)]
print(f'Дан массив: {array}')
min_index = 0
for i in array:
    if array[min_index] > i:
        min_index = array.index(i)
if array[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {array[min_index]}.'
          f'Находится в массиве на позиции {min_index}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.



# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

r = [random.randint(0, 99) for _ in range(100)]
print(f'Дан массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.



# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
