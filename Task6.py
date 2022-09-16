"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
"""
from random import randint


def guess_num(num, attempt=10):
    if attempt == 0:
        return f'Попытки исчерпаны. Загаданное число - {num}'
    print(f'У вас осталось {attempt} попыток.')
    try:
        user_num = int(input('Отгадайте число: '))
    except ValueError:
        print(f'Вы ввели не число! Попытка использована.')
        return guess_num(num, attempt - 1)
    else:
        if user_num == num:
            return f'Поздравляем! Вы отгадали число. это - {num}'
        if user_num > num:
            print('Неверно! Ваше число больше загаданного.')
        else:
            print('Неверно! Ваше число меньше загаданного.')
        return guess_num(num, attempt - 1)


random_num = randint(0, 100)
print(guess_num(random_num))
