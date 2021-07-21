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
    inserting all arguments into a list
    :param list_obj: list object where arguments should be add
    :param args: data, which should be added to a list
    :return: list with added arguments
    O(n) = n
    """
    for i in args:                  # O(n)
        list_obj.append(i)          # O(1)
    return print(list_obj)          # O(1) + O(..)  - I did not find O() for print.


@time_spend
def data_to_dict(dict_obj, **kwargs):
    """
    adding all argument into dictionary
    :param kwargs: data which should be added to dict
    :param dict_obj: dictionary where all argument should be added
    :return: dictionary with added arguments
    O(n) = n
    """
    for k, v in kwargs.items():     # O(n)
        dict_obj[k] = v             # O(1)
    return print(dict_obj)          # O(1) + O(..)  - I did not find O() for print.


@time_spend
def actions_with_list(list_obj):
    # O() = n
    items_in_list = len(list_obj)                           # O(1) + O(1)
    first_item = list_obj[0]                                # O(1) + O(1)
    new_list = list(list_obj)                               # O(1) + O(n)
    return print(items_in_list, first_item, new_list)


@time_spend
def actions_with_dict(dict_obj):
    # O() = n
    items_in_dict = len(dict_obj)                           # O(1) + O(1)
    first_item = dict_obj['k1']                             # O(1) + O(1)
    new_dict = dict(dict_obj)                               # O(1) + O(n)
    return print(items_in_dict, first_item, new_dict)


@time_spend
def remove_from_list(list_obj, *args):
    # O() = n^2
    for i in args:                      # O(n)
        try:
            list_obj.remove(i)          # O(n)
        except Exception as e:
            print(e)
    print(list_obj)


@time_spend
def remove_from_dict(dict_obj, *args):
    # O() = n
    for i in args:                      # O(n)
        try:
            del dict_obj[i]             # O(1)
        except Exception as e:
            print(e)
    print(dict_obj)


list_1 = []
dict_1 = {}

print(data_to_list(list_1, 1, "string", None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(data_to_dict(dict_1, k1=1, k2="string", k3=None, k4=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k5=5))

print(actions_with_list(list_1))
print(actions_with_dict(dict_1))

print(remove_from_list(list_1, 1, "string", None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(remove_from_dict(dict_1, 'k1', "k2", 'k3', 'k4', 'k5'))

"""
Results:
1) adding new values to dictionary usually ~twice faster than adding values to lists
2) for operations to get value, len() or list()/dict() same amount of time was spent
3) deleting items from dictionary is ~1.5 faster than from list
"""
