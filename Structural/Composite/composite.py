# Component: Base class for all shapes
class Shape:
    def draw(self):
        pass


# Leaf: Individual shape
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")


class Square(Shape):
    def draw(self):
        print("Drawing a Square")


# Composite: A collection of shapes
class CompositeShape(Shape):
    def __init__(self):
        self._shapes = []

    def add(self, shape):
        self._shapes.append(shape)

    def draw(self):
        print("Drawing a Composite Shape")
        for shape in self._shapes:
            shape.draw()


# Client code
if __name__ == "__main__":
    circle = Circle()
    square = Square()

    composite = CompositeShape()
    composite.add(circle)
    composite.add(square)

    # Draw all shapes, treating individual and composite shapes uniformly
    composite.draw()
