"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def mirrored_number(initial_number=None, result_number=None):
    """
    show mirrored number
    :param initial_number: number inputted by user
    :param result_number: mirrored number
    :return: mirrored number
    """
    # using function arguments for current step
    working_number = initial_number
    number_in_progress = result_number if result_number is not None else []
    # checking that it is the first call of a function
    if working_number is None:
        try:
            working_number = int(input('Please input a number (should be integer): '))
        except Exception as e:
            print(e)
            mirrored_number()
            return
    # exit requirement
    if working_number == 0:
        return print(*number_in_progress, sep='')
    # recursion step
    else:
        number_in_progress.append(working_number % 10)
        working_number //= 10
        mirrored_number(working_number, number_in_progress)
        return


mirrored_number()
