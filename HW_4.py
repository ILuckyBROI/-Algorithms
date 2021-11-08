# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import random
import cProfile


def create_1():
    first_array = [random.randint(0, 99) for _ in range(10)]
    print(f'Первый массив {first_array}')
    last_array = []
    for i in first_array:
        if i % 2 == 0:
            last_array.append(first_array.index(i))
    print(f'Четные индексы элементов первого массива: {last_array}')


cProfile.run('create_1()')

def create_2():
    from random import randint, seed
    seed(42)
    init_list = [randint(0, 100) for _ in range(10)]
    a = [i for i, item in enumerate(init_list) if item % 2 == 0]
    print(init_list, a)


cProfile.run('create_2()')

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить
# в виде комментариев в файле с кодом.
