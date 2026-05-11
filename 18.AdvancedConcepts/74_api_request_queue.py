# api_request_queue.py

import threading
import time
from queue import Queue


request_queue = Queue()


def api_worker():
    while True:
        request = request_queue.get()

        if request is None:
            break

        print(f"[Worker] Processing request: {request}")
        time.sleep(2)

        print(f"[Worker] Completed request: {request}")

        request_queue.task_done()


def receive_request(request_id):
    print(f"[API] Received request: {request_id}")
    request_queue.put(request_id)


def main():
    worker = threading.Thread(target=api_worker)
    worker.start()

    for i in range(5):
        receive_request(f"REQ-{i+1}")
        time.sleep(1)

    request_queue.join()

    request_queue.put(None)
    worker.join()

    print("\nAll API requests processed")


main()