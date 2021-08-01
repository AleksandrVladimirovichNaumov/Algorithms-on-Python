"""
Задание 1.
Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import json
import sys
import timeit

import memory_profiler
from pympler import asizeof
from recordclass import recordclass

"""
Декоратор для замера времени и памяти
"""


# первый проход в цикле декоратора - замер памяти. Остальные проходы - замер времени
def time_memory(repeat):
    def decorator(func):
        def wrapper(*args):
            global mem_diff, res
            min_time = None
            i = 0
            while i < repeat:
                if i == 0:
                    m1 = memory_profiler.memory_usage()[0]
                    print(f'before function call {m1} Mib')
                    res = func(*args)
                    m2 = memory_profiler.memory_usage()[0]
                    print(f'after function call {m2} Mib')
                    mem_diff = m2-m1
                else:
                    start_time = timeit.default_timer()
                    func(*args)
                    time_func = timeit.default_timer() - start_time
                    # В качестве времени выполнения функции берется минимальное значение из всех попыток
                    if min_time is None:
                        min_time = time_func
                    else:
                        if min_time > time_func:
                            min_time = time_func
                i += 1
            print(f'{func.__name__}: {min_time}')

            return res, mem_diff

        return wrapper

    return decorator


"""
1) Ленивые вычисления
"""
# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

employees_list = ['инженер-конструктор Игорь   ', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']
employee_name = ''


# take name from a string and print message in a cycle
@time_memory(1000)
def employer_cycle(list_obj):
    list_obj1 = []
    for i in list_obj:
        i = i.rstrip()  # deleting all spaces from end of string
        i = i[i.rfind(" "):]  # deleting everything before last space
        employee_name = i.title()  # make all letter low except a first one
        list_obj1.append(f'Привет,{employee_name}!')
    return list_obj1


@time_memory(1000)
def employer_generator(list_obj):
    list_obj1 = []
    for i in list_obj:
        i = i.rstrip()  # deleting all spaces from end of string
        i = i[i.rfind(" "):]  # deleting everything before last space
        employee_name = i.title()  # make all letter low except a first one
        list_obj1.append(f'Привет,{employee_name}!')
        yield list_obj1


print('\n******* ленивые вычисления ********')
if __name__ == '__main__':
    res, mem_diff = employer_cycle(employees_list)
    print(f"Выполнение заняло {mem_diff} Mib")

if __name__ == '__main__':
    my_generator, mem_diff = employer_generator(employees_list)
    # for i in my_generator:
    #     print(i)

    print(f"Выполнение заняло {mem_diff} Mib")


# Выводы: генератор работает быстрее согласно замерам. Памяти тоже должен меньше потреблять, но почему-то после первого
# использования декоратора он перестает выдавать правильные замеры потребления помяти. Листинг 11. task 8.3py из
# методички ведет себя так же. Причину найти не смог.


"""
2) __slots__ в ООП
"""


# Реализовать базовый класс Worker (работник):
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.

class Worker:

    # attributes
    def __init__(self, n, s, p, i=None):
        if i is None:
            i = {"wage": 0, "bonus": 0}
        self.name = n
        self.surname = s
        self.position = p
        self._income = i


class Position(Worker):
    # attributes
    def __init__(self, n, s, p, i):
        super().__init__(n, s, p, i)

    # methods
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


@time_memory(100)
def create_worker():
    position_1 = Position('Sirius', 'Sam', 'Cool Guy', {'wage': 100000, 'bonus': 25000})
    return position_1


position_1 = Position('Sirius', 'Sam', 'Cool Guy', {'wage': 100000, 'bonus': 25000})


# def worker_info():
#     return f"{position_1.get_full_name()}'s total income is {position_1.get_total_income()} $ " \
#            f"at a position of a {position_1.position}."


class WorkerSlots:
    __slots__ = ['name', 'surname', 'position', '_income']

    # attributes
    def __init__(self, name, surname, position, _income=None):
        if _income is None:
            _income = {"wage": 0, "bonus": 0}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class PositionSlots(WorkerSlots):
    __slots__ = ['name', 'surname', 'position', '_income']

    # attributes
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    # methods
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


@time_memory(100)
def create_worker_slots():
    position_2 = PositionSlots('Sirius', 'Sam', 'Cool Guy', {'wage': 100000, 'bonus': 25000})
    return position_2


position_2 = PositionSlots('Sirius', 'Sam', 'Cool Guy', {'wage': 100000, 'bonus': 25000})

# def worker_info_slots():
#     return f"{position_2.get_full_name()}'s total income is {position_2.get_total_income()} $ " \
#            f"at a position of a {position_2.position}."

print('\n******* __slots__ в ООП ********')

print(f'Объём занимаемой объектом Worker памяти: {asizeof.asizeof((position_1))} байт(а)')
create_worker()
print(f'Объём занимаемой объектом WorkerSlots памяти: {asizeof.asizeof((position_2))} байт(а)')
create_worker_slots()

# Выводы: использование списка вместо словаря помогло сократить размер используемой памяти ~ в полтора раза.


"""
3) recordclass
"""

# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.

# dictionary for numbers
list_numbers = {'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}

# сохраняем в recordclass
number_records = recordclass('num_rec', ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
num_rec = number_records(one='один',
                         two='два',
                         three='три',
                         four='четыре',
                         five='пять',
                         six='шесть',
                         seven='семь',
                         eight='восемь',
                         nine='девять',
                         ten='десять'
                         )


# функция, чтобы возвращать None если нет такого значения в recordclass
def get_record(number):
    try:
        return eval(f"num_rec.{number}")
    except:
        return None


def num_translate_record(number):
    """
    num_translate(number)
    :param number:
    :return: translation of a number in Russian from dict list_numbers
    """
    print(f'>>> num_translate_record("{number}")\n"{get_record(number)}"')


def num_translate(number):
    """
    num_translate(number)
    :param number:
    :return: translation of a number in Russian from dict list_numbers
    """
    print(f'>>> num_translate("{number}")\n"{list_numbers.get(number)}"')


# разкоментировать для проверки скрипта (если надо)

# for i in list_numbers:
#     num_translate(i)
#
# for i in list_numbers:
#     num_translate_record(i)
# num_translate(1)
# num_translate_record(1)


print('\n******* recordclass ********')

print(f'Объём занимаемой объектом словаря памяти: {sys.getsizeof(list_numbers)} байт(а)')
print(f'Объём занимаемой объектом recordclass памяти: {sys.getsizeof(num_rec)} байт(а)')

# Выводы: recordclass занимает меньше места чем словарь. Однако в этой задаче пришлось писать дополнительную функцию,
# чтобы возвратить None, когда нет значения в объекте recordclass


"""
4) использование json вместо словаря на примере предыдущего скрипта
"""
print('\n******* json вместо словаря ********')
dumped_dict = json.dumps(list_numbers)
print('Размер dict: ', asizeof.asizeof(list_numbers))
print('Размер json: ', asizeof.asizeof(dumped_dict))

