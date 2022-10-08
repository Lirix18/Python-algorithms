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


print(dec_mem_even_odd(75835768237632762676983276098160983270698203069837609837))

@decor_mem
def even_odd_opti(num):
    even = 0
    odd = 0
    while num != 0:
        if num % 2:
            even += 1
        else:
            odd += 1
        num = num // 10
    return f'четных цифр {even}, нечетных {odd}'

print(even_odd_opti(75835768237632762676983276098160983270698203069837609837))


"""
Цикл гораздо экономичнее по использованию памяти, чем рекурсия
"""

