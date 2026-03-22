# 06_functional_programming.py
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x**2, numbers))

# filter
even = list(filter(lambda x: x % 2 == 0, numbers))

# reduce
sum_all = reduce(lambda x, y: x + y, numbers)

print("Squared:", squared)
print("Even:", even)
print("Sum:", sum_all)
