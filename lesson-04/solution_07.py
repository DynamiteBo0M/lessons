"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ, из этих чисел составляется первый список. Далее таким же образом вводятся второй и третий списки. Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем.
"""

# Creating a list which contains three lists inside
my_list = [[], [], []]

# Filling in all three lists from user's input
for index in range(0, 3):
    # Read numbers from user's input till we get string
    print("Please enter elements for a list #" + str(index))
    while True:
        my_string = input()
        try:
            my_number = int(my_string)
        except ValueError:
            break
        my_list[index].append(my_number)

# Get elements which are common for the first and the second lists
# And delete from the result elements which are present in the third list
list_intersection = list(set(my_list[0]) & set(my_list[1]))
list_difference = set(list_intersection) - set(my_list[2])

print(list_difference)
