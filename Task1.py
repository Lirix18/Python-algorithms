from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, val in enumerate(nums) if val % 2 == 0]


print(func_1([1, 2, 3, 4, 5, 6, 7, 8]))

print(func_2([1, 2, 3, 4, 5, 6, 7, 8]))

print(timeit("func_1([1, 2, 3, 4, 5, 6, 7, 8])", globals=globals(), number=10000))
print(timeit("func_2([1, 2, 3, 4, 5, 6, 7, 8])", globals=globals(), number=10000))

print(timeit("func_1([1, 2, 3, 4, 5, 6, 7, 8])", globals=globals(), number=10000000))
print(timeit("func_2([1, 2, 3, 4, 5, 6, 7, 8])", globals=globals(), number=10000000))

"""
    0.007811899995431304
    0.011428700003307313
    7.328798400005326
    7.032890699978452
    При использовании list comprehensions на очень большом количестве повторов 
    есть прирост в скорости выполнения,
    на малых количествах повторов - скорость хуже"""



