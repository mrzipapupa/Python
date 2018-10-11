import random
from functools import reduce


# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
# matrix = [[1, 0, 8],
#          [3, 4, 1],
#          [0, 4, 2]]
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]
# Суть сложности hard: Решите задачу в одну строку

def trans_matrix(matrix):
    print([list(line) for line in zip(*matrix)])


# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.


def find_max_sequence():
    len_of_number = 1000
    number = ''.join([str(random.randint(0, 9)) for i in range(len_of_number)])
    max_multiply = 0
    start_offset = 0
    end_offset = 5
    offset = 0
    while end_offset <= len_of_number:
        part_of_number = list(number[start_offset:end_offset])
        multiply_result = int(reduce(lambda x, y: int(x) * int(y), part_of_number))
        start_offset += 1
        end_offset += 1
        if multiply_result > max_multiply:
            max_multiply = multiply_result
            offset = start_offset
    print('Максимальное произведение = %s \nСоответствующее смещение = %s' % (max_multiply, offset))


# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


def queens(list_of_coordinates):
    n = 8
    x = [list_of_coordinates[i][0] for i in range(8)]
    y = [list_of_coordinates[i][1] for i in range(8)]
    is_intersection = False
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                is_intersection = True
    print("YES") if is_intersection else print("NO")


if __name__ == '__main__':
    trans_matrix([[1, 0, 8], [3, 4, 1], [0, 4, 2]])  # Вызов функции для 1-го задания
    find_max_sequence()  # Вызов функции для 2-го задания
    positions_yes = ((1, 1), (3, 3), (2, 6), (4, 6), (5, 1), (6, 3), (7, 6), (8, 4))  # Бьющиеся позиции
    positions_no = ((1, 5), (2, 1), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4))  # Не бьющиеся позиции
    queens(positions_yes)  # Вызов функции для 3-го задания
    pass
