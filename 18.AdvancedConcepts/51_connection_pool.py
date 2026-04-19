# connection_pool.py

import threading
import time


class ConnectionPool:
    def __init__(self, size):
        self.size = size
        self.available = [f"Conn-{i+1}" for i in range(size)]
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def acquire(self):
        with self.condition:
            while not self.available:
                print(f"[{threading.current_thread().name}] Waiting for connection...")
                self.condition.wait()

            conn = self.available.pop()
            print(f"[{threading.current_thread().name}] Acquired {conn}")
            return conn

    def release(self, conn):
        with self.condition:
            self.available.append(conn)
            print(f"[{threading.current_thread().name}] Released {conn}")
            self.condition.notify()


def worker(pool, work_time):
    conn = pool.acquire()
    time.sleep(work_time)  # Simulate work
    pool.release(conn)


def main():
    pool = ConnectionPool(size=2)

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(pool, 2), name=f"Worker-{i+1}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll work completed")


main()
