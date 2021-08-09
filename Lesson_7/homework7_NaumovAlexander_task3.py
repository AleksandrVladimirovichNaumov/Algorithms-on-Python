"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.
[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]
my_lst
new_lts
arr[m]
from statistics import median
[3, 4, 3, 3, 5, 3, 3]
left = []
right = []
left == right and
for i in
    for
    left == right
    left.clear()
    right.clear()
"""
import random
import statistics


def find_median():
    while True:
        try:
            m = int(input('Введите m для определения длины массива по формуле 2m + 1: '))
        except Exception as e:
            print(e)
        else:
            break
    list_obj = [random.randint(0, 100) for i in range(2 * m + 1)]
    print(f'список: {list_obj}')
    print(f'медиана найдена с помощью сортировки Шелла: {sorted_median(list_obj[:], m)}')
    print(f'медиана найдена с помощью цикла: {cycle_median(list_obj[:])}')
    print(f'медиана найдена с помощью встроенной функции statistics.median(): {statistics.median(list_obj[:])}')


def sorted_median(list_obj, m):
    step = len(list_obj) // 2
    while step > 0:
        for i in range(step, len(list_obj)):
            delta = i - step
            while delta >= 0 and list_obj[delta] > list_obj[i]:
                list_obj[delta], list_obj[i] = list_obj[i], list_obj[delta]
                i = delta
                delta -= step
        step //= 2
    return list_obj[m]


def cycle_median(list_obj):
    for i in range(len(list_obj) // 2):
        list_obj.remove(max(list_obj))
    return max(list_obj)


find_median()
