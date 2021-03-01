import unittest
from inheritance import Circle, Rectangle, Square, average_shape_area

class TestInheritance(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(10.)
        self.assertEqual(c.area(), 314.0)

    def test_square_area(self):
        sq = Square(5.0)
        self.assertEqual(sq.area(), 25.)

    def test_rect_area(self):
        rect = Rectangle(7., 9.)
        self.assertEqual(rect.area(), 63.)

    def test_average_area(self):
        shapes = [Circle(10.), Square(5.), Rectangle(7., 9.)]
        self.assertEqual(average_shape_area(shapes), ((314.+25.+63.)/3.))

if __name__ == '__main__':
    unittest.main()