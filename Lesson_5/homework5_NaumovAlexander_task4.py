"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

dict_obj1 = dict()
ordered_dict_obj1 = OrderedDict()


def dict_add(*args):
    for i, k in enumerate(args):
        dict_obj1[k] = i


def dict_get_value(dict_obj):
    for i in list(dict_obj):
        dict_obj.get(i)


def ordered_dict_add(*args):
    for i, k in enumerate(args):
        ordered_dict_obj1[k] = i


def ordered_dict_get_value(ordered_dict_obj):
    for i in list(ordered_dict_obj):
        ordered_dict_obj1.get(i)


print("******** adding ********")

print('dict_add(): ',
      timeit(
          'dict_add(1, 2, 3, 4, 5, 6, 7, 8, 9)',
          setup='from __main__ import dict_add',
          number=10000
      ))

print('ordered_dict_add(): ',
      timeit(
          'ordered_dict_add(1, 2, 3, 4, 5, 6, 7, 8, 9)',
          setup='from __main__ import ordered_dict_add',
          number=10000
      ))

print("******** get values ********")

print('dict_get_value(): ',
      timeit(
          'dict_get_value(dict_obj1)',
          setup='from __main__ import dict_get_value, dict_obj1',
          number=10000
      ))

print('ordered_dict_get_value(): ',
      timeit(
          'ordered_dict_get_value(ordered_dict_obj1)',
          setup='from __main__ import ordered_dict_get_value, ordered_dict_obj1',
          number=10000
      ))

"""
Выводы:
Замеры показали, заполнение обычных словарей и получение из них значений происходит быстрее чем с orderedDict, хоть и не
на много. Так как я использую версию питона 3.9, то большого смысла в orderedDict нет, так как Python и в обычных
словарях запоминает порядок.
"""