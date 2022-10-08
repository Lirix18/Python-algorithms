from Decor_memory import decor_mem

@decor_mem
def func_1(enter_num):
    return ''.join(reversed(str(enter_num)))


@decor_mem
def func_2(enter_num):
    yield reversed(str(enter_num))


list1 = 123456789

func_1(list1)
func_2(list1)

"""
yield не хранит объекты в памяти, а генерирует элементы на лету и удаляет их, 
как только итератор переходит к следующему элементу.
"""
