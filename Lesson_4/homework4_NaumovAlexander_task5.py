"""
Задание 5.**
Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).
Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.
Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def simple_eratosphen(number, initial_number=0, step=100, working_list=[]):
    n = initial_number + step
    for i in range(initial_number, n+1):
        working_list.append(i)
    print(working_list)
    working_list[1] = 0
    # начинаем с 3-го элемента
    i = 2
    while i <= n:
        # Если значение ячейки до этого
        # не было обнулено,
        # в этой ячейке содержится
        # простое число.
        if working_list[i] != 0:
            # первое кратное ему
            # будет в два раза больше
            j = i + i + initial_number
            while j <= n:
                # это число составное,
                # поэтому заменяем его нулем
                working_list[j] = 0
                # переходим к следующему числу,
                # которое кратно i
                # (оно на i больше)
                j = j + i
        i += 1

    result_list = [item for item in working_list if item != 0]
    print(result_list)
    if len(result_list) < number:
        simple_eratosphen(number, n, 100, working_list)
    else:
        return result_list[number-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(simple_eratosphen(i))
