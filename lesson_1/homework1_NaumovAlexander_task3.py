"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

companies_profit = {
    'Horns & Hoofs': 300,
    'MMM': 450,
    "Ashot's Pizza": 10,
    'Pink Rabbit': 100,
    "Bill_Gates_tip": 1000
}


def profit_leaders_1(dict_obj):
    """
    Function finds 3 keys from dictionary with 3 biggest values.
    :param dict_obj: three keys with biggest values will be selected from this dictionary
    :return: three keys in a list
    T(n) = 1 + n * log(n) + 1 + 1 + 1 + 3 = n * log(n) + 7
    O(n) = n * log(n)
    """

    return sorted(dict_obj, key=dict_obj.get, reverse=True)[:3]
    # return            O(1)
    # sorted()          O(n * log(n))       - Did not find in teacher's materials. Got it from google.
    # key =             O(1)                - not sure does it affect O() in function parameters
    # dict_obj.get      O(1)
    # reverse=          O(1)                - not sure does it affect O() in function parameters
    # [:3]              O(3)


def profit_leaders_2(dict_obj):
    """
    Function finds 3 keys from dictionary with 3 biggest values.
    :param dict_obj: three keys with biggest values will be selected from this dictionary
    :return: three keys in a list
    T(n) = 1 + 1 + n + 3 * (1 + n + 1 + 1 + 1 + 1 + 1) + 1 = 3 + n + 3 * n + 15 = 18 + 4 * n
    O(n) = n
    """
    companies_leaders = []                                                          # O(1)
    # not to cut original dictionary after del
    companies_dict = dict_obj.copy()                                                # O(1) + O(n)
    for i in range(3):                                                              # O(3)
        companies_leaders.append(max(companies_dict, key=companies_dict.get))       # O(1) + O(n) + O(1) + O(1) + O(1)
        del companies_dict[companies_leaders[-1]]                                   # O(1) + O(1)
    return companies_leaders                                                        # O(1)


def profit_leaders_3(dict_obj):
    """
    Function finds 3 keys from dictionary with 3 biggest values.
    :param dict_obj: three keys with biggest values will be selected from this dictionary
    :return: three keys in a list
    T(n) = n + 1 + 1 + 1 + n * (30) + 1 = 4 + 31 * n
    O(0) = n
    """
    companies_leaders = ['', '', '']                            # O(n)
    first_profit = 0                                            # O(1)
    second_profit = 0                                           # O(1)
    third_profit = 0                                            # O(1)
    for i in dict_obj:                                          # O(n)
        if first_profit < dict_obj[i]:                              # O(1) + O(1)
            third_profit = second_profit                            # O(1)
            second_profit = first_profit                            # O(1)
            first_profit = dict_obj[i]                              # O(1) + O(1)
            companies_leaders[2] = companies_leaders[1]             # O(1) + O(1) + O(1)
            companies_leaders[1] = companies_leaders[0]             # O(1) + O(1) + O(1)
            companies_leaders[0] = i                                # O(1) + O(1)
        elif second_profit < dict_obj[i]:                           # O(1) + O(1)
            third_profit = second_profit                            # O(1)
            second_profit = dict_obj[i]                             # O(1) + O(1)
            companies_leaders[2] = companies_leaders[1]             # O(1) + O(1) + O(1)
            companies_leaders[1] = i                                # O(1) + O(1)
        elif third_profit < dict_obj[i]:                            # O(1) + O(1)
            third_profit = dict_obj[i]                              # O(1) + O(1)
            companies_leaders[2] = i                                # O(1) + O(1)
    return companies_leaders                                    # O(1)


# checking that functions works ok
print(profit_leaders_1(companies_profit))
print(profit_leaders_2(companies_profit))
print(profit_leaders_3(companies_profit))

"""
Result:
1) function #1 profit_leaders_1() has the smallest complexity because it is O(n) = n * log(n);
2) function #2 & #3  will work slower because its complexity is O(0) = n;
3) function #2 will work faster then function #3 because coefficient before n is smaller (4 * n < 31 * n)
"""