# ============================================================
# Program 12: Inheritance & Polymorphism
# Concepts: single/multi inheritance, super(), abstract base
#           classes, method overriding, MRO, isinstance/issubclass
# ============================================================

from abc import ABC, abstractmethod
import math

# ---- Abstract base class -----------------------------------
class Shape(ABC):
    """Abstract base class for 2-D geometric shapes."""

    color: str = "white"

    def __init__(self, color: str = "white"):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...

    def describe(self) -> str:
        return (f"{type(self).__name__}("
                f"color={self.color}, "
                f"area={self.area():.2f}, "
                f"perimeter={self.perimeter():.2f})")

    def __repr__(self):
        return self.describe()

# ---- Concrete subclasses -----------------------------------
class Circle(Shape):
    def __init__(self, radius: float, color="white"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float, color="white"):
        super().__init__(color)
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float, color="white"):
        super().__init__(color)
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = self.perimeter() / 2           # Heron's formula
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# ---- Square inherits Rectangle -----------------------------
class Square(Rectangle):
    def __init__(self, side: float, color="white"):
        super().__init__(side, side, color)
        self.side = side

    def describe(self):
        return (f"Square(side={self.side}, color={self.color}, "
                f"area={self.area():.2f})")

# ---- Polymorphism demo -------------------------------------
shapes = [
    Circle(5, "red"),
    Rectangle(4, 6, "blue"),
    Triangle(3, 4, 5, "green"),
    Square(7, "yellow"),
]

print("SHAPE DESCRIPTIONS (Polymorphism)")
print("=" * 55)
for shape in shapes:
    print(" ", shape.describe())

print("\nSORTED BY AREA (largest first)")
print("-" * 55)
for shape in sorted(shapes, key=lambda s: s.area(), reverse=True):
    print(f"  {type(shape).__name__:<12} area={shape.area():.2f}")

# ---- Multiple inheritance ----------------------------------
print("\nMULTIPLE INHERITANCE")
print("-" * 55)

class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} is swimming!"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

donald = Duck()
print(" ", donald.fly())
print(" ", donald.swim())
print(" ", donald.quack())

# ---- MRO ---------------------------------------------------
print("\nMETHOD RESOLUTION ORDER (MRO)")
print("  Duck MRO:", [cls.__name__ for cls in Duck.__mro__])

# ---- isinstance / issubclass --------------------------------
print("\nISINSTANCE / ISSUBCLASS")
sq = Square(4)
print(f"  Square instance of Shape?     {isinstance(sq, Shape)}")
print(f"  Square instance of Rectangle? {isinstance(sq, Rectangle)}")
print(f"  Square subclass of Shape?     {issubclass(Square, Shape)}")