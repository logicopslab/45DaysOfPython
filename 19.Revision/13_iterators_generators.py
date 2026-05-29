# ============================================================
# Program 13: Iterators & Generators
# Concepts: __iter__/__next__, StopIteration, generator
#           functions, yield, send(), yield from, itertools
# ============================================================

import itertools

# ---- Custom Iterator class ---------------------------------
class FibonacciIter:
    """Iterator that yields Fibonacci numbers up to n terms."""

    def __init__(self, n):
        self.n   = n
        self.a   = 0
        self.b   = 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= self.n:
            raise StopIteration
        value    = self.a
        self.a, self.b = self.b, self.a + self.b
        self.idx += 1
        return value

print("CUSTOM ITERATOR — Fibonacci(15)")
print("-" * 40)
fib_seq = list(FibonacciIter(15))
print(" ", fib_seq)

# ---- Generator function ------------------------------------
def fibonacci_gen(n):
    """Generator version — much simpler!"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nGENERATOR FUNCTION — same sequence")
print("-" * 40)
print(" ", list(fibonacci_gen(15)))

# ---- Infinite generator with islice ------------------------
def naturals(start=1):
    """Infinite generator of natural numbers."""
    n = start
    while True:
        yield n
        n += 1

print("\nINFINITE GENERATOR (first 10 squares via map)")
print("-" * 40)
squares = map(lambda x: x**2, naturals())
print(" ", list(itertools.islice(squares, 10)))

# ---- Generator expression ----------------------------------
print("\nGENERATOR EXPRESSION")
print("-" * 40)
gen_expr = (x**2 for x in range(1, 11) if x % 2 == 0)
print("  Even squares:", list(gen_expr))

# ---- send() — coroutine-style generator --------------------
def running_average():
    """Coroutine: receives values via send(), yields the running avg."""
    total, count = 0, 0
    while True:
        value = yield (total / count if count else None)
        total += value
        count += 1

print("\nCOROUTINE — Running average")
print("-" * 40)
avg = running_average()
next(avg)                           # prime the generator
for v in [10, 20, 30, 15, 25]:
    result = avg.send(v)
    print(f"  Sent {v:>4} → running avg = {result:.2f}")

# ---- yield from (delegating generator) ----------------------
def chain_generators(*iterables):
    """Flatten multiple iterables using yield from."""
    for it in iterables:
        yield from it

print("\nYIELD FROM — chaining generators")
print("-" * 40)
result = list(chain_generators([1, 2], (3, 4), fibonacci_gen(5)))
print(" ", result)

# ---- itertools showcase ------------------------------------
print("\nITERTOOLS")
print("-" * 40)

# combinations & permutations
letters = ["A", "B", "C"]
print("  Combinations(3,2)  :", list(itertools.combinations(letters, 2)))
print("  Permutations(3,2)  :", list(itertools.permutations(letters, 2)))

# groupby
data = [("fruit","apple"),("fruit","banana"),("veg","carrot"),("veg","dill")]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    items = [x[1] for x in group]
    print(f"  groupby '{key}'      : {items}")

# accumulate
nums = [1, 2, 3, 4, 5]
print("  accumulate(sum)    :", list(itertools.accumulate(nums)))
print("  accumulate(product):", list(itertools.accumulate(nums, lambda a,b: a*b)))