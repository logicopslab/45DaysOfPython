# ==========================================
# PYTHON OPERATORS DEMONSTRATION PROGRAM
# ==========================================

print("\n===== 1. ARITHMETIC OPERATORS =====")
a = 10
b = 3

print("a =", a, "b =", b)
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b):", a % b)
print("Exponent (a ** b):", a ** b)


print("\n===== 2. COMPARISON OPERATORS =====")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


print("\n===== 3. ASSIGNMENT OPERATORS =====")
x = 5
print("Initial x:", x)

x += 3
print("x += 3:", x)

x -= 2
print("x -= 2:", x)

x *= 4
print("x *= 4:", x)

x /= 2
print("x /= 2:", x)

x //= 3
print("x //= 3:", x)

x %= 2
print("x %= 2:", x)

x **= 3
print("x **= 3:", x)


print("\n===== 4. LOGICAL OPERATORS =====")
p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)


print("\n===== 5. BITWISE OPERATORS =====")
m = 6    # 110 in binary
n = 3    # 011 in binary

print("m =", m, "(", bin(m), ")")
print("n =", n, "(", bin(n), ")")

print("Bitwise AND (m & n):", m & n)
print("Bitwise OR (m | n):", m | n)
print("Bitwise XOR (m ^ n):", m ^ n)
print("Bitwise NOT (~m):", ~m)
print("Left Shift (m << 1):", m << 1)
print("Right Shift (m >> 1):", m >> 1)


print("\n===== 6. MEMBERSHIP OPERATORS =====")
nums = [1, 2, 3, 4, 5]

print("List:", nums)
print("3 in nums:", 3 in nums)
print("10 not in nums:", 10 not in nums)


print("\n===== 7. IDENTITY OPERATORS =====")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)   # Same values
print("list1 is list2:", list1 is list2)   # Different objects
print("list1 is list3:", list1 is list3)   # Same object


print("\n===== 8. TERNARY (CONDITIONAL) OPERATOR =====")
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Age:", age)
print("Status:", status)


print("\n===== PROGRAM COMPLETE =====")