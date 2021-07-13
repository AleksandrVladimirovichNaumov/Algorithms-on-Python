"""
Задание 2.
Реализуйте два алгоритма.
Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.
Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""


def find_min_1(list_obj):
    """
    Function returns minimum value from a list
    :param list_obj: list where minimum value should be found
    :return: min_value: minimum value in list_obj
    T(n) = 1 + n * n * (1 + 1) * 1 + 1 = 2 * n^2 +2; O(n^2)
    """
    min_value = list_obj[0]                 # O(1) - константная
    for i in list_obj:                      # O(n) - линейная
        for j in list_obj:                  # O(n) - линейная
            if i < j and i < min_value:     # O(1) - константная
                min_value = i               # O(1) - константная
    return min_value                        # O(1) - константная


def find_min_2(list_obj):
    """
    Function returns minimum value from a list
    :param list_obj: list where minimum value should be found
    :return: min_value: minimum value in list_obj
    T(n) = 1 + n * 1 * 1 + 1 = n^2 +2; O(n^2)
    """
    min_value = list_obj[0]      # O(1) - константная
    for i in list_obj[1:]:       # O(n) - линейная
        if min_value > i:        # O(1) - константная
            min_value = i        # O(1) - константная
    return min_value             # O(1) - константная


print(find_min_1([2, 3, 1, 4, 5, 1]))
print(find_min_2([2, 3, 1, 4, 5, 1]))
