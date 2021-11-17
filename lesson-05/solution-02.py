"""
Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их сумму и максимальное из
них.
"""

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

my_list = [1, 4, 5, 11, 43]
print(my_sum(*my_list))