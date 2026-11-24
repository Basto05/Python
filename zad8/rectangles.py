from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Nieprawidłowe wierzchołki prostokąta")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        point1, point2 = points
        return cls(point1.x, point1.y, point2.x, point2.y)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return (
            f"Rectangle({self.pt1.x}, {self.pt1.y}, "
            f"{self.pt2.x}, {self.pt2.y})"
        )

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def top(self):
        return self.pt2.y

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    def center(self):
        return Point(
            (self.left + self.right) / 2,
            (self.bottom + self.top) / 2
        )

    def area(self):
        return self.width * self.height

    def move(self, x, y):
        self.pt1 = Point(self.left + x, self.bottom + y)
        self.pt2 = Point(self.right + x, self.top + y)

    def intersection(self, other):
        x1 = max(self.left, other.left)
        y1 = max(self.bottom, other.bottom)
        x2 = min(self.right, other.right)
        y2 = min(self.top, other.top)

        if x1 >= x2 or y1 >= y2:
            return None

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.left, other.left)
        y1 = min(self.bottom, other.bottom)
        x2 = max(self.right, other.right)
        y2 = max(self.top, other.top)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        mx = (self.left + self.right) / 2
        my = (self.bottom + self.top) / 2

        return (
            Rectangle(self.left, self.bottom, mx, my),
            Rectangle(mx, self.bottom, self.right, my),
            Rectangle(self.left, my, mx, self.top),
            Rectangle(mx, my, self.right, self.top)
        )
