"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import random
from timeit import timeit


def bubble_sort(list_obj, check_flag):
    list_length = len(list_obj)
    n = 1
    done_flag = True
    while n < list_length:
        for i in range(list_length - n):
            if list_obj[i] < list_obj[i + 1]:
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
                done_flag = False
        if check_flag and done_flag:
            return list_obj, n
        done_flag = True
        n += 1
    return list_obj, n


# функция без благов(чистая) для достоверности замеров
def bubble_sort_clear(list_obj):
    list_length = len(list_obj)
    n = 1
    while n < list_length:
        for i in range(list_length - n):
            if list_obj[i] < list_obj[i + 1]:
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
        n += 1
    return list_obj, n


random_list = [random.randint(-100, 100) for i in range(10)]
print(random_list)
print(bubble_sort(random_list[:], False))
print(bubble_sort(random_list[:], True))
print(bubble_sort_clear(random_list[:]))

print(f"Сортировка при флаге = False и длине списка {len(random_list)}: "
      f"{timeit('bubble_sort(random_list[:], False)', globals=globals(), number=1000)}")
print(f"Сортировка при флаге = True и длине списка {len(random_list)}: "
      f"{timeit('bubble_sort(random_list[:], True)', globals=globals(), number=1000)}")
print(f"Сортировка 'чистой' функцией при длине списка {len(random_list)}: "
      f"{timeit('bubble_sort_clear(random_list[:])', globals=globals(), number=1000)}")

random_list = [random.randint(-100, 100) for i in range(50)]
print(f"Сортировка при флаге = False и длине списка {len(random_list)}: "
      f"{timeit('bubble_sort(random_list[:], False)', globals=globals(), number=1000)}")
print(f"Сортировка при флаге = True и длине списка {len(random_list)}: "
      f"{timeit('bubble_sort(random_list[:], True)', globals=globals(), number=1000)}")
print(f"Сортировка 'чистой' функцией при длине списка {len(random_list)}: "
      f"{timeit('bubble_sort_clear(random_list[:])', globals=globals(), number=1000)}")

random_list = [random.randint(-100, 100) for i in range(100)]
print(f"Сортировка при флаге = False и длине списка {len(random_list)}: "
      f"{timeit('bubble_sort(random_list[:], False)', globals=globals(), number=1000)}")
print(f"Сортировка при флаге = True и длине списка {len(random_list)}: "
      f"{timeit('bubble_sort(random_list[:], True)', globals=globals(), number=1000)}")
print(f"Сортировка 'чистой' функцией при длине списка {len(random_list)}: "
      f"{timeit('bubble_sort_clear(random_list[:])', globals=globals(), number=1000)}")

"""
Выводы:
1) Сравнивая работу функции bubble_sort() с в ключеным и выключеным флагом - быстрее работает с включеным флагом при
любой длинне списка, так как затрачивается время на проверку if и присвоению флага true/false значений.
2) сравнивая работу функции с флагом и чистой функции - большее влияние идет от длины списка. определенной тенденции нет
замеры всегда показывают приемущество разных подходов.
если увеличить количество повторов замеров - занимет много времени. на замеры будет влиять нагрузка на компьютер.
мысли следующие:
1) при малой длинне списка вероятность ранней сортировки больше, но в тоже время время на проход меньше,
а дополнительные операции для флага делать надо и на это время уходит
2) при длинном списке вероятность ранней сортировки меньше, но экономия времени за проходы больше.

В целом я считаю, что для мелких списков флаг не нужен. время и так мизерное и выигрыш особо не будет заметен.
Для длинных списков, где время на один проход гораздо больше времени, затраченного на работу со флагом - да, 
стоит использовать, с учетом, что функция используется часто. Хотя последние проходы, на которых получается ранняя
сортировка, по времени особо не затратны (так как n растет с каждым проходом)
"""
