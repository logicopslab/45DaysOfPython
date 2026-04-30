# distributed_lock.py

import threading
import time


lock = threading.Lock()


def critical_task(task_name):
    print(f"{task_name} waiting for lock...")

    with lock:
        print(f"{task_name} acquired lock")
        time.sleep(2)  # Simulate work
        print(f"{task_name} releasing lock")


def main():
    threads = []

    for i in range(3):
        t = threading.Thread(target=critical_task, args=(f"Task-{i+1}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll tasks completed")


main()