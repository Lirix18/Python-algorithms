from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i + 1], lst_obj[i] = lst_obj[i], lst_obj[i + 1]
        n += 1
    return lst_obj


def bubble_sort2(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i + 1], lst_obj[i] = lst_obj[i], lst_obj[i + 1]
                flag = False
        if flag:
            break
        n += 1
    return lst_obj


# замеры 10
orig_list = [randint(-100, 100) for _ in range(10)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(orig_list[:])", globals=globals(), number=1000))

# замеры 100
orig_list = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(orig_list[:])", globals=globals(), number=1000))

# замеры 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(orig_list[:])", globals=globals(), number=1000))

# отсортированный список
orig_list = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(orig_list[:])", globals=globals(), number=1000))

"""
Доработка эффективна только в случае, когда массив отсортирован 
"""
