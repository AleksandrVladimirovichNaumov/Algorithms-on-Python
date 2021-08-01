"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import timeit
import random


# Алгоритм из методички
def merge_sort_initial(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_initial(left)
        merge_sort_initial(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


def merge_sort_custom(lst_obj):
    # если список из одного элемента - возвращаем его и прекращаем рекурсию
    if len(lst_obj) < 2:
        return lst_obj
    result_list = list()
    center = len(lst_obj) // 2
    left = lst_obj[:center]
    right = lst_obj[center:]

    sort_left = merge_sort_custom(left)
    sort_rigth = merge_sort_custom(right)

    i, j = 0, 0

    while i < len(sort_left) and j < len(sort_rigth):
        if sort_left[i] > sort_rigth[j]:
            result_list.append(sort_rigth[j])
            j += 1
        else:
            result_list.append(sort_left[i])
            i += 1

    if j < len(sort_rigth):
        result_list += sort_rigth[j:]
    else:
        result_list += sort_left[i:]
    return result_list


# Сравнение алгоритмов сортировки
orig_list = [random.uniform(0, 50) for _ in range(10)]
# замеры 10
print("Длина списка = 10. Исходный алгоритм: ",
      timeit.timeit(
          "merge_sort_initial(orig_list[:])",
          globals=globals(),
          number=1000),
      "измененный алгоритм: ",
      timeit.timeit(
          "merge_sort_custom(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.uniform(0, 50) for _ in range(100)]

# замеры 100
print("Длина списка = 100. Исходный алгоритм: ",
      timeit.timeit(
          "merge_sort_initial(orig_list[:])",
          globals=globals(),
          number=1000),
      "измененный алгоритм: ",
      timeit.timeit(
          "merge_sort_custom(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.uniform(0, 50) for _ in range(1000)]

# замеры 1000
print("Длина списка = 1000. Исходный алгоритм: ",
      timeit.timeit(
          "merge_sort_initial(orig_list[:])",
          globals=globals(),
          number=1000),
      "измененный алгоритм: ",
      timeit.timeit(
          "merge_sort_custom(orig_list[:])",
          globals=globals(),
          number=1000))


# функция по заданию
def user_input():
    while True:
        try:
            input_length = int(input('Введите число элементов: '))
        except Exception as e:
            print(e)
        else:
            break
    random_list = [random.uniform(0, 50) for _ in range(input_length)]
    print(f'Исходный - {random_list}')
    print(f'Отсортированный - {merge_sort_custom(random_list)}')


user_input()
"""
Выводы:
В целом работают алгоритмы одинаково. Все зависит от того, насколько большой срез можно сразу добавить в конец
списка, а не добавлять поэлементно.
"""
