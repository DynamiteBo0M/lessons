"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".
"""

def month_to_season(mounth):
    if mounth == 12 or mounth == 1 or mounth == 2:
        season = "Winter"
    elif mounth == 3 or mounth == 4 or mounth == 5:
        season = "Spring"
    elif mounth == 6 or mounth == 7 or mounth == 8:
        season = "Summer"
    else:
        season = "Autumn"
    return season

print(month_to_season(9))