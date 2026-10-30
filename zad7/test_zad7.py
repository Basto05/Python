
import unittest
from itertools import islice

from iterators import iterator01, random_direction, iterator_weekdays
from rectangles import Rectangle
from points import Point


class TestIterators(unittest.TestCase):

    def test_iterator01(self):
        it = iterator01()
        self.assertEqual(
            list(islice(it, 8)),
            [0, 1, 0, 1, 0, 1, 0, 1]
        )

    def test_random_direction(self):
        it = random_direction()
        result = list(islice(it, 100))

        self.assertEqual(len(result), 100)
        for direction in result:
            self.assertIn(direction, ("N", "E", "S", "W"))

    def test_weekdays(self):
        it = iterator_weekdays()
        self.assertEqual(
            list(islice(it, 14)),
            [0, 1, 2, 3, 4, 5, 6,
             0, 1, 2, 3, 4, 5, 6]
        )


class TestRectangle(unittest.TestCase):

    def test_str_repr(self):
        r = Rectangle(0, 0, 4, 3)
        self.assertEqual(str(r), "[(0, 0), (4, 3)]")
        self.assertEqual(repr(r), "Rectangle(0, 0, 4, 3)")

    def test_comparison(self):
        self.assertEqual(
            Rectangle(0, 0, 4, 3),
            Rectangle(0, 0, 4, 3)
        )
        self.assertNotEqual(
            Rectangle(0, 0, 4, 3),
            Rectangle(0, 0, 5, 3)
        )

    def test_center_area(self):
        r = Rectangle(0, 0, 4, 6)
        self.assertEqual(r.center(), Point(2, 3))
        self.assertEqual(r.area(), 24)

    def test_move(self):
        r = Rectangle(0, 0, 4, 3)
        r.move(2, 1)
        self.assertEqual(r, Rectangle(2, 1, 6, 4))

    def test_intersection(self):
        r1 = Rectangle(0, 0, 4, 4)
        r2 = Rectangle(2, 2, 6, 6)

        self.assertEqual(
            r1.intersection(r2),
            Rectangle(2, 2, 4, 4)
        )
        self.assertIsNone(
            r1.intersection(Rectangle(5, 5, 7, 7))
        )

    def test_cover(self):
        r1 = Rectangle(0, 0, 4, 4)
        r2 = Rectangle(2, 2, 6, 6)

        self.assertEqual(
            r1.cover(r2),
            Rectangle(0, 0, 6, 6)
        )

    def test_make4(self):
        r = Rectangle(0, 0, 4, 4)

        self.assertEqual(
            r.make4(),
            (
                Rectangle(0, 0, 2, 2),
                Rectangle(2, 0, 4, 2),
                Rectangle(0, 2, 2, 4),
                Rectangle(2, 2, 4, 4)
            )
        )

    def test_invalid_rectangle(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 0, 2, 3)


if __name__ == "__main__":
    unittest.main()
