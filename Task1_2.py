from Decor_memory import decor_mem

names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

@decor_mem
def func_3(line):
    for i in line:
        name = i.split()[-1].title()
        print(f"Привет, {name}!")

@decor_mem
def func_4(line):
    for i in line:
        print(f"Привет, {i.split()[-1].title()}!")


func_3(names)
print('_' * 30)
func_4(names)

"""
Убрала создание переменной name
"""
