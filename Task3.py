"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
"""


def recur(num, rc=''):
    if num < 1:
        print(rc)
        return
    else:
        rc += str(num % 10)
    return recur(num // 10, rc)

recur(5678)