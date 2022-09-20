import time

"""___________a)___________"""


def decor(func):
    def wrapper(*args):
        now = time.time()
        result = func(*args)
        print((time.time() - now))
        return result

    return wrapper


@decor
# O(n)
def list_gen(n):
    return [i for i in range(0, n)]


@decor
# O(n)
def dict_gen(n):
    return {i: None for i in range(0, n)}


list1 = list_gen(9999999)
dict1 = dict_gen(9999999)

# Словарь заполняется дольше, так как для него создается хэш-таблица

"""___________b)___________"""


@decor
# O(n)
def list_search1(inp_list, elem):  # O(n)
    for i in inp_list:  # O(n)
        if i == elem:  # O(1)
            return i  # O(1)


@decor
# # O(log n) так как список сортированный, то можно воспользоваться бинарным поиском
def list_search2(inp_list, elem):
    low = 0
    high = len(inp_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = inp_list[mid]
        if guess == elem:
            return mid
        if guess > elem:
            high = mid - 1
        else:
            low = mid + 1
    return None


@decor
# O(1)
def dict_search(inp_dict, elem):
    return inp_dict[elem]


list_elem1 = list_search1(list1, 9999998)
list_elem2 = list_search2(list1, 9999998)
dict_elem = dict_search(dict1, 9999998)

# Получение элемента из словаря быстрее, так как происходит за одну операцию

"""___________b)___________"""

@decor
# O(n)
def list_del(inp_list, elem):
    inp_list.remove(elem)


@decor
# O(1)
def dict_del(inp_dict, elem):
    del inp_dict[elem]


list_del(list1, 9999998)
dict_del(dict1, 9999998)

# Удаление из словаря быстрее, так как время выполнения константа