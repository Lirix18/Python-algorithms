from numpy import array
from pympler.asizeof import asizeof



src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


result = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(result)
print(f'Размер до оптимизации: {asizeof(result)}')

list_number = array([number for number in (src[1:]) if number > src[src.index(number) - 1]])
print(list_number)
print(f'Размер после оптимизации: {asizeof(list_number)}')

"""
Модуль Numpy позволил сократить расход памятина массив
"""