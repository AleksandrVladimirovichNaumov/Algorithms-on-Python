"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Массив в этом задании строить не нужно!
Нужно решить без него!
Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75
Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_of_progression(quantity=None, element=None, total=None):
    """
    function to fin sum of progression 1 -0.5 0.25 -0.125 ...
    :param quantity: quantity of elements in a progression
    :param element: element of progression
    :param total: sum of progression
    :return: sum of progression
    """
    # using function arguments for current step
    current_quantity = quantity
    current_element = element
    current_total = total
    # checking that it is the first call of a function
    if current_quantity is None:
        try:
            current_quantity = int(input('Please input a number (should be integer): '))
        except Exception as e:
            print(e)
            sum_of_progression()
            return
    # exit requirement
    if quantity == 0:
        return print(f'sum of all elementas is {current_total}')
    # recursion step
    else:
        current_quantity -= 1
        current_element = -current_element / 2 if current_element is not None else 1
        current_total = current_total + current_element if current_total is not None else 1
        sum_of_progression(current_quantity, current_element, current_total)
        return


sum_of_progression()
