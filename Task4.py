from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    elem = max(array, key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))

"""
Первые 2 функции занимают больше времени, так как в них используется цикл.
Третий вариант занимает меньшее количество времени, так как сразу определяет
определяется число, которое встречается в массиве чаще всего. 
"""