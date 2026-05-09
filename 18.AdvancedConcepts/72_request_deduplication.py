# request_deduplication.py

import time


processed_requests = {}


def process_request(request_id):
    current_time = time.time()

    # Remove expired entries
    expired = []

    for rid, timestamp in processed_requests.items():
        if current_time - timestamp > 5:
            expired.append(rid)

    for rid in expired:
        del processed_requests[rid]

    # Deduplication check
    if request_id in processed_requests:
        print(f"[DUPLICATE] Ignoring request: {request_id}")
        return

    processed_requests[request_id] = current_time

    print(f"[PROCESSING] Request: {request_id}")


def simulate():
    requests = ["r1", "r2", "r1", "r3", "r2"]

    for req in requests:
        process_request(req)
        time.sleep(1)


def main():
    simulate()


main()