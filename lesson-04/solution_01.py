"""
Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
"""

my_list = [5, 7, 13, 24, 4, 8, 11]

result = 0

for x in my_list:
    if x > 10:
        result += x
        
print(result)
