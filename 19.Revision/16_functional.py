# ============================================================
# Program 16: Functional Programming
# Concepts: map, filter, reduce, partial, compose, currying,
#           immutability, namedtuple, dataclass, pure functions
# ============================================================

from functools import reduce, partial
from collections import namedtuple
from dataclasses import dataclass, field
from typing import Callable, TypeVar

T = TypeVar("T")

# ---- map / filter / reduce ---------------------------------
nums = list(range(1, 11))
print("NUMBERS:", nums)

doubled   = list(map(lambda x: x * 2, nums))
evens     = list(filter(lambda x: x % 2 == 0, nums))
total     = reduce(lambda acc, x: acc + x, nums)
product   = reduce(lambda acc, x: acc * x, nums)

print(f"  map(×2)    : {doubled}")
print(f"  filter(even): {evens}")
print(f"  reduce(sum) : {total}")
print(f"  reduce(prod): {product}")

# ---- Composing functions -----------------------------------
def compose(*funcs):
    """Right-to-left function composition: compose(f, g)(x) = f(g(x))."""
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

def compose_left(*funcs):
    """Left-to-right pipeline."""
    return reduce(lambda f, g: lambda x: g(f(x)), funcs)

square   = lambda x: x ** 2
add_one  = lambda x: x + 1
to_str   = lambda x: f"result={x}"

transform = compose_left(add_one, square, to_str)
print("\nFUNCTION COMPOSITION (pipeline: add_one → square → str)")
print(f"  transform(4) = {transform(4)}")   # (4+1)² = 25

# ---- Partial application -----------------------------------
print("\nPARTIAL APPLICATION")
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)
print(f"  square(7)  = {square(7)}")
print(f"  cube(4)    = {cube(4)}")

# Log with preset prefix
import functools
def log(level, message):
    print(f"  [{level.upper()}] {message}")

info  = partial(log, "info")
error = partial(log, "error")
info("Server started.")
error("Disk full.")

# ---- Currying ----------------------------------------------
print("\nCURRYING")
def curry(func):
    """Simple curry for 2-argument functions."""
    return lambda a: lambda b: func(a, b)

@curry
def add(a, b):
    return a + b

add5 = add(5)
print(f"  add5(3)  = {add5(3)}")
print(f"  add5(10) = {add5(10)}")
print(f"  list of add5: {list(map(add5, range(5)))}")

# ---- Immutable data with namedtuple ------------------------
print("\nNAMEDTUPLE (immutable)")
Point = namedtuple("Point", ["x", "y"])
p1 = Point(3, 4)
p2 = Point(6, 8)
distance = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2) ** 0.5
print(f"  {p1} → {p2}, distance = {distance:.2f}")
p3 = p1._replace(x=10)       # creates a new namedtuple
print(f"  After _replace: {p3}")

# ---- dataclass (Python 3.7+) -------------------------------
print("\nDATACLASS")

@dataclass(frozen=True)          # frozen = immutable
class Vector:
    x: float
    y: float
    z: float = 0.0

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1 + v2
print(f"  v1 = {v1}, |v1| = {v1.magnitude():.3f}")
print(f"  v2 = {v2}, |v2| = {v2.magnitude():.3f}")
print(f"  v1 + v2 = {v3}, |v3| = {v3.magnitude():.3f}")