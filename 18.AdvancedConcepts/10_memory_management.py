# 10_memory_management.py

import sys

a = [1, 2, 3]
b = a

print("Reference count:", sys.getrefcount(a))

del b

print("Reference count after deleting b:", sys.getrefcount(a))
