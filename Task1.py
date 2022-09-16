"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
"""


def my_calc():
    calc_symbols = ['+', '-', '*', '/', '0']
    symbol = input('Введите операцию (+, -, *, /) или 0 для выхода: ')
    if symbol not in calc_symbols:
        print('Вы ввели неверный знак операции. Исправьтесь!')
        my_calc()
    if symbol == '0':
        print('Вы закрыли калькулятор.')
        return
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
    except ValueError:
        print('Вы вместо числа ввели строку! Исправьтесь!')
    else:
        if symbol == '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        elif symbol == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        elif symbol == '*':
            print(f'{num1} * {num2} = {num1 * num2}')
        elif symbol == '/' and num2 != 0:
            print(f'{num1} / {num2} = {num1 / num2}')
        else:
            print('На ноль делить нельзя! Исправьтесь!')
    finally:
        my_calc()


my_calc()
