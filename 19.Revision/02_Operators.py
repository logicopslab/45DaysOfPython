# ============================================================
# Program 2: Operators & Expressions
# Concepts: arithmetic, comparison, logical, bitwise, walrus
# ============================================================

print("=" * 45)
print("  ARITHMETIC OPERATORS")
print("=" * 45)
a, b = 17, 5
print(f"a={a}, b={b}")
print(f"  Addition       : {a} + {b}  = {a + b}")
print(f"  Subtraction    : {a} - {b}  = {a - b}")
print(f"  Multiplication : {a} * {b}  = {a * b}")
print(f"  Division       : {a} / {b}  = {a / b}")
print(f"  Floor Division : {a} // {b} = {a // b}")
print(f"  Modulus        : {a} % {b}  = {a % b}")
print(f"  Exponentiation : {a} ** {b} = {a ** b}")

print("\n" + "=" * 45)
print("  COMPARISON OPERATORS")
print("=" * 45)
print(f"  {a} == {b}  → {a == b}")
print(f"  {a} != {b}  → {a != b}")
print(f"  {a} >  {b}  → {a > b}")
print(f"  {a} <  {b}  → {a < b}")
print(f"  {a} >= {b}  → {a >= b}")
print(f"  {a} <= {b}  → {a <= b}")

print("\n" + "=" * 45)
print("  LOGICAL OPERATORS")
print("=" * 45)
x, y = True, False
print(f"  True and False → {x and y}")
print(f"  True or  False → {x or y}")
print(f"  not True       → {not x}")
print(f"  Short-circuit  : True or (1/0) → {True or (1/0)}")

print("\n" + "=" * 45)
print("  BITWISE OPERATORS")
print("=" * 45)
p, q = 0b1010, 0b1100   # 10 and 12
print(f"  p={p} (1010), q={q} (1100)")
print(f"  AND  : {p} & {q}  = {p & q}   (binary: {p & q:04b})")
print(f"  OR   : {p} | {q}  = {p | q}  (binary: {p | q:04b})")
print(f"  XOR  : {p} ^ {q}  = {p ^ q}   (binary: {p ^ q:04b})")
print(f"  NOT  : ~{p}      = {~p}")
print(f"  LEFT : {p} << 1  = {p << 1}")
print(f"  RIGHT: {p} >> 1  = {p >> 1}")

print("\n" + "=" * 45)
print("  ASSIGNMENT & WALRUS OPERATOR")
print("=" * 45)
n = 10
n += 5;  print(f"  n += 5  → {n}")
n -= 3;  print(f"  n -= 3  → {n}")
n *= 2;  print(f"  n *= 2  → {n}")
n //= 3; print(f"  n //= 3 → {n}")

# Walrus operator (Python 3.8+)
numbers = [1, 5, 3, 9, 2]
if (maximum := max(numbers)) > 8:
    print(f"\n  Walrus: max of {numbers} is {maximum} (> 8)")