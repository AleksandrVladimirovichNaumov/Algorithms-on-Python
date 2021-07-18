"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Подсказка:
Правой части в рекурсии быть не должно!!! Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_check(n, element=[], n_sum=0):
    """
    function checks that 1+2+...+n = n(n+1)/2
    :param n: quantity of progressions elements
    :param element: list of elements (required only for same result appearance as in a task)
    :param n_sum: keep sum for each step of recursion
    :return: check result
    """
    # checking end of recursion
    if n == 0:
        # prints required to have same result appearance as in a task
        print(f'for n = {element[-1]}')
        print(*element, sep='+', end='')
        print(' = ', end='') if n_sum == element[-1] * (element[-1] + 1) / 2 else print(' <> ', end='')
        print(f'{element[-1]}({element[-1]}+1)/2')
        # clear list with element and sum result to use this function again
        element.clear()
        return
    else:
        # recursion step
        n_sum += n
        element.insert(0, n)
        n -= 1
        sum_check(n, element, n_sum)
        return


sum_check(10)
sum_check(5)
sum_check(100)
