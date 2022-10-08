'''
class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def math(self, weight, thickness):
        calc = (self._lenght * self._width * weight * thickness) / 1000
        return f'{calc} т'
'''

class Road:
    __slots__ = '_lenght', '_width'
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def math(self, weight, thickness):
        calc = (self._lenght * self._width * weight * thickness) / 1000
        return f'{calc} т'

"""
Использую __slots__ для экономии памяти
"""

