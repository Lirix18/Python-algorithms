from random import randint
from timeit import timeit


# сортировка Шелла
def shell_sort(lst):
    step = len(lst) // 2
    while step > 0:
        for i in range(step, len(lst)):
            j = i
            delta = j - step
            while delta >= 0 and lst[delta] > lst[j]:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst


# 10 элементов
m = 5
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=1000))
print(f'Медиана - {shell_sort(orig_list[:])[m]}')

# 100 элементов
m = 50
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=1000))
print(f'Медиана - {shell_sort(orig_list[:])[m]}')

# 1000 элементов
m = 500
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=1000))
print(f'Медиана - {shell_sort(orig_list[:])[m]}')
