# ============================================================
# Program 6: Lists & List Comprehensions
# Concepts: CRUD on lists, slicing, comprehensions, map,
#           filter, sorted, 2D lists, unpacking
# ============================================================

# ---- Creating and modifying --------------------------------
fruits = ["banana", "apple", "cherry", "date", "elderberry"]
print("Original:", fruits)

fruits.append("fig")
fruits.insert(1, "avocado")
fruits.remove("date")
popped = fruits.pop()
print("After ops:", fruits)
print("Popped   :", popped)

# ---- Slicing -----------------------------------------------
nums = list(range(10))          # [0, 1, 2, ..., 9]
print("\nNums     :", nums)
print("Slice [2:7]   :", nums[2:7])
print("Every 2nd     :", nums[::2])
print("Reversed      :", nums[::-1])
print("Last 3        :", nums[-3:])

# ---- Common list methods -----------------------------------
scores = [72, 88, 55, 91, 63, 88, 77]
print("\nScores   :", scores)
print("Sorted   :", sorted(scores))
print("Max      :", max(scores))
print("Min      :", min(scores))
print("Sum      :", sum(scores))
print("Count 88 :", scores.count(88))
print("Index 91 :", scores.index(91))

scores.sort(reverse=True)
print("Desc sort:", scores)

# ---- List comprehensions -----------------------------------
print("\nLIST COMPREHENSIONS")

squares      = [x**2 for x in range(1, 11)]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
flat         = [val for row in [[1,2],[3,4],[5,6]] for val in row]
celsius      = [0, 20, 37, 100]
fahrenheit   = [round(c * 9/5 + 32, 1) for c in celsius]

print("  Squares (1-10) :", squares)
print("  Even squares   :", even_squares)
print("  Flattened      :", flat)
print("  °C → °F        :", list(zip(celsius, fahrenheit)))

# ---- map() and filter() ------------------------------------
print("\nMAP & FILTER")
words   = ["hello", "world", "python", "is", "awesome"]
lengths = list(map(len, words))
long_w  = list(filter(lambda w: len(w) > 4, words))
print("  Lengths :", lengths)
print("  Long    :", long_w)

# ---- 2D list (matrix) --------------------------------------
print("\n2D MATRIX (3×3 identity)")
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
for row in identity:
    print("  ", row)

# ---- Unpacking ---------------------------------------------
print("\nUNPACKING")
first, *middle, last = range(1, 7)
print(f"  first={first}, middle={list(middle)}, last={last}")