from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


enter_num = 123456789

print(revers(enter_num))
print(timeit("revers(enter_num)", number=100000, globals=globals()))

print(revers_2(enter_num))
print(timeit("revers_2(enter_num)", number=100000, globals=globals()))

print(revers_3(enter_num))
print(timeit("revers_3(enter_num)", number=100000, globals=globals()))

print(revers_4(enter_num))
print(timeit("revers_4(enter_num)", number=100000, globals=globals()))
"""
3 и 4 функции выполняются быстрее, так как используют встроенные методы Python
"""
