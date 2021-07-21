"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""


# function which use only set{}
def unique_substring_1(str_obj):
    substring_set = set()
    for i in range(len(str_obj)):
        for j in range(len(str_obj)):
            if i + j < len(str_obj) and i + j != 0:
                substring_set.add(str_obj[j:len(str_obj) - i])
    print(f'Quantity of substrings is {len(substring_set)}: {substring_set}')


# function which use dict + hash function
def unique_substring_2(str_obj):
    substring_dict = dict()
    for i in range(len(str_obj)):
        for j in range(len(str_obj)):
            if i + j < len(str_obj) and i + j != 0:
                substring = str_obj[j:len(str_obj) - i]
                substring_dict[hash(substring)] = substring
    print(f'Quantity of substrings is {len(substring_dict)}: {substring_dict.values()}')


unique_substring_1('papa')
unique_substring_2('papa')
