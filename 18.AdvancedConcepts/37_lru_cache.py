# lru_cache.py

cache = {}
order = []
CAPACITY = 3


def get(key):
    if key in cache:
        # Move key to end (most recently used)
        order.remove(key)
        order.append(key)
        return cache[key]
    else:
        return "Key not found"


def put(key, value):
    if key in cache:
        order.remove(key)
    elif len(cache) >= CAPACITY:
        # Remove least recently used
        lru = order.pop(0)
        del cache[lru]
        print(f"Removed LRU key: {lru}")

    cache[key] = value
    order.append(key)


def display():
    print("\nCache State:")
    for key in order:
        print(f"{key}: {cache[key]}")


def main():
    put("A", 1)
    put("B", 2)
    put("C", 3)
    display()

    get("A")  # Access A (becomes most recent)

    put("D", 4)  # Should evict B
    display()


main()
