# ============================================================
# Program 14: Decorators
# Concepts: basic decorator, functools.wraps, decorator with
#           args, stacking, class-based decorator, lru_cache
# ============================================================

import time
import functools

# ---- Basic decorator ---------------------------------------
def timer(func):
    """Measure and print the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [{func.__name__}] took {elapsed*1000:.3f} ms")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print("TIMER DECORATOR")
print("-" * 45)
result = slow_sum(10_000_000)
print(f"  Result: {result}")

# ---- Decorator with arguments ------------------------------
def repeat(times):
    """Repeat a function call `times` times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say(msg):
    print(f"  {msg}")

print("\nREPEAT DECORATOR")
print("-" * 45)
say("Hello from repeat!")

# ---- Stacking decorators -----------------------------------
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  → Calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"  ← {func.__name__} returned {result}")
        return result
    return wrapper

@timer
@logger
def power(base, exp):
    return base ** exp

print("\nSTACKED DECORATORS (timer + logger)")
print("-" * 45)
power(2, 10)

# ---- Class-based decorator ---------------------------------
class Retry:
    """Retry a function up to `max_attempts` times on exception."""

    def __init__(self, max_attempts=3, delay=0.0):
        self.max_attempts = max_attempts
        self.delay        = delay

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, self.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt} failed: {e}")
                    if attempt < self.max_attempts:
                        time.sleep(self.delay)
            raise RuntimeError(f"{func.__name__} failed after {self.max_attempts} attempts")
        return wrapper

counter = {"n": 0}

@Retry(max_attempts=4)
def flaky_function():
    counter["n"] += 1
    if counter["n"] < 3:
        raise ValueError(f"Not ready yet (attempt {counter['n']})")
    return f"Success on attempt {counter['n']}!"

print("\nCLASS-BASED RETRY DECORATOR")
print("-" * 45)
print(" ", flaky_function())

# ---- functools.lru_cache -----------------------------------
print("\nLRU_CACHE — Fibonacci")
print("-" * 45)

@functools.lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

print("  fib(40) =", fib(40))
info = fib.cache_info()
print(f"  cache hits={info.hits}, misses={info.misses}, size={info.currsize}")

# preserve __name__ after wrapping
print(f"\n  slow_sum.__name__  = {slow_sum.__name__}")
print(f"  slow_sum.__doc__   = {slow_sum.__doc__}")