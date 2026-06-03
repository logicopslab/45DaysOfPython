# ============================================================
# Program 18: Concurrency — Threading & Multiprocessing
# Concepts: Thread, Lock, ThreadPoolExecutor, Queue,
#           Process, Pool, shared memory, timing comparison
# ============================================================

import threading
import multiprocessing
import time
import queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# ---- Basic Thread ------------------------------------------
print("BASIC THREADS")
print("-" * 45)

results = {}
lock    = threading.Lock()

def fetch_data(name, delay, value):
    time.sleep(delay)
    with lock:
        results[name] = value
        print(f"  Thread '{name}' done (delay={delay}s)")

threads = [
    threading.Thread(target=fetch_data, args=("A", 0.1, 100)),
    threading.Thread(target=fetch_data, args=("B", 0.05, 200)),
    threading.Thread(target=fetch_data, args=("C", 0.15, 300)),
]

t0 = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
elapsed = time.perf_counter() - t0
print(f"  All done in {elapsed:.3f}s (sequential would be ~0.30s)")
print(f"  Results: {results}")

# ---- Producer-Consumer with Queue --------------------------
print("\nPRODUCER-CONSUMER (Queue)")
print("-" * 45)

def producer(q, items):
    for item in items:
        q.put(item)
        time.sleep(0.01)
    q.put(None)                          # sentinel

def consumer(q, collected):
    while True:
        item = q.get()
        if item is None:
            break
        collected.append(item * 2)
        q.task_done()

q         = queue.Queue()
collected = []
items     = list(range(1, 11))

p = threading.Thread(target=producer, args=(q, items))
c = threading.Thread(target=consumer, args=(q, collected))
p.start(); c.start()
p.join();  c.join()
print(f"  Produced: {items}")
print(f"  Consumed (×2): {collected}")

# ---- ThreadPoolExecutor ------------------------------------
print("\nTHREADPOOL EXECUTOR (simulated I/O)")
print("-" * 45)

def io_task(n):
    time.sleep(0.05)
    return n * n

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(io_task, i): i for i in range(1, 9)}
    for future in as_completed(futures):
        print(f"  io_task({futures[future]}) = {future.result()}")
print(f"  Finished in {time.perf_counter()-t0:.3f}s")

# ---- CPU-bound: multiprocessing Pool -----------------------
print("\nMULTIPROCESSING POOL (CPU-bound)")
print("-" * 45)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

numbers = list(range(1, 200_001))

t0 = time.perf_counter()
with multiprocessing.Pool(processes=2) as pool:
    prime_flags = pool.map(is_prime, numbers)
primes = [n for n, flag in zip(numbers, prime_flags) if flag]
elapsed = time.perf_counter() - t0

print(f"  Primes up to 200,000: {len(primes)}")
print(f"  Last 5 primes: {primes[-5:]}")
print(f"  Time (2 processes): {elapsed:.3f}s")