"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить, причем сам себе
человек не может подарить, дубликаты тоже не допустимы.
"""


import random

people = []

while True:
    person = input("Enter a person participating.(end to exit):\n")
    if person == "end":
        break
    people.append(person)

random.shuffle(people)
for i in range(len(people)//2):
    print(people[i], "buys for", people[i+len(people)//2])
