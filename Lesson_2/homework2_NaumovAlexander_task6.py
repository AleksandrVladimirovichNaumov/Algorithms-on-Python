"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Подсказка:
Базовый случай здесь - угадали число или закончились попытки
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random


def find_a_number(count=10, number=None):
    """
    a game to guess a number between 0 and 100
    :param count: number of a try
    :param number: number to guess
    :return: win or loose in a game
    """
    # take a random number if it was not taken before
    if number is None:
        number = random.randint(0, 100)
    # checking that integer was inputed
    try:
        answer = int(input(f'Try {11 - count}: input a number between 0 and 100 (must be int): '))
    except Exception as e:
        print(e)
        find_a_number(count, number)
        return
    # checking that answer is between 0 and 100
    if answer < 0 or 100 < answer:
        print('number should be between 0 and 100')
        find_a_number(count, number)
        return
    # is answer a correct number?
    if answer == number:
        return print('You win')
    # checking quantity of tries
    if count == 1:
        return print('You loose')
    # telling is answer bigger or smaller thank target number
    print(f'Target number is smaller than {answer}') if answer > number else print(
        f'Target number is bigger than {answer}')
    count -= 1
    find_a_number(count, number)


find_a_number()
