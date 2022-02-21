"""Модуль классов геометрических фигур. Импортируется функционал стандартной библиотеки math."""

from math import pi, sqrt, tan, sin
import numpy as np
import matplotlib.pyplot as plt


class Draw:
    """Класс-отрисовщик."""

    def draw_square(self, square) -> None:
        """Отрисовывает в отдельном окне изображение квадрата."""
        fig = plt.figure(figsize=(4, 4), facecolor='#eee')
        ax = fig.add_subplot()
        fig.suptitle('Square')
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        pr = plt.Polygon(([0, 0], [0, 4], [4, 4], [4, 0]), facecolor='skyblue')
        ax.add_patch(pr)
        plt.axis('off')
        plt.show()

    def draw_cube(self, cube) -> None:
        pass

    def draw_rectangle(self, rectangle) -> None:
        """Отрисовывает в отдельном окне изображение прямоугольника."""
        fig = plt.figure(figsize=(4, 4), facecolor='#eee')
        ax = fig.add_subplot()
        fig.suptitle('Rectangle')
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        pr = plt.Polygon(([0, 0], [0, 2.5], [4, 2.5], [4, 0]), facecolor='skyblue')
        ax.add_patch(pr)
        plt.axis('off')
        plt.show()

    def draw_box(self, box) -> None:
        pass

    def draw_circle(self, circle) -> None:
        """Отрисовывает в отдельном окне изображение круга."""
        fig = plt.figure(figsize=(4, 4), facecolor='#eee')
        ax = fig.add_subplot()
        fig.suptitle('Circle')
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        cr = plt.Circle((0, 0), 2, facecolor='skyblue', fill=True)
        ax.add_patch(cr)
        plt.axis('off')
        plt.show()

    def draw_ball(self, ball) -> None:
        """Отрисовывает в отдельном окне изображение шара."""
        fig = plt.figure(figsize=(4, 4), facecolor='#eee')
        ax_3d = fig.add_subplot(projection='3d')
        r = 2
        p = np.arange(0, 2 * np.pi, 0.1)
        t = np.arange(0, 2 * np.pi, 0.1)
        phi, theta = np.meshgrid(p, t)
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
        ax_3d.plot_surface(x, y, z, facecolor='skyblue')
        plt.axis('off')
        plt.show()

    def draw_cylinder(self, cylinder) -> None:
        """Отрисовывает в отдельном окне изображение цилиндра."""
        fig = plt.figure(figsize=(4, 4))
        ax_3d = fig.add_subplot(projection='3d')
        fig.suptitle('Cylinder')
        u = np.linspace(0, 2 * np.pi, 50)
        h = np.linspace(0, 1, 25)
        x = np.outer(np.sin(u), np.ones(len(h)))
        y = np.outer(np.cos(u), np.ones(len(h)))
        z = np.outer(np.ones(len(u)), h)
        ax_3d.plot_surface(x, y, z, color='skyblue')
        plt.axis('off')
        plt.show()

    def draw_cone(self, cone) -> None:
        pass

    def draw_pyramid(self, pyramid) -> float:
        result = sqrt(pyramid.height ** 2 + (pyramid.length / (2 * tan(pi / pyramid.quantity))) ** 2)
        return round(result, 2)

    def draw_trapeze(self, trapeze) -> None:
        """Отрисовывает в отдельном окне изображение трапеции."""
        fig = plt.figure(figsize=(4, 4), facecolor='#eee')
        ax = fig.add_subplot()
        fig.suptitle('Trapeze')
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        pr = plt.Polygon(([0, 0], [1, 3], [3, 3], [4, 0]), facecolor='skyblue')
        ax.add_patch(pr)
        plt.axis('off')
        plt.show()

    def draw_rhombus(self, rhombus) -> None:
        """Отрисовывает в отдельном окне изображение ромба."""
        fig = plt.figure(figsize=(4, 4), facecolor='#eee')
        ax = fig.add_subplot()
        fig.suptitle('Rhombus')
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        pr = plt.Polygon(([0, 1], [2, 2], [4, 1], [2, 0]), facecolor='skyblue')
        ax.add_patch(pr)
        plt.axis('off')
        plt.show()

    def draw_triangle(self, triangle) -> None:
        """Отрисовывает в отдельном окне изображение треугольника."""
        fig = plt.figure(figsize=(4, 4), facecolor='#eee')
        ax = fig.add_subplot()
        fig.suptitle('Triangle')
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        pr = plt.Polygon(([0, 0], [1.5, 3], [4, 0]), facecolor='skyblue')
        ax.add_patch(pr)
        plt.axis('off')
        plt.show()


class Param:
    """Класс-дескриптор для присвоения и вызова значений свойств классов."""

    def __set_name__(self, owner, name):
        """Позволяет получить имя атрибута, связанного с дескриптором."""
        self.__name = name

    def __get__(self, instance, owner):
        """Возвращает значение, хранящееся в экземпляре instance."""
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        """
        Сохраняет значение value в экземпляре класса instance.

        В случае некорректного значения заменяет его на ноль,
        чтобы не вызывать ошибку, а в дальнейшем обработать ноль как ошибку.
        """
        if self.__check_params(value):
            instance.__dict__[self.__name] = float(value)
        else:
            instance.__dict__[self.__name] = 0.0

    def __check_params(self, value):
        """Проверяет, чтобы присваиваемые значения были числами."""
        return type(value) in (int, float)


class Shape(Param):
    """Родительский класс для всех классов модуля. Определяет общую структуру и функционал."""

    title = 'Shape'

    def __init__(self):
        """Инициализирует экземпляр класса при его создании."""

    def check_possibility(self):
        """Проверяет возможность существования экземпляра класса в зависимости от его параметров."""

    def calculate(self, visitor):
        """Возвращает значение параметра, вычисляемое соответствующим Visitor."""
        if self.check_possibility():
            return getattr(visitor, f'calculate_{self.title.lower()}')(self)
        return 'ERROR'

    def draw(self, visitor=Draw()):
        """Отрисовывает модель экземпляра класса."""
        return getattr(visitor, f'draw_{self.title.lower()}')(self)


class Square(Shape):
    """Класс-наследник класса Shape. Определяет функционал квадрата."""

    title = 'Square'
    names = ('Length',)
    length = Param()

    def __init__(self, length=0) -> None:
        """Наследуется от родителя. Дополняется одним параметром."""
        super().__init__()
        self.length = length

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования квадрата.
        """
        return self.length != 0


class Cube(Square):
    """
    Класс-наследник класса Square.
    Определяет функционал куба. При инициализации так же получает один параметр.
    """

    title = 'Cube'


class Rectangle(Square):
    """
    Класс-наследник класса Square.
    Определяет функционал прямоугольника. При инициализации получает один дополнительный параметр.
    """

    title = 'Rectangle'
    names = ('Length', 'Width')
    width = Param()

    def __init__(self, length=0, width=0) -> None:
        """Наследуется от родителя. Дополняется одним параметром."""
        super().__init__(length)
        self.width = width

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования прямоугольника.
        """
        return self.length != 0 and self.width != 0


class Box(Rectangle):
    """
    Класс-наследник класса Rectangle. Определяет функционал параллелепипеда.
    При инициализации получает один дополнительный параметр.
    """

    title = 'Box'
    names = ('Length', 'Width', 'Height')
    height = Param()

    def __init__(self, length=0, width=0, height=0) -> None:
        """Наследуется от родителя. Дополняется одним параметром."""
        super().__init__(length, width)
        self.height = height

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования параллелепипеда.
        """
        return self.length != 0 and self.width != 0 and self.height != 0


class Circle(Shape):
    """Класс-наследник класса Shape. Определяет функционал круга."""

    title = 'Circle'
    names = ('Radius',)
    radius = Param()

    def __init__(self, radius=0) -> None:
        """Наследуется от родителя. Дополняется одним параметром."""
        super().__init__()
        self.radius = radius

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования круга.
        """
        return self.radius != 0


class Ball(Circle):
    """Класс-наследник класса Circle. При инициализации получает те же параметры. Определяет функционал шара."""

    title = 'Ball'


class Cylinder(Circle):
    """Класс-наследник класса Circle. Определяет функционал цилиндра."""

    title = 'Cylinder'
    names = ('Radius', 'Height')
    height = Param()

    def __init__(self, radius=0, height=0) -> None:
        """Наследуется от родителя. Дополняется при инициализации одним параметром."""
        super().__init__(radius)
        self.height = height

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования цилиндра.
        """
        return self.radius != 0 and self.height != 0


class Cone(Cylinder):
    """Класс-наследник класса Cylinder. Имеет те же параметры. Определяет функционал конуса."""

    title = 'Cone'


class Pyramid(Shape):
    """Класс-наследник базового класса Shape. Определяет функционал правильной пирамиды."""

    title = 'Pyramid'
    names = ('Quantity', 'Length', 'Height')
    quantity = Param()
    length = Param()
    height = Param()

    def __init__(self, quantity=0, length=0, height=0) -> None:
        """Наследуется от родителя. Дополняется при инициализации тремя параметрами."""
        super().__init__()
        self.quantity = quantity
        self.length = length
        self.height = height

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования пирамиды.
        """
        return self.quantity != 0 and self.length != 0 and self.height != 0


class Trapeze(Shape):
    """Класс-наследник базового класса Shape. Определяет функционал трапеции."""

    title = 'Trapeze'
    names = ('Lower Base', 'Upper Base', 'Side 1', 'Side 2')
    lower_base = Param()
    upper_base = Param()
    side1 = Param()
    side2 = Param()

    def __init__(self, lower_base=0, upper_base=0, side1=0, side2=0) -> None:
        """Наследуется от родителя. Дополняется при инициализации четырьмя параметрами."""
        super().__init__()
        self.lower_base = lower_base
        self.upper_base = upper_base
        self.side1 = side1
        self.side2 = side2

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования трапеции.
        """
        check_list = [self.lower_base, self.upper_base, self.side1, self.side2]
        max_side = max(check_list)
        check_list.remove(max_side)
        return (max_side < sum(check_list)) and (self.lower_base != self.upper_base) and \
               self.lower_base != 0 and self.upper_base != 0 and self.side1 != 0 and self.side2 != 0


class Rhombus(Shape):
    """Класс-наследник базового класса Shape. Определяет функционал ромба."""

    title = 'Rhombus'
    names = ('Diagonal 1', 'Diagonal 1')
    diagonal1 = Param()
    diagonal2 = Param()

    def __init__(self, diagonal1=0, diagonal2=0) -> None:
        """Наследуется от родителя. Дополняется при инициализации двумя параметрами."""
        super().__init__()
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования ромба.
        """
        return self.diagonal1 != 0 and self.diagonal2 != 0


class Triangle(Shape):
    """Класс-наследник базового класса Shape. Определяет функционал треугольника."""

    title = 'Triangle'
    names = ('Side a', 'Side b', 'Side c')
    side1 = Param()
    side2 = Param()
    side3 = Param()

    def __init__(self, side1=0, side2=0, side3=0) -> None:
        """Наследуется от родителя. Дополняется при инициализации тремя параметрами."""
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def check_possibility(self) -> bool:
        """
        Переопределяет родительский метод.

        Проверяет, что исходные данные удовлетворяют факту существования трапеции.
        """
        check_list = [self.side1, self.side2, self.side3]
        max_side = max(check_list)
        check_list.remove(max_side)
        return max_side < sum(check_list) and self.side1 != 0 and self.side2 != 0 and self.side3 != 0


class Perimeter:
    """Класс-визитер, содержащий методы расчета периметра."""

    def calculate_square(self, square) -> float:
        """Возвращает периметр квадрата."""
        result = square.length * 4
        return round(result, 2)

    def calculate_cube(self, cube) -> float:
        """Возвращает периметр куба."""
        result = cube.length * 12
        return round(result, 2)

    def calculate_rectangle(self, rectangle) -> float:
        """Возвращает периметр прямоугольника."""
        result = (rectangle.length + rectangle.width) * 2
        return round(result, 2)

    def calculate_box(self, box) -> float:
        """Возвращает периметр параллелепипеда."""
        result = (box.length + box.width) * 2 + box.height * 4
        return round(result, 2)

    def calculate_circle(self, circle) -> float:
        """Возвращает периметр круга (длину окружности)."""
        result = 2 * pi * circle.radius
        return round(result, 2)

    def calculate_ball(self, ball) -> None:
        """Метод не определен для шара."""
        return None

    def calculate_cylinder(self, cylinder) -> None:
        """Метод не определен для цилиндра."""
        return None

    def calculate_cone(self, cone) -> None:
        """Метод не определен для конуса."""
        return None

    def calculate_pyramid(self, pyramid) -> float:
        """Возвращает периметр пирамиды."""
        result = pyramid.quantity * sqrt(
            pyramid.height ** 2 + (
                        pyramid.length / (2 * sin(pi / pyramid.quantity))) ** 2) + pyramid.length * pyramid.quantity
        return round(result, 2)

    def calculate_trapeze(self, trapeze) -> float:
        """Возвращает периметр трапеции."""
        result = trapeze.lower_base + trapeze.upper_base + trapeze.side1 + trapeze.side2
        return round(result, 2)

    def calculate_rhombus(self, rhombus) -> float:
        """Возвращает периметр ромба."""
        result = sqrt((rhombus.diagonal1 / 2) ** 2 + (rhombus.diagonal2 / 2) ** 2) * 4
        return round(result, 2)

    def calculate_triangle(self, triangle) -> float:
        """Возвращает периметр треугольника."""
        result = triangle.side1 + triangle.side2 + triangle.side3
        return round(result, 2)


class Area:
    """Класс-визитер, содержащий методы расчета площади."""
    def calculate_square(self, square) -> float:
        """Возвращает площадь квадрата."""
        result = square.length * square.length
        return round(result, 2)

    def calculate_cube(self, cube) -> float:
        """Возвращает площадь куба."""
        result = cube.length * cube.length * 6
        return round(result, 2)

    def calculate_rectangle(self, rectangle) -> float:
        """Возвращает площадь прямоугольника."""
        result = rectangle.length * rectangle.width
        return round(result, 2)

    def calculate_box(self, box) -> float:
        """Возвращает площадь параллелепипеда."""
        result = (box.length * box.width + box.height * box.length + box.height * box.width) * 2
        return round(result, 2)

    def calculate_circle(self, circle) -> float:
        """Возвращает площадь круга."""
        result = pi * circle.radius ** 2
        return round(result, 2)

    def calculate_ball(self, ball) -> float:
        """Возвращает площадь шара."""
        result = 4 * pi * ball.radius ** 2
        return round(result, 2)

    def calculate_cylinder(self, cylinder) -> float:
        """Возвращает площадь цилиндра."""
        result = 2 * pi * cylinder.radius * (cylinder.height + cylinder.radius)
        return round(result, 2)

    def calculate_cone(self, cone) -> float:
        """Возвращает площадь конуса."""
        result = pi * cone.radius * (cone.radius + sqrt(cone.radius ** 2 + cone.height ** 2))
        return round(result, 2)

    def calculate_pyramid(self, pyramid) -> float:
        """Возвращает площадь пирамиды."""
        result = (pyramid.quantity * pyramid.length / 2) * \
                 (pyramid.length / (2 * tan(pi / pyramid.quantity)) +
                  sqrt(pyramid.height ** 2 + (pyramid.length / (2 * tan(pi / pyramid.quantity))) ** 2))
        return round(result, 2)

    def calculate_trapeze(self, trapeze) -> float:
        """Возвращает площадь трапеции."""
        p = (trapeze.lower_base + trapeze.upper_base + trapeze.side1 + trapeze.side2) / 2
        result = (trapeze.lower_base + trapeze.upper_base) / abs(trapeze.lower_base - trapeze.upper_base) * sqrt(
            (p - trapeze.lower_base) * (p - trapeze.upper_base) * (p - trapeze.lower_base - trapeze.side1) * (
                    p - trapeze.lower_base - trapeze.side2))
        return round(result, 2)

    def calculate_rhombus(self, rhombus) -> float:
        """Возвращает площадь ромба."""
        result = rhombus.diagonal1 * rhombus.diagonal2 / 2
        return round(result, 2)

    def calculate_triangle(self, triangle) -> float:
        """Возвращает площадь треугольника."""
        p = (triangle.side1 + triangle.side2 + triangle.side3) / 2
        result = sqrt(p * (p - triangle.side1) * (p - triangle.side2) * (p - triangle.side3))
        return round(result, 2)


class Volume:
    """Класс-визитер, содержащий методы расчета объема."""
    def calculate_square(self, square) -> None:
        """Метод не определен для квадрата."""
        return None

    def calculate_cube(self, cube) -> float:
        """Возвращает объем куба."""
        result = cube.length ** 3
        return round(result, 2)

    def calculate_rectangle(self, rectangle) -> None:
        """Метод не определен для прямоугольника."""
        return None

    def calculate_box(self, box) -> float:
        """Возвращает объем параллелепипеда."""
        result = box.length * box.width * box.height
        return round(result, 2)

    def calculate_circle(self, circle) -> None:
        """Метод не определен для круга."""
        return None

    def calculate_ball(self, ball) -> float:
        """Возвращает объем шара."""
        result = pi * ball.radius ** 3 * 4 / 3
        return round(result, 2)

    def calculate_cylinder(self, cylinder) -> float:
        """Возвращает объем цилиндра."""
        result = cylinder.height * pi * cylinder.radius ** 2
        return round(result, 2)

    def calculate_cone(self, cone) -> float:
        """Возвращает объем конуса."""
        result = (cone.height * pi * cone.radius ** 2) / 3
        return round(result, 2)

    def calculate_pyramid(self, pyramid) -> float:
        """Возвращает объем пирамиды."""
        result = pyramid.height * pyramid.quantity * pyramid.length ** 2 / (12 * tan(pi / pyramid.quantity))
        return round(result, 2)

    def calculate_trapeze(self, trapeze) -> None:
        """Метод не определен для трапеции."""
        return None

    def calculate_rhombus(self, rhombus) -> None:
        """Метод не определен для ромба."""
        return None

    def calculate_triangle(self, triangle) -> None:
        """Метод не определен для треугольника."""
        return None


class Apothem:
    """Класс-визитер, содержащий методы расчета апофемы."""
    def calculate_square(self, square) -> None:
        """Метод не определен для квадрата."""
        return None

    def calculate_cube(self, cube) -> None:
        """Метод не определен для куба."""
        return None

    def calculate_rectangle(self, rectangle) -> None:
        """Метод не определен для прямоугольника."""
        return None

    def calculate_box(self, box) -> None:
        """Метод не определен для параллелепипеда."""
        return None

    def calculate_circle(self, circle) -> None:
        """Метод не определен для круга."""
        return None

    def calculate_ball(self, ball) -> None:
        """Метод не определен для шара."""
        return None

    def calculate_cylinder(self, cylinder) -> None:
        """Метод не определен для цилиндра."""
        return None

    def calculate_cone(self, cone) -> None:
        """Метод не определен для конуса."""
        return None

    def calculate_pyramid(self, pyramid) -> float:
        """Возвращает апофему пирамиды."""
        result = sqrt(pyramid.height ** 2 + (pyramid.length / (2 * tan(pi / pyramid.quantity))) ** 2)
        return round(result, 2)

    def calculate_trapeze(self, trapeze) -> None:
        """Метод не определен для трапеции."""
        return None

    def calculate_rhombus(self, rhombus) -> None:
        """Метод не определен для ромба."""
        return None

    def calculate_triangle(self, triangle) -> None:
        """Метод не определен для треугольника."""
        return None
