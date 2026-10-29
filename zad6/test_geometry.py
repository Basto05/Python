import unittest

from points import Point
from rectangles import Rectangle


class TestPoint(unittest.TestCase):

    def test_str_repr(self):
        p = Point(2, 3)
        self.assertEqual(str(p), "(2, 3)")
        self.assertEqual(repr(p), "Point(2, 3)")

    def test_comparison(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertNotEqual(Point(1, 2), Point(2, 1))

    def test_add_sub(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))
        self.assertEqual(Point(5, 7) - Point(2, 3), Point(3, 4))

    def test_multiply(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)

    def test_hash(self):
        self.assertEqual(len({Point(1, 2), Point(1, 2)}), 1)


class TestRectangle(unittest.TestCase):

    def test_str_repr(self):
        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(str(r), "[(0, 0), (4, 3)]")
        self.assertEqual(repr(r), "Rectangle(0, 0, 4, 3)")

    def test_comparison(self):
        self.assertEqual(Rectangle(0, 0, 4, 3), Rectangle(0, 0, 4, 3))
        self.assertNotEqual(Rectangle(0, 0, 4, 3), Rectangle(0, 0, 5, 3))

    def test_center(self):
        self.assertEqual(Rectangle(0, 0, 4, 6).center(), Point(2, 3))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 3).area(), 12)
        self.assertEqual(Rectangle(1, 1, 2, 2).area(), 1)

    def test_move(self):
        r = Rectangle(0, 0, 4, 3)
        r.move(2, 1)
        self.assertEqual(r, Rectangle(2, 1, 6, 4))


if __name__ == "__main__":
    unittest.main()
