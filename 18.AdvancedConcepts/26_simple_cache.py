# simple_cache.py

import time

cache = {}


def set_cache(key, value, ttl):
    expiry = time.time() + ttl
    cache[key] = (value, expiry)
    print(f"Key '{key}' stored with TTL {ttl} seconds")


def get_cache(key):
    if key in cache:
        value, expiry = cache[key]

        if time.time() < expiry:
            return value
        else:
            print("Key expired")
            del cache[key]
            return None
    else:
        print("Key not found")
        return None


def view_cache():
    print("\nCurrent Cache:")
    for key, (value, expiry) in cache.items():
        print(f"{key}: {value} (expires in {int(expiry - time.time())}s)")


def main():
    while True:
        print("\n1. Set Cache")
        print("2. Get Cache")
        print("3. View Cache")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            ttl = int(input("Enter TTL (seconds): "))
            set_cache(key, value, ttl)

        elif choice == "2":
            key = input("Enter key: ")
            result = get_cache(key)
            if result:
                print("Value:", result)

        elif choice == "3":
            view_cache()

        elif choice == "4":
            break

        else:
            print("Invalid choice")


main()
