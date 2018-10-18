# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    """Simple triange class"""

    def __init__(self, coordinates):
        self.x1 = coordinates[0][0]
        self.y1 = coordinates[0][1]
        self.x2 = coordinates[1][0]
        self.y2 = coordinates[1][1]
        self.x3 = coordinates[2][0]
        self.y3 = coordinates[2][1]

        self.len_a = self._get_length_side(((self.x3, self.y3), (self.x1, self.y1)))
        self.len_b = self._get_length_side(((self.x2, self.y2), (self.x1, self.y1)))
        self.len_c = self._get_length_side(((self.x3, self.y3), (self.x2, self.y2)))

    def _get_length_side(self, coords):
        try:
            len = math.sqrt((coords[1][0] - coords[0][0])**2 + (coords[1][1] - coords[0][1])**2)
        except Exception as ex:
            print("Ошибка! Подробнее: ", str(ex))
        else:
            return len

    def get_area(self):
        try:
            area = self.len_a * self.get_height()/2
        except ValueError as ex:
            print("Ошибка: ", str(ex))
        else:
            return area

    def get_height(self):
        p = self.get_perimeter()
        try:
            height = (2/self.len_a) * math.sqrt(p*(p-self.len_a)*(p-self.len_b)*(p-self.len_c))
        except ValueError as ex:
            print("Ошибка: ", str(ex))
        else:
            return height

    def get_perimeter(self):
        try:
            perimeter = self.len_a + self.len_b + self.len_c
        except ValueError as ex:
            print("Ошибка: ", str(ex))
        else:
            return perimeter

if __name__ == '__main__':
    triangle1 = Triangle(((0, 0), (3, 3), (4, 0)))
    print("Высота = {0}. Периметр = {1}. Площадь = {2}.".format(triangle1.get_height(), triangle1.get_perimeter(),
                                                                triangle1.get_area()))
