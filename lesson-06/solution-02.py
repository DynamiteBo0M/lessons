"""
Доработать первое задание так, чтобы словарь читался из текстового CSV файла,
где на каждой строке пары слов вида: apple,яблоко.
"""

import csv

def translate_en_to_ru(dictionary, word):
    return dictionary[word]


def translate_ru_to_en(dictionary, word):
    for en, ru in dictionary.items():
        if word == ru:
            return en


def load_dictionary():
    result = {}
    with open("dictionary.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            result[row[0]] = row[1]
    return result


if __name__ == "__main__":
    dictionary = load_dictionary()

    print(translate_ru_to_en(dictionary, "солнце"))
    print(translate_en_to_ru(dictionary, "moon"))