# ============================================================
# Program 20: Type Hints & Dataclasses
# Concepts: PEP 484 hints, Optional, Union, TypeVar, Generic,
#           Protocol, dataclass (frozen, post_init, fields),
#           runtime type checking with isinstance
# ============================================================

from __future__ import annotations
from dataclasses import dataclass, field, KW_ONLY
from typing import (Optional, Union, TypeVar, Generic,
                    Protocol, runtime_checkable, ClassVar)
from enum import Enum, auto

# ---- Basic type hints in functions -------------------------
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))

print("TYPE-HINTED FUNCTIONS")
print("-" * 45)
print(f"  {greet('Alice', 3)}")
print(f"  clamp(150, 0, 100) = {clamp(150, 0, 100)}")

# ---- Optional / Union / list / dict hints ------------------
def first_or_default(items: list[int], default: Optional[int] = None) -> Optional[int]:
    return items[0] if items else default

def stringify(value: Union[int, float, str]) -> str:
    return f"value={value!r} (type={type(value).__name__})"

print(f"  first_or_default([])        = {first_or_default([])}")
print(f"  first_or_default([5, 3, 1]) = {first_or_default([5, 3, 1])}")
print(f"  stringify(3.14)             = {stringify(3.14)}")

# ---- Generic class -----------------------------------------
T = TypeVar("T")

class Stack(Generic[T]):
    """A typed stack data structure."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"

print("\nGENERIC STACK")
print("-" * 45)
s: Stack[int] = Stack()
for v in [10, 20, 30, 40]:
    s.push(v)
print(f"  Stack: {s}")
print(f"  Pop:   {s.pop()}")
print(f"  Peek:  {s.peek()}")
print(f"  Len:   {len(s)}")

# ---- Protocol (structural subtyping) -----------------------
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "○ Drawing Circle"

class Square:
    def draw(self) -> str:
        return "□ Drawing Square"

class NotDrawable:
    def render(self) -> str:
        return "Not drawable"

print("\nPROTOCOL (structural typing)")
print("-" * 45)
shapes = [Circle(), Square(), NotDrawable()]
for obj in shapes:
    if isinstance(obj, Drawable):
        print(f"  {obj.draw()}")
    else:
        print(f"  {type(obj).__name__} is not Drawable.")

# ---- Enum --------------------------------------------------
class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST  = auto()
    WEST  = auto()

    def opposite(self) -> Direction:
        opposites = {Direction.NORTH: Direction.SOUTH,
                     Direction.SOUTH: Direction.NORTH,
                     Direction.EAST:  Direction.WEST,
                     Direction.WEST:  Direction.EAST}
        return opposites[self]

print("\nENUM")
print("-" * 45)
for d in Direction:
    print(f"  {d.name:5} ({d.value}) → opposite: {d.opposite().name}")

# ---- Dataclass with all bells and whistles -----------------
@dataclass
class Employee:
    name:       str
    department: str
    _: KW_ONLY                             # everything below is keyword-only
    salary:     float = 50_000.0
    skills:     list[str] = field(default_factory=list)
    active:     bool = True
    COMPANY:    ClassVar[str] = "Acme Corp"

    def __post_init__(self):
        self.name = self.name.title()      # normalise name
        if self.salary < 0:
            raise ValueError("Salary cannot be negative.")

    def give_raise(self, pct: float) -> None:
        self.salary *= (1 + pct / 100)

print("\nDATACLASS")
print("-" * 45)
emp = Employee("alice smith", "Engineering", salary=75_000, skills=["Python", "SQL"])
print(f"  {emp}")
emp.give_raise(10)
print(f"  After 10% raise: £{emp.salary:,.2f}")
print(f"  Company: {Employee.COMPANY}")

