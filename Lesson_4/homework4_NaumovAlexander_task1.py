"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
import timeit


# декоратор для замера времени. в качестве аргумента quantity задается количесво раз повторения функции
def time_it(quantity):
    def decorator(func):
        def wrapper(list_obj):
            min_time = None
            i = 0
            while i < quantity:
                start_time = timeit.default_timer()
                func(list_obj)
                time_func = timeit.default_timer() - start_time
                # В качестве времени выполнения функции берется минимальное значение из всех попыток
                if min_time is None:
                    min_time = time_func
                else:
                    if min_time > time_func:
                        min_time = time_func
                i += 1
            print(f'{func.__name__}: {min_time}')
        return wrapper
    return decorator


@time_it(10000)
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@time_it(10000)
def func_2(nums):
    new_arr = [i for v, i in enumerate(nums) if v % 2 == 0]
    return new_arr


@time_it(10000)
def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


list_obj_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4,
              5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func_1(list_obj_1)
func_2(list_obj_1)
func_3(list_obj_1)


"""
Результаты:
Наихудший результат показывает func_1. в отличее от спискового включения, перед запуском цикло необходимо создать пустой
список. Так же для добавления элемента используется функция append().
Из двух функций, использующих списковое включение, наилучший результат показывает func_2. в ней используется встроенная
функция enumerate(), которая возвращает значение и индекс элемента списка в виде кортежа. видимо встроенные функции и
работа с кортежем оказывается быстрее.
"""
