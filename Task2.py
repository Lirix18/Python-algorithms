from Decor_memory import decor_mem
@decor_mem
def dec_mem_even_odd(num):
    def even_odd(num, even=0, odd=0):
        if num < 1:
            return f'нечетных цифр: {odd}, четных цифр: {even}'
        if num % 2:
            odd += 1
        else:
            even += 1
        return even_odd(num // 10, even, odd)
    return even_odd(num)

"""
Без обертки в другую функцию на каждый вызов рекурсии создается отдельная таблица profile.
При обертки в функцию вся статистика объединяется в одну таблицу
"""