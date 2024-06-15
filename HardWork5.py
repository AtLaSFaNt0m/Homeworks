class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.filled = False
        self.__color = list(color)
        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Нельзя сменить цвет на ({}, {}, {})".format(r, g, b))

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            print(f"Нельзя сменить стороны на {sides}")

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def __len__(self):
        return sum(self.__sides)

    def get_sides(self):
        return self.__sides

import math

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__radius = self.__calculate_radius()

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        s = len(self) / 2
        a, b, c = self.get_sides()
        return (2 / a) * (math.sqrt(s * (s - a) * (s - b) * (s - c)))

    def get_square(self):
        a = self.get_sides()[0]
        return 0.5 * a * self.__height

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__height = self.__calculate_height()

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1] * self.sides_count
        else:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

    def set_sides(self, *sides):
        if len(sides) == 1:
            super().set_sides(*([sides[0]] * self.sides_count))
        else:
            print(f"Нельзя сменить стороны на {sides}")

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
