from random import randint
from timeit import timeit


def median_search(lst):
    array = lst[:]
    while len(array) > len(lst) // 2 + 1:
        array.remove(max(array))
    return max(array)


# 10 элементов
m = 5
orig_list = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(timeit('median_search(orig_list[:])', globals=globals(), number=100))
print(f'Медиана - {median_search(orig_list)}')

# 100 элементов
m = 50
orig_list = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(timeit('median_search(orig_list[:])', globals=globals(), number=100))
print(f'Медиана - {median_search(orig_list)}')

# 1000 элементов
m = 500
orig_list = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(timeit('median_search(orig_list[:])', globals=globals(), number=100))
print(f'Медиана - {median_search(orig_list)}')