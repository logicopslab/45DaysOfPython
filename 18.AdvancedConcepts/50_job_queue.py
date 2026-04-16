# job_queue.py

import threading
import time
from queue import Queue


job_queue = Queue()


def producer():
    for i in range(5):
        job = f"Job-{i+1}"
        job_queue.put(job)
        print(f"[Producer] Added {job}")
        time.sleep(1)


def consumer():
    while True:
        job = job_queue.get()

        if job is None:
            break

        print(f"[Consumer] Processing {job}")
        time.sleep(2)

        print(f"[Consumer] Completed {job}")

        job_queue.task_done()


def main():
    # Start consumer thread
    t = threading.Thread(target=consumer)
    t.start()

    # Start producer
    producer()

    # Wait until all jobs are done
    job_queue.join()

    # Stop consumer
    job_queue.put(None)
    t.join()

    print("\nAll jobs processed")


main()
