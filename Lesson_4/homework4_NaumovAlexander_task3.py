"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = [i for i in str(enter_num)]
    revers_num.reverse()
    result_num = int(''.join(i for i in revers_num))
    return result_num


def revers_5(enter_num):
    enter_num = str(enter_num)
    revers_num = "".join(reversed(enter_num))
    return revers_num


print(revers_1(123456789))
print(revers_2(123456789))
print(revers_3(123456789))
print(revers_4(123456789))
print(revers_5(123456789))

print(timeit.timeit("revers_1(123456789)", "from __main__ import revers_1"))
print(timeit.timeit("revers_2(123456789)", "from __main__ import revers_2"))
print(timeit.timeit("revers_3(123456789)", "from __main__ import revers_3"))
print(timeit.timeit("revers_4(123456789)", "from __main__ import revers_4"))
print(timeit.timeit("revers_5(123456789)", "from __main__ import revers_5"))

run('revers_1(123456789)')
run('revers_2(123456789)')
run('revers_3(123456789)')
run('revers_4(123456789)')
run('revers_5(123456789)')


"""
Выводы:
Наихудшем способом решения является рекурсия, так как сложность данного метода очевидно выше остальных. В целом рекурсию
приемняют обычно для получения лаконичного решения или например при получениие списка файлов и папок на диске.
Из CProfile видно что функция была вызвана 10 раз.
Вторым медленным способом являются функции 2 (через цикл while) и 4 (с помощью спискового включени + revere())
Наилучшие способы: 3(через срезы) и 5 (через reversed). 5 медленнее чем 3, потому что для получения итогового числа 
приходится использовать join()
"""