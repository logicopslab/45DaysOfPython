# ============================================================
# Program 9: File I/O
# Concepts: open/read/write, context manager, csv, json,
#           pathlib, os.path, binary files
# ============================================================

import csv
import json
import os
from pathlib import Path

# Work in a temp directory
BASE = Path("/tmp/py_file_io_demo")
BASE.mkdir(exist_ok=True)

# ---- Plain text file ---------------------------------------
txt_file = BASE / "notes.txt"

# Write
with open(txt_file, "w") as f:
    f.write("Line 1: Python file I/O\n")
    f.write("Line 2: Reading and writing files\n")
    f.writelines([f"Line {i}: Generated\n" for i in range(3, 6)])

# Read all at once
with open(txt_file) as f:
    content = f.read()
print("TEXT FILE CONTENT:")
print(content)

# Read line by line
with open(txt_file) as f:
    lines = [line.rstrip() for line in f]
print(f"Line count: {len(lines)}")
print(f"Last line : {lines[-1]}\n")

# Append
with open(txt_file, "a") as f:
    f.write("Line 6: Appended later\n")

# ---- CSV file ----------------------------------------------
csv_file = BASE / "students.csv"

students = [
    {"name": "Alice",  "score": 92, "grade": "A"},
    {"name": "Bob",    "score": 78, "grade": "C"},
    {"name": "Carol",  "score": 85, "grade": "B"},
    {"name": "Dave",   "score": 60, "grade": "D"},
]

# Write CSV
with open(csv_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score", "grade"])
    writer.writeheader()
    writer.writerows(students)

# Read CSV
print("CSV FILE CONTENT:")
with open(csv_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']:<8} score={row['score']}  grade={row['grade']}")

# ---- JSON file ---------------------------------------------
json_file = BASE / "config.json"

config = {
    "app": "MyApp",
    "version": "1.2.3",
    "features": {"dark_mode": True, "notifications": False},
    "limits": [100, 200, 500],
}

# Write JSON
with open(json_file, "w") as f:
    json.dump(config, f, indent=2)

# Read JSON
with open(json_file) as f:
    loaded = json.load(f)

print(f"\nJSON LOADED:")
print(f"  App        : {loaded['app']} v{loaded['version']}")
print(f"  Dark mode  : {loaded['features']['dark_mode']}")
print(f"  Limits     : {loaded['limits']}")

# ---- pathlib operations ------------------------------------
print("\nPATHLIB OPERATIONS:")
for p in sorted(BASE.iterdir()):
    size = p.stat().st_size
    print(f"  {p.name:<20} {size:>5} bytes  suffix={p.suffix}")

# rename a file
old = BASE / "notes.txt"
new = BASE / "notes_backup.txt"
old.rename(new)
print(f"\nRenamed notes.txt → notes_backup.txt")
print(f"Exists? {new.exists()}")

# ---- Cleanup -----------------------------------------------
import shutil
shutil.rmtree(BASE)
print("\nDemo files cleaned up.")