"""
Задание 5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def find_ascii(result='', num=32):
    if num > 127:
        print(result)
        return ''
    result += f'{num} - {chr(num)}  '
    if not (num - 1) % 10:
        print(result)
        result = ''
    return find_ascii(result, num + 1)


find_ascii()
