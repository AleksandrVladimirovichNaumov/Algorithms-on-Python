"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
from collections import deque
from timeit import timeit

list_obj1 = []
extended_list = [1, 2, 3, 4, 5]
deque_obj1 = deque(list_obj1)


def list_append(*args):
    for i in args:
        list_obj1.append(i)


def list_append_left(*args):
    for i in args:
        list_obj1.insert(0, i)


def list_pop_left():
    list_obj1.remove(list_obj1[1])


def list_extend_left(list_obj):
    for i in list_obj:
        list_obj1.insert(0, i)


def deque_append(*args):
    for i in args:
        deque_obj1.append(i)


def deque_append_left(*args):
    for i in args:
        deque_obj1.appendleft(i)


def deque_pop_left():
    deque_obj1.popleft()


def deque_extend_left(list_obj):
    deque_obj1.extendleft(list_obj)


print('\n********* APPEND **********')

print('list_append(1, 2, 3, 4, 5):',
      timeit(
          'list_append(1, 2, 3, 4, 5)',
          setup='from __main__ import list_append',
          number=10000))

print('deque_append(1, 2, 3, 4, 5):',
      timeit(
          'deque_append(1, 2, 3, 4, 5)',
          setup='from __main__ import deque_append',
          number=10000))

print('\n********* APPEND_LEFT **********')

print('list_append_left(1, 2, 3, 4, 5):',
      timeit(
          'list_append_left(1, 2, 3, 4, 5)',
          setup='from __main__ import list_append_left',
          number=10000))

print('deque_append_left(1, 2, 3, 4, 5):',
      timeit(
          'deque_append_left(1, 2, 3, 4, 5)',
          setup='from __main__ import deque_append_left',
          number=10000))

print('\n********* POP_LEFT **********')

print('list_pop_left():',
      timeit(
          'list_pop_left()',
          setup='from __main__ import list_pop_left',
          number=10000))

print('deque_pop_left():',
      timeit(
          'deque_pop_left()',
          setup='from __main__ import deque_pop_left',
          number=10000))

print('\n********* EXTEND_LEFT **********')

print('list_extend_left():',
      timeit(
          'list_extend_left(extended_list)',
          setup='from __main__ import list_extend_left, extended_list',
          number=10000))

print('deque_extend_left():',
      timeit(
          'deque_extend_left(extended_list)',
          setup='from __main__ import deque_extend_left, extended_list',
          number=10000))

"""
Выводы
При заполнении особой разницы в скорости между list и deque нет.
Однако для добавления/удаления значений из начала списка у deque есть приемущество по скорости согласно замерам timeit.
"""