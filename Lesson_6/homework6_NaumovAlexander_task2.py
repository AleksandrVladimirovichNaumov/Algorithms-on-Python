"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

# хранить элементы списка в файле построчно. Если нужно получить элемент "списка" просто считываем строку с
# нужным номером. Как результат, весь список не хранится в оперативной памяти.
from sys import getsizeof

from memory_profiler import profile

from itertools import islice


def storage_in_list(*args):
    list_obj = [i for i in args]
    return list_obj


def storage_in_file(file_name, *args):
    with open(file_name, "w") as file:
        for i in args:
            file.write(f'{i}\n')


def get_from_list(list_obj, *args):
    try:
        list_obj1 = [list_obj[i] for i in args]
    except Exception as e:
        print(e)
    return list_obj1


def get_from_file(file_name, *args):
    try:
        with open(file_name, "r") as file:
            list_obj = [islice(file, i, None) for i in args]
    except Exception as e:
        print(e)
    return list_obj


@profile()
def work_with_list():
    list_obj = storage_in_list("sdferwdf", "sdfefsdf", "sdefsdf", "sdferdf", "swefsdf")
    get_from_list(list_obj, 2, 3)


@profile()
def work_with_file():
    storage_in_file('list_file.txt', "sdferwdf", "sdfefsdf", "sdefsdf", "sdferdf", "swefsdf")
    get_from_file('list_file.txt', 2, 3)


print('********* work with list ********')
work_with_list()
print('********* work with file ********')
work_with_file()

# но как показали замеры выигрыша в памяти нет)

# хотя разница должна быть такой
print(getsizeof(storage_in_list("sdferwdf", "sdfefsdf", "sdefsdf", "sdferdf", "swefsdf")))
