"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


# 1 сложность O(1) + O(n) * O(n) + O(n) + O(1) + O(1) = O(n^2)
def min_num1(spisok):
    minimum = spisok[0]                 # O(1)
    for i in spisok:                    # O(n)
        for k in range(len(spisok)):    # O(n)
            if minimum > spisok[k]:     # O(n)
                minimum = spisok[k]     # O(1)
    return minimum                      # O(1)


# 2 сложность O(1) + O(n) + O(n) + O(1) + O(1) = O(n)
def min_num2(spisok):
    minimum2 = spisok[0]                # O(1)
    for i in spisok:                    # O(n)
        if i < minimum2:                # O(n)
            minimum2 = i                # O(1)
    return minimum2                     # O(1)

list1 = (5, 7, 100, 1, 25, -1)
print(min_num1(list1))
print(min_num2(list1))
