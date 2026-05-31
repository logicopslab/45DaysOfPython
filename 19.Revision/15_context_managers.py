# ============================================================
# Program 15: Context Managers
# Concepts: __enter__/__exit__, contextlib.contextmanager,
#           suppress, redirect_stdout, ExitStack, timing CM
# ============================================================

import time
import io
import sqlite3
import tempfile
from contextlib import (contextmanager, suppress,
                         redirect_stdout, ExitStack)

# ---- Class-based context manager ---------------------------
class Timer:
    """Context manager that measures elapsed time."""

    def __init__(self, label=""):
        self.label   = label
        self.elapsed = 0.0

    def __enter__(self):
        self._start = time.perf_counter()
        return self                          # available as 'as' target

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self._start
        label = f"[{self.label}] " if self.label else ""
        print(f"  {label}elapsed: {self.elapsed*1000:.3f} ms")
        return False                         # don't suppress exceptions

print("CLASS-BASED CONTEXT MANAGER — Timer")
print("-" * 45)
with Timer("sum 1M") as t:
    total = sum(range(1_000_000))
print(f"  Total = {total:,}")

# ---- @contextmanager decorator -----------------------------
@contextmanager
def managed_db(db_path=":memory:"):
    """Open a SQLite connection, yield it, and always close it."""
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()
        print("  DB: committed.")
    except Exception as e:
        conn.rollback()
        print(f"  DB: rolled back ({e}).")
        raise
    finally:
        conn.close()
        print("  DB: connection closed.")

print("\n@CONTEXTMANAGER — SQLite")
print("-" * 45)
with managed_db() as db:
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    db.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
    rows = db.execute("SELECT * FROM users").fetchall()
    for row in rows:
        print(f"  User: {row}")

# ---- suppress() -------------------------------------------
print("\nSUPPRESS")
print("-" * 45)
with suppress(FileNotFoundError, PermissionError):
    open("/no/such/file")
print("  No exception leaked out.")

# ---- redirect_stdout() ------------------------------------
print("\nREDIRECT_STDOUT")
print("-" * 45)
buffer = io.StringIO()
with redirect_stdout(buffer):
    print("This goes into the buffer, not the terminal.")
    for i in range(3):
        print(f"  Line {i}")
captured = buffer.getvalue()
print(f"  Captured {len(captured.splitlines())} lines:")
for line in captured.splitlines():
    print(f"    > {line}")

# ---- ExitStack for dynamic/variable context managers -------
print("\nEXITSTACK — dynamic file management")
print("-" * 45)
filenames = []
with ExitStack() as stack:
    for i in range(3):
        f = stack.enter_context(tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False))
        f.write(f"Content of file {i}\n")
        filenames.append(f.name)
    # All files are still open here
    print(f"  Opened {len(filenames)} temp files.")
# All files closed automatically when ExitStack exits
print("  All temp files closed by ExitStack.")

# Clean up temp files
import os
for fn in filenames:
    os.unlink(fn)
print("  Temp files deleted.")