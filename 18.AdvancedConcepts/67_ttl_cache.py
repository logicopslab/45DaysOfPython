# ttl_cache.py

import time
import threading


class TTLCache:
    def __init__(self):
        self.store = {}
        self.lock = threading.Lock()

        # Start cleanup thread
        t = threading.Thread(target=self.cleanup, daemon=True)
        t.start()

    def set(self, key, value, ttl):
        expiry = time.time() + ttl
        with self.lock:
            self.store[key] = (value, expiry)

    def get(self, key):
        with self.lock:
            if key in self.store:
                value, expiry = self.store[key]
                if time.time() < expiry:
                    return value
                else:
                    del self.store[key]
        return None

    def cleanup(self):
        while True:
            time.sleep(2)
            now = time.time()
            with self.lock:
                expired = [k for k, (_, exp) in self.store.items() if exp < now]
                for k in expired:
                    del self.store[k]
                    print(f"[Cleanup] Removed expired key: {k}")


def main():
    cache = TTLCache()

    cache.set("a", 100, 3)
    print("Value:", cache.get("a"))

    time.sleep(5)
    print("After expiry:", cache.get("a"))


main()