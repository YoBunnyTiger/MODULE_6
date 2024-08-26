from math import sqrt, pi


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = bool(filled)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            pass

    @staticmethod
    def __is_valid_color(r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count:
            if all(isinstance(side, int) and side > 0 for side in sides):
                return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.get_sides())


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        self.__radius = circumference / 2 * pi  # Радиус через окружность
        super().__init__(color=color, sides=[circumference], filled=False)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color=color, sides=sides, filled=False)

    def get_square(self):
        p = sum(self.get_sides()) * 0.5  # Полупериметр
        s = sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=False):
        super().__init__(color=color, sides=[side] * self.sides_count, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    print()
    # Дополнительные проверки
    triangle1 = Triangle((121, 121, 121), 13, 14, 15)
    print(triangle1.get_sides())
    print(triangle1.get_square())
    triangle1.set_sides(15, 0, 15)
    print(triangle1.get_sides())
