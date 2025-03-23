The **Open/Closed Principle (OCP)** is one of the five SOLID principles of object-oriented design. It states that:

> **Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.**

This means that you should design your code in such a way that you can add new functionality without changing the existing code. This promotes flexibility, maintainability, and reduces the risk of introducing bugs when extending the system.

---

### OCP in Python

In Python, the Open/Closed Principle can be implemented using techniques like inheritance, abstract base classes, and composition. Here's how you can apply OCP in Python:

---

### Example Without OCP

Let’s say you have a class `AreaCalculator` that calculates the area of different shapes:

```python
class AreaCalculator:
    def calculate_area(self, shape):
        if shape["type"] == "rectangle":
            return shape["width"] * shape["height"]
        elif shape["type"] == "circle":
            return 3.14 * shape["radius"] ** 2
        else:
            raise ValueError("Unknown shape type")

# Usage
rectangle = {"type": "rectangle", "width": 5, "height": 10}
circle = {"type": "circle", "radius": 7}

calculator = AreaCalculator()
print(calculator.calculate_area(rectangle))  # Output: 50
print(calculator.calculate_area(circle))     # Output: 153.86
```

**Problem**: If you want to add a new shape (e.g., a triangle), you need to modify the `AreaCalculator` class. This violates the Open/Closed Principle.

---

### Example With OCP

To adhere to OCP, you can use polymorphism and abstraction. Define a base class or interface for shapes and let each shape implement its own area calculation logic.

```python
from abc import ABC, abstractmethod

# Abstract base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete implementations
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# AreaCalculator now works with any Shape
class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.area()

# Usage
rectangle = Rectangle(5, 10)
circle = Circle(7)

calculator = AreaCalculator()
print(calculator.calculate_area(rectangle))  # Output: 50
print(calculator.calculate_area(circle))     # Output: 153.86
```

**Advantages**:
1. **Open for Extension**: You can add new shapes (e.g., `Triangle`) without modifying the `AreaCalculator` class.
2. **Closed for Modification**: The `AreaCalculator` class does not need to change when new shapes are added.

---

### Adding a New Shape

To add a new shape, simply create a new class that inherits from `Shape`:

```python
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Usage
triangle = Triangle(10, 5)
print(calculator.calculate_area(triangle))  # Output: 25.0
```

---

### Key Takeaways
1. Use **abstraction** (e.g., abstract base classes or interfaces) to define a contract for behavior.
2. Use **polymorphism** to allow different implementations of the same behavior.
3. Design your classes to be **extensible** without requiring changes to existing code.

By following OCP, your code becomes more modular, easier to maintain, and less prone to bugs when extending functionality.