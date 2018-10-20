# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class IsoscelesTrapezium:
    """Simple trapezium class"""

    def __init__(self, coordinates):
        self.x1 = coordinates[0][0]
        self.y1 = coordinates[0][1]
        self.x2 = coordinates[1][0]
        self.y2 = coordinates[1][1]
        self.x3 = coordinates[2][0]
        self.y3 = coordinates[2][1]
        self.x4 = coordinates[3][0]
        self.y4 = coordinates[3][1]

        self.len_a = self._get_length_side(((self.x4, self.y4), (self.x1, self.y1)))
        self.len_b = self._get_length_side(((self.x2, self.y2), (self.x1, self.y1)))
        self.len_c = self._get_length_side(((self.x3, self.y3), (self.x2, self.y2)))
        self.len_d = self._get_length_side(((self.x4, self.y4), (self.x3, self.y3)))

    def _get_length_side(self, coords):
        try:
            len = math.sqrt((coords[1][0] - coords[0][0]) ** 2 + (coords[1][1] - coords[0][1]) ** 2)
        except ValueError as ex:
            print("Ошибка! Подробнее: ", str(ex))
        else:
            return len

    def is_isosceles_trapezium(self):
        return self.len_b == self.len_d

    def get_area(self):
        height = self.get_height()
        try:
            area = height * (self.len_a + self.len_c) / 2
        except ValueError as ex:
            print("Ошибка: ", str(ex))
        else:
            return area

    def get_side(self, name):
        if name == 'a':
            return self.len_a
        elif name == 'b':
            return self.len_b
        elif name == 'c':
            return self.len_c
        elif name == 'd':
            return self.len_d
        else:
            print("Некорректно указана сторона")

    def get_perimeter(self):
        try:
            perimeter = self.len_a + self.len_b + self.len_c + self.len_d
        except ValueError as ex:
            print("Ошибка: ", str(ex))
        else:
            return perimeter

    def get_height(self):
        a = self.len_a
        b = self.len_b
        c = self.len_c
        d = self.len_d
        try:
            height = math.sqrt(c ** 2 - ((a - c) ** 2 + b ** 2 - d ** 2 / (2 * (a - c))))
        except ValueError as ex:
            print("Ошибка: ", str(ex))
        else:
            return height


if __name__ == '__main__':
    trapezium1 = IsoscelesTrapezium(((0, 0), (1, 2), (4, 2), (5, 0)))
    print("Периметр = {0}. Площадь = {1}.".format(trapezium1.get_perimeter(), trapezium1.get_area()))
    print("Является ли равнобедренной? - ", trapezium1.is_isosceles_trapezium())
