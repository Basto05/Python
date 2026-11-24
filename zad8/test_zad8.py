
import pytest
from points import Point
from rectangles import Rectangle


def test_from_points():
    p1 = Point(1, 2)
    p2 = Point(5, 7)

    rectangle = Rectangle.from_points([p1, p2])

    assert rectangle.left == 1
    assert rectangle.bottom == 2
    assert rectangle.right == 5
    assert rectangle.top == 7


def test_dimensions():
    rectangle = Rectangle(1, 2, 5, 7)

    assert rectangle.width == 4
    assert rectangle.height == 5


def test_corners():
    rectangle = Rectangle(1, 2, 5, 7)

    assert rectangle.topleft == Point(1, 7)
    assert rectangle.bottomleft == Point(1, 2)
    assert rectangle.topright == Point(5, 7)
    assert rectangle.bottomright == Point(5, 2)


def test_area():
    rectangle = Rectangle(1, 2, 5, 7)

    assert rectangle.area() == 20


def test_center():
    rectangle = Rectangle(1, 2, 5, 7)

    assert rectangle.center() == Point(3, 4.5)


def test_move():
    rectangle = Rectangle(1, 2, 5, 7)
    rectangle.move(2, 3)

    assert rectangle.left == 3
    assert rectangle.bottom == 5
    assert rectangle.right == 7
    assert rectangle.top == 10


def test_intersection():
    first = Rectangle(1, 1, 5, 5)
    second = Rectangle(3, 3, 7, 7)

    result = first.intersection(second)

    assert result == Rectangle(3, 3, 5, 5)


def test_no_intersection():
    first = Rectangle(1, 1, 2, 2)
    second = Rectangle(3, 3, 4, 4)

    assert first.intersection(second) is None


def test_invalid_rectangle():
    with pytest.raises(ValueError):
        Rectangle(5, 5, 1, 1)


def test_properties_are_read_only():
    rectangle = Rectangle(1, 2, 5, 7)

    with pytest.raises(AttributeError):
        rectangle.width = 10

    with pytest.raises(AttributeError):
        rectangle.topleft = Point(0, 0)
