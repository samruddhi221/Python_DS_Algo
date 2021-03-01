# Hierarchical Inheritance
# create a base class "shape"
# circle, square, rectangle
class Shape:
    def __init__(self):
        pass

    def area(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float):
        self.__radius = radius
        super().__init__()

    def area(self) -> float:
        return self.__radius * self.__radius * 3.14


class Square(Shape):
    def __init__(self, side: float):
        self.__side = side
        super().__init__()

    def area(self) -> float:
        return self.__side**2


class Rectangle(Shape):
    def __init__(self, length: float, breadth: float):
        self.__length = length
        self.__breadth = breadth
        super().__init__()

    def area(self) -> float:
        return self.__length * self.__breadth


def average_shape_area(s: list) -> float:
    average_area = 0
    for shape in s:
        average_area += shape.area()
    average_area /= len(s)
    print("average area: ", average_area)
    return average_area


if __name__ == '__main__':
    c = Circle(10.)
    sq = Square(5.)
    rect = Rectangle(3., 2.)
    area_ = average_shape_area([c, sq, rect])
