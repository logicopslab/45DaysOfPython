# ============================================================
# Program 21: Design Patterns
# Covers: Singleton, Factory, Observer, Strategy,
#         Decorator (pattern), Command, Builder
# ============================================================

from abc import ABC, abstractmethod
from typing import Callable
import copy

# =============================================
# 1. SINGLETON
# =============================================
class DatabaseConnection:
    _instance = None

    def __new__(cls, url="sqlite:///:memory:"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.url       = url
            cls._instance.connected = False
        return cls._instance

    def connect(self):
        self.connected = True
        return f"Connected to {self.url}"

print("1. SINGLETON")
db1 = DatabaseConnection("postgres://localhost/mydb")
db2 = DatabaseConnection("ignored")
print(f"   same instance? {db1 is db2}")
print(f"   url: {db2.url}")

# =============================================
# 2. FACTORY METHOD
# =============================================
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str: ...

class Dog(Animal):
    def speak(self): return "Woof!"

class Cat(Animal):
    def speak(self): return "Meow!"

class Parrot(Animal):
    def speak(self): return "Squawk!"

def animal_factory(kind: str) -> Animal:
    registry = {"dog": Dog, "cat": Cat, "parrot": Parrot}
    cls = registry.get(kind.lower())
    if cls is None:
        raise ValueError(f"Unknown animal: {kind!r}")
    return cls()

print("\n2. FACTORY METHOD")
for kind in ["dog", "cat", "parrot"]:
    a = animal_factory(kind)
    print(f"   {kind:<7} → {a.speak()}")

# =============================================
# 3. OBSERVER
# =============================================
class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, list[Callable]] = {}

    def on(self, event: str, fn: Callable):
        self._listeners.setdefault(event, []).append(fn)

    def emit(self, event: str, *args, **kwargs):
        for fn in self._listeners.get(event, []):
            fn(*args, **kwargs)

print("\n3. OBSERVER")
emitter = EventEmitter()
emitter.on("login",  lambda u: print(f"   Logger  : user '{u}' logged in"))
emitter.on("login",  lambda u: print(f"   Mailer  : welcome email sent to {u}"))
emitter.on("logout", lambda u: print(f"   Logger  : user '{u}' logged out"))
emitter.emit("login",  "alice")
emitter.emit("logout", "alice")

# =============================================
# 4. STRATEGY
# =============================================
class Sorter:
    def __init__(self, strategy: Callable):
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy(data)

print("\n4. STRATEGY")
data = [5, 1, 4, 2, 8, 3]
for name, strategy in [
    ("ascending",  lambda d: sorted(d)),
    ("descending", lambda d: sorted(d, reverse=True)),
    ("by_mod3",    lambda d: sorted(d, key=lambda x: x % 3)),
]:
    s = Sorter(strategy)
    print(f"   {name:<12}: {s.sort(data)}")

# =============================================
# 5. DECORATOR PATTERN (not Python decorator)
# =============================================
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float: ...
    @abstractmethod
    def description(self) -> str: ...

class SimpleCoffee(Coffee):
    def cost(self): return 1.00
    def description(self): return "Simple coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    def cost(self): return self._coffee.cost()
    def description(self): return self._coffee.description()

class Milk(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.25
    def description(self): return self._coffee.description() + ", milk"

class Sugar(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.10
    def description(self): return self._coffee.description() + ", sugar"

class Vanilla(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.50
    def description(self): return self._coffee.description() + ", vanilla"

print("\n5. DECORATOR PATTERN")
order = Vanilla(Milk(Sugar(SimpleCoffee())))
print(f"   {order.description()}")
print(f"   Cost: £{order.cost():.2f}")

# =============================================
# 6. COMMAND
# =============================================
class Command(ABC):
    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo(self): ...

class TextEditor:
    def __init__(self):
        self.text = ""
        self._history: list[Command] = []

    def execute(self, cmd: Command):
        cmd.execute()
        self._history.append(cmd)

    def undo(self):
        if self._history:
            self._history.pop().undo()

class TypeCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text   = text
    def execute(self):
        self.editor.text += self.text
    def undo(self):
        self.editor.text = self.editor.text[:-len(self.text)]

print("\n6. COMMAND + UNDO")
ed = TextEditor()
ed.execute(TypeCommand(ed, "Hello"))
ed.execute(TypeCommand(ed, ", World"))
ed.execute(TypeCommand(ed, "!"))
print(f"   Text: {ed.text!r}")
ed.undo()
print(f"   After undo: {ed.text!r}")
ed.undo()
print(f"   After undo: {ed.text!r}")