"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


# записываем элемент как ключ в словарь. значение ключа - количество его повторений
def func_3():
    dict_obj = {}
    for i in array:
        if i not in dict_obj.keys():
            dict_obj[i] = 1
        else:
            dict_obj[i] += 1
    elem_3 = max(dict_obj, key=dict_obj.get)
    max_3 = dict_obj[elem_3]
    return f'Чаще всего встречается число {elem_3}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


# удаляем элемент из листа и преобразовываем лист в множество. если удаленный элемент вошел в множество -
# значит он повторяется. считаем сколько раз он повторяется и записываем.
def func_4():
    new_array = array.copy()
    elem_4 = 0
    max_4 = 0
    while len(new_array) > 0:
        i = new_array[-1]
        new_array.pop()
        if i in set(new_array):
            temp_max = array.count(i)
            if max_4 < temp_max:
                elem_4 = i
                max_4 = temp_max
    return f'Чаще всего встречается число {elem_4}, ' \
           f'оно появилось в массиве {max_4} раз(а)'


# улучшенный первый способ. удаляем все повторения из листа с помощью set() и оставшиеся элементы проверям на повторы.
def func_5():
    m5 = 0
    num5 = 0
    for i in set(array):
        count = array.count(i)
        if count > m5:
            m5 = count
            num5 = i
    return f'Чаще всего встречается число {num5}, ' \
           f'оно появилось в массиве {m5} раз(а)'


# получения множества неуникальных значений с помощью множественного включения и их дальнейшим подсчетом
def func_6():
    set_obj = set(array)
    non_unique_set = {i for i in array if i not in set_obj or set_obj.remove(i)}
    m6 = 0
    num6 = 0
    for i in non_unique_set:
        count = array.count(i)
        if count > m6:
            m6 = count
            num6 = i
    return f'Чаще всего встречается число {num6}, ' \
           f'оно появилось в массиве {m6} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())
print(func_6())

print(timeit.timeit("func_1()", "from __main__ import func_1"))
print(timeit.timeit("func_2()", "from __main__ import func_2"))
print(timeit.timeit("func_3()", "from __main__ import func_3"))
print(timeit.timeit("func_4()", "from __main__ import func_4"))
print(timeit.timeit("func_5()", "from __main__ import func_5"))
print(timeit.timeit("func_6()", "from __main__ import func_6"))


"""
Выводы:
наилучшим получившимся способом является улучшенный первый способ. в нем удаляются повторяющиеся значения с помощью
set. Соответсвенно количество поторяющиеся значения не будут подсчитываться снова.
Остальные способы с помощью словарей, множеств и их комбинаций выполняются дольше согласно timeit.
"""