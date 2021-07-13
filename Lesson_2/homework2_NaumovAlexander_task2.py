"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def odd_or_even(number=None, odd=0, even=0):
    """
    count quantity of odd and even numerics in a number
    :param number: number to calculate numerics
    :param odd: quantity of odd numbers
    :param even: quantity of even numbers
    :return: quantity of odd and even numbers
    """
    # using function arguments for current step
    current_number = number
    current_odd = odd
    current_even = even

    # checking that it is the first call of a function
    if current_number is None:
        # checking that number inputted correctly
        try:
            current_number = int(input('Input a number (must be integer): '))
        except Exception as e:
            print(e)
            odd_or_even()
            return

    # exit requirement
    if current_number < 10:
        if current_number % 2 == 0:
            current_even += 1
        else:
            current_odd += 1
        return print(f'quantity of odd numbers = {current_odd}\nquantity of even numbers = {current_even}')
    # step of recursion
    else:
        numeric = current_number - current_number // 10 * 10
        if numeric % 2 == 0:
            current_even += 1
        else:
            current_odd += 1
        current_number //= 10
        odd_or_even(current_number, current_odd, current_even)
        return


odd_or_even()
