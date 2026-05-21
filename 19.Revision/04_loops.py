# ============================================================
# Program 4: Loops — for, while, break, continue, else
# Concepts: range, enumerate, zip, nested loops, loop else
# ============================================================

print("FOR LOOP — Multiplication Table (1–5)")
print("-" * 40)
for i in range(1, 6):
    row = "  " + "  ".join(f"{i*j:3}" for j in range(1, 6))
    print(row)

# ---- enumerate & zip ---------------------------------------
print("\nENUMERATE")
print("-" * 40)
fruits = ["apple", "banana", "cherry", "date"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}. {fruit}")

print("\nZIP")
print("-" * 40)
names  = ["Alice", "Bob", "Carol"]
scores = [88, 74, 95]
for name, score in zip(names, scores):
    print(f"  {name:6} scored {score}")

# ---- while loop + break/continue ---------------------------
print("\nWHILE LOOP — Collatz Sequence (starting 27)")
print("-" * 40)
n, steps = 27, 0
sequence = [n]
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(n)
    steps += 1
print(f"  Steps: {steps}")
print(f"  Max value reached: {max(sequence)}")
print(f"  Last 10 values: {sequence[-10:]}")

# ---- break, continue, else ---------------------------------
print("\nBREAK / CONTINUE / LOOP-ELSE")
print("-" * 40)

# continue: print only odd numbers
print("  Odd numbers 1-10:", end=" ")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# break: find first multiple of 7 above 50
print("  First multiple of 7 above 50:", end=" ")
for i in range(51, 200):
    if i % 7 == 0:
        print(i)
        break

# loop else: check for prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False   # factor found — no else
    else:
        return True        # loop completed without break → prime

primes = [n for n in range(2, 30) if is_prime(n)]
print(f"  Primes < 30: {primes}")

# ---- Nested loop: pattern ----------------------------------
print("\nNESTED LOOP — Diamond Pattern")
print("-" * 40)
n = 5
for i in range(1, n + 1):
    print("  " + " " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print("  " + " " * (n - i) + "* " * i)