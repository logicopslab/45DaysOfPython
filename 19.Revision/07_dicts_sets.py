# ============================================================
# Program 7: Dictionaries & Sets
# Concepts: dict CRUD, comprehensions, defaultdict, Counter,
#           sets, set operations, frozenset
# ============================================================

from collections import defaultdict, Counter

# ---- Dictionary basics -------------------------------------
person = {"name": "Alice", "age": 30, "city": "Chicago"}
print("Dict:", person)
print("Name:", person["name"])
print("Age :", person.get("age"))
print("Missing key (default):", person.get("salary", "N/A"))

person["email"] = "alice@example.com"
person["age"] = 31
del person["city"]
print("Updated:", person)

# ---- Iterating ---------------------------------------------
print("\nIterating dict:")
for key, value in person.items():
    print(f"  {key:<8} : {value}")

# ---- Dict comprehension ------------------------------------
words   = ["apple", "banana", "cherry", "date"]
word_len = {w: len(w) for w in words}
inverted = {v: k for k, v in word_len.items()}    # assumes unique lengths
print("\nWord lengths :", word_len)
print("Inverted     :", inverted)

squares = {x: x**2 for x in range(1, 8) if x % 2 != 0}
print("Odd squares  :", squares)

# ---- Merging dicts (Python 3.9+) ---------------------------
defaults = {"theme": "light", "lang": "en", "debug": False}
user_prefs = {"theme": "dark", "lang": "fr"}
config = defaults | user_prefs          # user_prefs wins on conflict
print("\nMerged config:", config)

# ---- defaultdict -------------------------------------------
print("\nDEFAULTDICT — word frequency")
sentence = "the cat sat on the mat the cat in the hat"
freq = defaultdict(int)
for word in sentence.split():
    freq[word] += 1
for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"  '{word}': {count}")

# ---- Counter -----------------------------------------------
print("\nCOUNTER")
grades = ["A", "B", "A", "C", "B", "A", "D", "B", "A", "C"]
c = Counter(grades)
print("  Grade counts:", dict(c))
print("  Most common :", c.most_common(2))

# ---- Set operations ----------------------------------------
print("\nSET OPERATIONS")
python_devs = {"Alice", "Bob", "Carol", "Dave"}
js_devs     = {"Bob", "Eve", "Dave", "Frank"}

print("  Python devs     :", sorted(python_devs))
print("  JS devs         :", sorted(js_devs))
print("  Union           :", sorted(python_devs | js_devs))
print("  Intersection    :", sorted(python_devs & js_devs))
print("  Difference (Py) :", sorted(python_devs - js_devs))
print("  Symmetric diff  :", sorted(python_devs ^ js_devs))
print("  Is subset?      :", {"Bob", "Dave"} <= python_devs)

# ---- frozenset as dict key ---------------------------------
print("\nFROZENSET as dict key")
pair_scores = {
    frozenset(["Alice", "Bob"]): 95,
    frozenset(["Carol", "Dave"]): 88,
}
print("  Alice-Bob score:", pair_scores[frozenset(["Bob", "Alice"])])