from random import randint
from timeit import timeit
from statistics import median

# 10 элементов
m = 5
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(orig_list[:])', globals=globals(), number=1000))
print(f'Медиана - {median(orig_list[:])}')

# 100 элементов
m = 50
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(orig_list[:])', globals=globals(), number=1000))
print(f'Медиана - {median(orig_list[:])}')

# 1000 элементов
m = 500
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(orig_list[:])', globals=globals(), number=1000))
print(f'Медиана - {median(orig_list[:])}')

"""
Эффективнее оказался способ с использованием встроенной функции median
"""