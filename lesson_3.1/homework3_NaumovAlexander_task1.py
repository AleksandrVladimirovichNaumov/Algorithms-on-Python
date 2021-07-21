"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать,
   так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def time_spend(func):
    def g(obj, *args, **kwargs):
        time_period = time.perf_counter()
        func(obj, *args, **kwargs)
        time_period = time.perf_counter() - time_period
        return f'Spent time for {func}: {time_period}'

    return g


@time_spend
def data_to_list(list_obj, *args):
    """
    добавление всех аргументов в список
    :param list_obj: список, в который будут добавляться элементы
    :param args: данные, которые будут добавлены в список
    :return: список с аргументами
    O(n) = n
    """
    for i in args:                  # O(n)
        list_obj.append(i)          # O(1)
    return list_obj                 # O(1)


@time_spend
def data_to_dict(dict_obj, **kwargs):
    """
    добавление всех аргументов в список
    :param dict_obj: словарь, в который будут добавляться элементы
    :param kwargs: данные, которые будут добавлены в словарь
    :return: словарь с аргументами
    O(n) = n
    """
    for k, v in kwargs.items():     # O(n)
        dict_obj[k] = v             # O(1)
    return dict_obj                 # O(1)


@time_spend
def actions_with_list(list_obj):
    # O() = n
    items_in_list = len(list_obj)                           # O(1) + O(1)
    first_item = list_obj[0]                                # O(1) + O(1)
    new_list = list(list_obj)                               # O(1) + O(n)
    return items_in_list, first_item, new_list


@time_spend
def actions_with_dict(dict_obj):
    # O() = n
    items_in_dict = len(dict_obj)                           # O(1) + O(1)
    first_item = dict_obj['k1']                             # O(1) + O(1)
    new_dict = dict(dict_obj)                               # O(1) + O(n)
    return items_in_dict, first_item, new_dict


@time_spend
def remove_from_list(list_obj, *args):
    # O() = n^2
    for i in args:                      # O(n)
        try:
            list_obj.remove(i)          # O(n)
        except Exception as e:
            print(e)
    return list_obj


@time_spend
def remove_from_dict(dict_obj, *args):
    # O() = n
    for i in args:                      # O(n)
        try:
            del dict_obj[i]             # O(1)
        except Exception as e:
            print(e)
    return dict_obj


list_1 = []
dict_1 = {}

print(data_to_list(list_1, 1, "string", None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(data_to_dict(dict_1, k1=1, k2="string", k3=None, k4=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k5=5))

print(actions_with_list(list_1))
print(actions_with_dict(dict_1))

print(remove_from_list(list_1, 1, "string", None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(remove_from_dict(dict_1, 'k1', "k2", 'k3', 'k4', 'k5'))

"""
В предыдущей версии практического задания в функциях использовал return print(). Это влияло на затраченное время.

Результаты:
1) добавление элементов с список с помощью метода append() происходит быстрее чем добавление значения в словарь;
2) операции на получения значений, а также использование  len() или list()/dict() занимают примерно одинаковое время;
3) поэлементное удаление значений из словаря примерно в 3 быстрее чем поэлементное удаление значений из списка.
"""
