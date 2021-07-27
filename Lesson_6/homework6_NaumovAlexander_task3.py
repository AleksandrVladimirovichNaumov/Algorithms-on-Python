"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
import timeit
import memory_profiler


# первый проход в цикле декоратора - замер памяти. Остальные проходы - замер времени
def time_memory(repeat):
    def decorator(func):
        def wrapper(*args):
            min_time = None
            i = 0
            while i < repeat:
                if i == 0:
                    m1 = memory_profiler.memory_usage()[0]
                    print(f'before function call {m1} Mib')
                    res = func(*args)
                    m2 = memory_profiler.memory_usage()[0]
                    print(f'after function call {m2} Mib')
                    mem_diff = m2 - m1
                    print(f'memory used {mem_diff} Mib')
                else:
                    start_time = timeit.default_timer()
                    func(*args)
                    time_func = timeit.default_timer() - start_time
                    # В качестве времени выполнения функции берется минимальное значение из всех попыток
                    if min_time is None:
                        min_time = time_func
                    else:
                        if min_time > time_func:
                            min_time = time_func
                i += 1
            print(f'time spent for {func.__name__}: {min_time}')

            return res

        return wrapper

    return decorator


def get_factorial(number):
    if number == 2:
        return 2
    return number * get_factorial(number - 1)


# функция, вызывающая рекурсивную функцию, чтобы декоратор сработал только раз
@time_memory(1000)
def factorial_func(number):
    return get_factorial(number)


print(f'\nfactorial is {factorial_func(4)}')
