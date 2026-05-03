# bulkhead_system.py

import threading
import time
from queue import Queue


class WorkerPool:
    def __init__(self, name, size):
        self.name = name
        self.queue = Queue()
        self.threads = []

        for i in range(size):
            t = threading.Thread(target=self.worker, name=f"{name}-Worker-{i+1}", daemon=True)
            t.start()
            self.threads.append(t)

    def worker(self):
        while True:
            task = self.queue.get()
            if task is None:
                break

            print(f"[{threading.current_thread().name}] Processing {task}")
            time.sleep(2)

            print(f"[{threading.current_thread().name}] Completed {task}")
            self.queue.task_done()

    def submit(self, task):
        self.queue.put(task)


def main():
    # Two isolated pools
    payment_pool = WorkerPool("Payment", 2)
    email_pool = WorkerPool("Email", 2)

    # Submit tasks
    for i in range(5):
        payment_pool.submit(f"PaymentTask-{i+1}")

    for i in range(3):
        email_pool.submit(f"EmailTask-{i+1}")

    # Wait for completion
    payment_pool.queue.join()
    email_pool.queue.join()

    print("\nAll tasks processed independently")


main()
