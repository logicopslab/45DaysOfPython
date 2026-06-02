# ============================================================
# Program 17: Modules & Packages
# Concepts: import styles, __name__, sys.path, importlib,
#           __all__, creating a mini package in /tmp,
#           standard library highlights
# ============================================================

import sys
import os
import math
import random
import datetime
import importlib

# ---- Different import styles --------------------------------
print("IMPORT STYLES")
print("-" * 45)
print(f"  math.pi          = {math.pi:.6f}")

from math import sqrt, factorial
print(f"  sqrt(144)        = {sqrt(144):.1f}")
print(f"  factorial(10)    = {factorial(10)}")

import math as m
print(f"  m.e              = {m.e:.6f}")

from datetime import date, timedelta
today    = date.today()
deadline = today + timedelta(days=30)
print(f"  Today            = {today}")
print(f"  +30 days         = {deadline}")

# ---- Standard library highlights ---------------------------
print("\nSTANDARD LIBRARY HIGHLIGHTS")
print("-" * 45)

# os
print(f"  os.getcwd()      = {os.getcwd()}")
print(f"  os.cpu_count()   = {os.cpu_count()}")
print(f"  os.sep           = {os.sep!r}")

# sys
print(f"  sys.version      = {sys.version.split()[0]}")
print(f"  sys.platform     = {sys.platform}")
print(f"  sys.path[0]      = {sys.path[0]!r}")

# random
random.seed(42)
print(f"  random.random()  = {random.random():.4f}")
print(f"  randint(1,100)   = {random.randint(1, 100)}")
sample = random.sample(range(50), 6)
print(f"  sample(50,6)     = {sample}")

# math extras
print(f"  math.gcd(48,18)  = {math.gcd(48, 18)}")
print(f"  math.log2(1024)  = {math.log2(1024):.0f}")
print(f"  math.isclose(0.1+0.2, 0.3) = {math.isclose(0.1+0.2, 0.3)}")

# ---- Creating a mini package on disk -----------------------
print("\nCREATING A MINI PACKAGE IN /tmp")
print("-" * 45)

PKG = "/tmp/myutils"
os.makedirs(f"{PKG}/math_utils", exist_ok=True)

# __init__.py
with open(f"{PKG}/__init__.py", "w") as f:
    f.write('"""myutils package."""\n__version__ = "0.1.0"\n')

# math_utils/__init__.py
with open(f"{PKG}/math_utils/__init__.py", "w") as f:
    f.write('from .stats import mean, variance\n__all__ = ["mean", "variance"]\n')

# math_utils/stats.py
with open(f"{PKG}/math_utils/stats.py", "w") as f:
    f.write(
        'def mean(data):\n'
        '    return sum(data) / len(data)\n\n'
        'def variance(data):\n'
        '    mu = mean(data)\n'
        '    return sum((x - mu)**2 for x in data) / len(data)\n'
    )

# Add package to path and import dynamically
if PKG not in sys.path:
    sys.path.insert(0, PKG)

stats = importlib.import_module("math_utils")
data  = [4, 8, 15, 16, 23, 42]
print(f"  data      = {data}")
print(f"  mean      = {stats.mean(data):.2f}")
print(f"  variance  = {stats.variance(data):.2f}")

# ---- __name__ guard ----------------------------------------
print("\n__NAME__ GUARD")
print("-" * 45)
print(f"  This module __name__ = {__name__!r}")
print("  (When run directly, __name__ == '__main__')")
print("  (When imported,     __name__ == 'module_name')")

if __name__ == "__main__":
    print("  → Running as main script ✓")

# Cleanup
import shutil
shutil.rmtree(PKG)