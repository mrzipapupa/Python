import math


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    result_coll = [1, 1]
    for i in range(3, m + 1):
        result_coll.append(result_coll[i - 3] + result_coll[i - 2])
    print(result_coll[n - 1:])


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    print(origin_list)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, coll):
    print([element for element in coll if func(element)])


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

'''
У параллелограмма стороны попарно равны(определение)
Условимся именовать координаты слева-направо, т.е. верхние - А1, А2, нижние А3, А4
'''


def is_parallelogram(A1, A2, A3, A4):
    AB = math.sqrt(((A2[0] - A1[0]) ** 2) + (A2[1] - A1[1]) ** 2)
    CD = math.sqrt((((A4[0] - A3[0]) ** 2) + (A4[1] - A3[1]) ** 2))
    AC = math.sqrt((((A3[0] - A1[0]) ** 2) + (A3[1] - A1[1]) ** 2))
    BD = math.sqrt((((A4[0] - A2[0]) ** 2) + (A4[1] - A2[1]) ** 2))
    if AB == CD and AC == BD:
        print("Это вершины параллелограмма")
    else:
        print("Это НЕ вершины параллелограмма")


if __name__ == '__main__':
    fibonacci(4, 9)
    sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
    my_filter(lambda x: x > 0, [-4, -2, 4, 3, 5, 0, -10])
    is_parallelogram((1,3), (6,3), (0,0), (5,0))
