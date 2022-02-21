"""Модуль тестирования методов модуля shapes.py"""

import unittest
from .. import shapes


class ShapeTest(unittest.TestCase):
    """Тесты для модуля shapes.py"""

    def setUp(self) -> None:
        """Set up for test"""
        print(f'Set up for {self.shortDescription()}')

    def tearDown(self) -> None:
        """Tear down for test"""
        print(f'Tear down for {self.shortDescription()}')

    def test_perimeter_square(self):
        """Тест расчета периметра квадрата."""
        obj = shapes.Square(3)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 12.0)

    def test_perimeter_cube(self):
        """Тест расчета периметра куба."""
        obj = shapes.Cube(3)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 36.0)

    def test_perimeter_rectangle(self):
        """Тест расчета периметра прямоугольника."""
        obj = shapes.Rectangle(3, 5)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 16.0)

    def test_perimeter_box(self):
        """Тест расчета периметра параллелепипеда."""
        obj = shapes.Box(3, 5, 10)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 56.0)

    def test_perimeter_circle(self):
        """Тест расчета периметра круга."""
        obj = shapes.Circle(3)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 18.85)

    def test_perimeter_ball(self):
        """Тест расчета периметра шара."""
        obj = shapes.Ball(3)
        self.assertEqual(obj.calculate(shapes.Perimeter()), None)

    def test_perimeter_cylinder(self):
        """Тест расчета периметра цилиндра."""
        obj = shapes.Cylinder(3, 10)
        self.assertEqual(obj.calculate(shapes.Perimeter()), None)

    def test_perimeter_cone(self):
        """Тест расчета периметра конуса."""
        obj = shapes.Cone(3, 10)
        self.assertEqual(obj.calculate(shapes.Perimeter()), None)

    def test_perimeter_pyramid(self):
        """Тест расчета периметра пирамиды."""
        obj = shapes.Pyramid(6, 5, 10)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 97.08)

    def test_perimeter_rhombus(self):
        """Тест расчета периметра ромба."""
        obj = shapes.Rhombus(5, 10)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 22.36)

    def test_perimeter_triangle(self):
        """Тест расчета периметра треугольника."""
        obj = shapes.Triangle(3, 4, 5)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 12.0)

    def test_perimeter_triangle_0(self):
        """Тест расчета периметра треугольника с нулевым параметром."""
        obj = shapes.Triangle(0, 2, 4)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 'ERROR')

    def test_perimeter_triangle_bad(self):
        """Тест расчета периметра плохого треугольника."""
        obj = shapes.Triangle(1, 2, 4)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 'ERROR')

    def test_perimeter_trapeze(self):
        """Тест расчета периметра трапеции."""
        obj = shapes.Trapeze(8, 5, 3, 4)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 20.0)

    def test_perimeter_trapeze_0(self):
        """Тест расчета периметра трапеции с нулевым параметром."""
        obj = shapes.Trapeze(2, 3, 1, 0)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 'ERROR')

    def test_perimeter_trapeze_bad(self):
        """Тест расчета периметра плохой трапеции."""
        obj = shapes.Trapeze(2, 3, 1, 10)
        self.assertEqual(obj.calculate(shapes.Perimeter()), 'ERROR')


    def test_area_square(self):
        """Тест расчета площади квадрата."""
        obj = shapes.Square(3)
        self.assertEqual(obj.calculate(shapes.Area()), 9.0)

    def test_area_square_0(self):
        """Тест расчета площади квадрата с 0."""
        obj = shapes.Square(0)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_cube(self):
        """Тест расчета площади куба."""
        obj = shapes.Cube(3)
        self.assertEqual(obj.calculate(shapes.Area()), 54.0)

    def test_area_cube_0(self):
        """Тест расчета площади куба с 0."""
        obj = shapes.Cube(0)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_rectangle(self):
        """Тест расчета площади прямоугольника."""
        obj = shapes.Rectangle(3, 5)
        self.assertEqual(obj.calculate(shapes.Area()), 15.0)

    def test_area_rectangle_0(self):
        """Тест расчета площади прямоугольника с 0."""
        obj = shapes.Rectangle(3, 0)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_box(self):
        """Тест расчета площади параллелепипеда."""
        obj = shapes.Box(3, 5, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 190.0)

    def test_area_box_0(self):
        """Тест расчета площади параллелепипеда с 0."""
        obj = shapes.Box(3, 0, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_circle(self):
        """Тест расчета площади круга."""
        obj = shapes.Circle(3)
        self.assertEqual(obj.calculate(shapes.Area()), 28.27)

    def test_area_circle_0(self):
        """Тест расчета площади круга с 0."""
        obj = shapes.Circle(0)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_ball(self):
        """Тест расчета площади шара."""
        obj = shapes.Ball(3)
        self.assertEqual(obj.calculate(shapes.Area()), 113.1)

    def test_area_ball_0(self):
        """Тест расчета площади шара с 0."""
        obj = shapes.Ball(0)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_cylinder(self):
        """Тест расчета площади цилиндра."""
        obj = shapes.Cylinder(3, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 245.04)

    def test_area_cylinder_0(self):
        """Тест расчета площади цилиндра с 0."""
        obj = shapes.Cylinder(0, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_cone(self):
        """Тест расчета площади конуса."""
        obj = shapes.Cone(3, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 126.67)

    def test_area_cone_0(self):
        """Тест расчета площади конуса с 0."""
        obj = shapes.Cone(0, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_pyramid(self):
        """Тест расчета площади пирамиды."""
        obj = shapes.Pyramid(6, 5, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 228.41)

    def test_area_pyramid_0(self):
        """Тест расчета площади пирамиды с 0."""
        obj = shapes.Pyramid(6, 0, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_rhombus(self):
        """Тест расчета площади ромба."""
        obj = shapes.Rhombus(5, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 25.0)

    def test_area_rhombus_0(self):
        """Тест расчета площади ромба с 0."""
        obj = shapes.Rhombus(0, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_triangle(self):
        """Тест расчета площади треугольника."""
        obj = shapes.Triangle(3, 4, 5)
        self.assertEqual(obj.calculate(shapes.Area()), 6.0)

    def test_area_triangle_0(self):
        """Тест расчета площади треугольника с нулевым параметром."""
        obj = shapes.Triangle(0, 2, 4)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_triangle_bad(self):
        """Тест расчета площади плохого треугольника."""
        obj = shapes.Triangle(1, 2, 4)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_trapeze(self):
        """Тест расчета площади трапеции."""
        obj = shapes.Trapeze(8, 5, 3, 4)
        self.assertEqual(obj.calculate(shapes.Area()), 19.38)

    def test_area_trapeze_0(self):
        """Тест расчета площади трапеции с нулевым параметром."""
        obj = shapes.Trapeze(2, 3, 1, 0)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')

    def test_area_trapeze_bad(self):
        """Тест расчета площади плохой трапеции."""
        obj = shapes.Trapeze(2, 3, 1, 10)
        self.assertEqual(obj.calculate(shapes.Area()), 'ERROR')


    def test_volume_square(self):
        """Тест расчета объема квадрата."""
        obj = shapes.Square(3)
        self.assertEqual(obj.calculate(shapes.Volume()), None)

    def test_volume_cube(self):
        """Тест расчета объема куба."""
        obj = shapes.Cube(3)
        self.assertEqual(obj.calculate(shapes.Volume()), 27.0)

    def test_volume_rectangle(self):
        """Тест расчета объема прямоугольника."""
        obj = shapes.Rectangle(3, 5)
        self.assertEqual(obj.calculate(shapes.Volume()), None)

    def test_volume_box(self):
        """Тест расчета объема параллелепипеда."""
        obj = shapes.Box(3, 5, 10)
        self.assertEqual(obj.calculate(shapes.Volume()), 150.0)

    def test_volume_circle(self):
        """Тест расчета объема круга."""
        obj = shapes.Circle(3)
        self.assertEqual(obj.calculate(shapes.Volume()), None)

    def test_volume_ball(self):
        """Тест расчета объема шара."""
        obj = shapes.Ball(3)
        self.assertEqual(obj.calculate(shapes.Volume()), 113.1)

    def test_volume_cylinder(self):
        """Тест расчета объема цилиндра."""
        obj = shapes.Cylinder(3, 10)
        self.assertEqual(obj.calculate(shapes.Volume()), 282.74)

    def test_volume_cone(self):
        """Тест расчета объема конуса."""
        obj = shapes.Cone(3, 10)
        self.assertEqual(obj.calculate(shapes.Volume()), 94.25)

    def test_volume_pyramid(self):
        """Тест расчета объема пирамиды."""
        obj = shapes.Pyramid(6, 5, 10)
        self.assertEqual(obj.calculate(shapes.Volume()), 216.51)

    def test_volume_rhombus(self):
        """Тест расчета объема ромба."""
        obj = shapes.Rhombus(5, 10)
        self.assertEqual(obj.calculate(shapes.Volume()), None)

    def test_volume_triangle(self):
        """Тест расчета объема треугольника."""
        obj = shapes.Triangle(3, 4, 5)
        self.assertEqual(obj.calculate(shapes.Volume()), None)

    def test_volume_trapeze(self):
        """Тест расчета объема трапеции."""
        obj = shapes.Trapeze(8, 5, 3, 4)
        self.assertEqual(obj.calculate(shapes.Volume()), None)


    def test_apothem_square(self):
        """Тест расчета апофемы квадрата."""
        obj = shapes.Square(3)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_cube(self):
        """Тест расчета апофемы куба."""
        obj = shapes.Cube(3)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_rectangle(self):
        """Тест расчета апофемы прямоугольника."""
        obj = shapes.Rectangle(3, 5)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_box(self):
        """Тест расчета апофемы параллелепипеда."""
        obj = shapes.Box(3, 5, 10)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_circle(self):
        """Тест расчета апофемы круга."""
        obj = shapes.Circle(3)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_ball(self):
        """Тест расчета апофемы шара."""
        obj = shapes.Ball(3)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_cylinder(self):
        """Тест расчета апофемы цилиндра."""
        obj = shapes.Cylinder(3, 10)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_cone(self):
        """Тест расчета апофемы конуса."""
        obj = shapes.Cone(3, 10)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_pyramid(self):
        """Тест расчета апофемы пирамиды."""
        obj = shapes.Pyramid(6, 5, 10)
        self.assertEqual(obj.calculate(shapes.Apothem()), 10.9)

    def test_apothem_rhombus(self):
        """Тест расчета апофемы ромба."""
        obj = shapes.Rhombus(5, 10)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_triangle(self):
        """Тест расчета апофемы треугольника."""
        obj = shapes.Triangle(3, 4, 5)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)

    def test_apothem_trapeze(self):
        """Тест расчета апофемы трапеции."""
        obj = shapes.Trapeze(8, 5, 3, 4)
        self.assertEqual(obj.calculate(shapes.Apothem()), None)


    def test_check_possibility_square(self):
        """Тест проверки параметров квадрата."""
        obj = shapes.Square(0)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_square_true(self):
        """Тест проверки параметров квадрата."""
        obj = shapes.Square(3)
        self.assertEqual(obj.check_possibility(), True)

    def test_check_possibility_cube(self):
        """Тест проверки параметров куба."""
        obj = shapes.Cube(0)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_rectangle(self):
        """Тест проверки параметров прямоугольника."""
        obj = shapes.Rectangle(0, 5)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_box(self):
        """Тест проверки параметров параллелепипеда."""
        obj = shapes.Box(0, 5, 10)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_circle(self):
        """Тест проверки параметров круга."""
        obj = shapes.Circle(0)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_ball(self):
        """Тест проверки параметров шара."""
        obj = shapes.Ball(0)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_cylinder(self):
        """Тест проверки параметров цилиндра."""
        obj = shapes.Cylinder(0, 10)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_cone(self):
        """Тест проверки параметров конуса."""
        obj = shapes.Cone(0, 10)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_pyramid(self):
        """Тест проверки параметров пирамиды."""
        obj = shapes.Pyramid(0, 5, 10)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_rhombus(self):
        """Тест проверки параметров ромба."""
        obj = shapes.Rhombus(0, 10)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_triangle(self):
        """Тест проверки параметров треугольника."""
        obj = shapes.Triangle(0, 4, 5)
        self.assertEqual(obj.check_possibility(), False)

    def test_check_possibility_trapeze(self):
        """Тест проверки параметров трапеции."""
        obj = shapes.Trapeze(0, 5, 3, 4)
        self.assertEqual(obj.check_possibility(), False)

    def test_string_enter(self):
        """Тест преобразования дескриптором в 0 некорректного ввода."""
        obj = shapes.Trapeze('w', 5, 3, 4)
        self.assertEqual(obj.lower_base, 0)


if __name__ == '__main__':
    unittest.main()
