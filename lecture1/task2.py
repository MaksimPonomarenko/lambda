"""
Напишите функцию, которая принимает 3 числа, сравнивает
между собой и возвращает количество совпадающих чисел.
"""

def matchAmount(x, y, z):
    if x == y == z:
        return 3
    elif x == y or x == z or y == z:
        return 2
    else:
        return 0
