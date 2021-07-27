"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
__mul__
__add__
Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
1. вариант
defaultdict(list)
int(, 16)
reduce
2. вариант
class HexNumber:
    __add__
    __mul__
hx = HexNumber
hx + hx
hex()
"""
from collections import defaultdict
from collections import deque

default_dict_obj = defaultdict()


def input_number():
    empty_set = set()
    number_16 = set('0123456789ABCDEF')
    while True:
        number = input('Введите число из шестнадцатеричной системы счисления: ')
        if set(number.upper()) - number_16 != empty_set:
            print("Некорректно введене число.")
        else:
            return list(number.upper())


def sum_16():
    default_dict_obj['number1'] = input_number()
    default_dict_obj['number2'] = input_number()
    # так как дальше будем удалять первый элемент из списка, то лучше использовать deque
    sum_16 = deque(hex(
        int(''.join(default_dict_obj.get('number1')), 16) + int(''.join(default_dict_obj.get('number2')), 16)).upper())
    while True:
        if sum_16[0] != 'X':
            sum_16.popleft()
        else:
            sum_16.popleft()
            return list(sum_16)  # без list выводиться как deque([...])


def mul_16():
    default_dict_obj['number1'] = input_number()
    default_dict_obj['number2'] = input_number()
    # так как дальше будем удалять первый элемент из списка, то лучше использовать deque
    mul_16 = deque(hex(
        int(''.join(default_dict_obj.get('number1')), 16) * int(''.join(default_dict_obj.get('number2')), 16)).upper())
    while True:
        if mul_16[0] != 'X':
            mul_16.popleft()
        else:
            mul_16.popleft()
            return list(mul_16)  # без list выводиться как deque([...])


print(sum_16())
print(mul_16())

"""
Решение с помощью ООП
"""


class HexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        summ_16 = deque(hex(int(self.number, 16) + int(other.number, 16)).upper())
        while True:
            if summ_16[0] != 'X':
                summ_16.popleft()
            else:
                summ_16.popleft()
                return list(summ_16)  # без list выводиться как deque([...])

    def __mul__(self, other):
        mul_16 = deque(hex(int(self.number, 16) * int(other.number, 16)).upper())
        while True:
            if mul_16[0] != 'X':
                mul_16.popleft()
            else:
                mul_16.popleft()
                return list(mul_16)  # без list выводиться как deque([...])


print('******** Решение с помощью ООП ***********')
number_1 = HexNumber(''.join(input_number()))
number_2 = HexNumber(''.join(input_number()))
print(number_1 + number_2)
print(number_1 * number_2)
