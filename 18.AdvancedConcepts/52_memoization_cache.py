# memoization_cache.py

cache = {}


def memoize(func):
    def wrapper(n):
        if n in cache:
            print(f"[CACHE HIT] Returning cached result for {n}")
            return cache[n]

        print(f"[CACHE MISS] Computing result for {n}")
        result = func(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    num = int(input("Enter a number: "))

    print("\nCalculating Fibonacci...\n")
    result = fibonacci(num)

    print(f"\nFibonacci({num}) = {result}")


main()
