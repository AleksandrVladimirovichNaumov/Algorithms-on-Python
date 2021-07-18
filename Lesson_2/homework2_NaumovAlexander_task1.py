"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def simple_calc(operation_status=None, first_number=None):
    """
    simple calc
    :param operation_status: keeping mathematical operation for next step of recursion if it was inputted
    :param first_number: keeping first inputted number for next step of recursion if it was inputted
    :return: result of mathematical operation
    """
    operation = operation_status  # taking previous inputted operation or None if it is a new try
    first_number_value = first_number  # taking previous inputted first number or None if it is a new try
    if operation_status is None:  # checking that operation was not inputted
        operation = input('input mathematical operation +, -, *, / or 0 to exit: ')
        if operation not in ['+', '-', '*', '/', '0']:  # checking that inputted operation is valid
            print("Incorrect value for operation. It should be '+', '-', '*', '/', '0'.")
            simple_calc()  # calling to function again to repeat input of operation
            return  # end current function
    if operation == '0':
        return print('calculations finished')
    else:
        if first_number is None:  # checking that first number was not inputted correctly before
            try:
                first_number_value = int(input('input first number (must be int): '))
            except Exception as e:
                print(e)
                simple_calc(operation_status=operation)  # keeping operation for next try to input second number
                return  # end current function
        try:
            second_number = int(input('input second number (must be int): '))
            if operation == '/' and second_number == 0:  # checking division by 0
                print('division by 0 is prohibited')
                simple_calc(operation_status=operation, first_number=first_number_value)
                return
        except Exception as e:
            print(e)
            simple_calc(operation_status=operation, first_number=first_number_value)
            return
        # performing calculations
        if operation == '+':
            print(f'{first_number_value} {operation} {second_number} = {first_number_value + second_number}')
        elif operation == '-':
            print(f'{first_number_value} {operation} {second_number} = {first_number_value - second_number}')
        elif operation == '*':
            print(f'{first_number_value} {operation} {second_number} = {first_number_value * second_number}')
        elif operation == '/':
            print(f'{first_number_value} {operation} {second_number} = {first_number_value / second_number}')
        simple_calc()


simple_calc()
