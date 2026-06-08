# ============================================================
# Program 24: SQLite Database
# Concepts: sqlite3, CRUD, transactions, parameterised queries,
#           joins, aggregates, context managers, row_factory
# ============================================================

import sqlite3
from contextlib import contextmanager
from datetime import date, timedelta
import random

DB_PATH = ":memory:"          # in-memory DB for demo

# ---- Connection helper -------------------------------------
@contextmanager
def get_db(path=DB_PATH):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row        # dict-like rows
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

# ---- Schema ------------------------------------------------
SCHEMA = """
CREATE TABLE IF NOT EXISTS departments (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employees (
    id         INTEGER PRIMARY KEY,
    name       TEXT    NOT NULL,
    dept_id    INTEGER NOT NULL REFERENCES departments(id),
    salary     REAL    NOT NULL CHECK (salary >= 0),
    hired_on   TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS assignments (
    emp_id  INTEGER REFERENCES employees(id),
    proj_id INTEGER REFERENCES projects(id),
    role    TEXT,
    PRIMARY KEY (emp_id, proj_id)
);
"""

# ---- Seed data ---------------------------------------------
DEPTS = ["Engineering", "Marketing", "HR", "Finance"]
EMPS  = [
    ("Alice Smith",   1, 95_000, "2020-01-15"),
    ("Bob Jones",     1, 88_000, "2021-03-01"),
    ("Carol White",   2, 72_000, "2019-07-22"),
    ("Dave Brown",    2, 68_000, "2022-05-10"),
    ("Eve Davis",     3, 65_000, "2018-11-30"),
    ("Frank Miller",  4, 105_000,"2017-04-01"),
    ("Grace Wilson",  1, 91_000, "2023-02-14"),
]
PROJS = ["Alpha", "Beta", "Gamma"]
ASSGN = [
    (1, 1, "Lead"),   (2, 1, "Member"), (3, 2, "Lead"),
    (4, 2, "Member"), (5, 3, "Member"), (1, 2, "Advisor"),
    (7, 1, "Member"),
]

def seed(conn):
    conn.executemany("INSERT INTO departments (name) VALUES (?)", [(d,) for d in DEPTS])
    conn.executemany("INSERT INTO employees (name, dept_id, salary, hired_on) VALUES (?,?,?,?)", EMPS)
    conn.executemany("INSERT INTO projects (name) VALUES (?)", [(p,) for p in PROJS])
    conn.executemany("INSERT INTO assignments (emp_id, proj_id, role) VALUES (?,?,?)", ASSGN)

# ---- Queries -----------------------------------------------
def print_section(title):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}")

with get_db() as db:
    db.executescript(SCHEMA)
    seed(db)

    # All employees with department name
    print_section("ALL EMPLOYEES")
    rows = db.execute("""
        SELECT e.id, e.name, d.name AS dept, e.salary, e.hired_on
        FROM employees e JOIN departments d ON e.dept_id = d.id
        ORDER BY e.salary DESC
    """).fetchall()
    for r in rows:
        print(f"  [{r['id']}] {r['name']:<15} {r['dept']:<12} £{r['salary']:>9,.0f}  {r['hired_on']}")

    # Aggregate per department
    print_section("DEPARTMENT STATS")
    rows = db.execute("""
        SELECT d.name, COUNT(*) AS headcount,
               ROUND(AVG(e.salary),2) AS avg_sal,
               MAX(e.salary) AS max_sal
        FROM employees e JOIN departments d ON e.dept_id = d.id
        GROUP BY d.id
        ORDER BY avg_sal DESC
    """).fetchall()
    for r in rows:
        print(f"  {r['name']:<12}  n={r['headcount']}  avg=£{r['avg_sal']:>9,.2f}  max=£{r['max_sal']:>9,.0f}")

    # Employees per project
    print_section("PROJECT ASSIGNMENTS")
    rows = db.execute("""
        SELECT p.name AS project, e.name AS employee, a.role
        FROM assignments a
        JOIN employees e ON a.emp_id  = e.id
        JOIN projects  p ON a.proj_id = p.id
        ORDER BY p.name, a.role
    """).fetchall()
    for r in rows:
        print(f"  {r['project']:<8} {r['employee']:<15} ({r['role']})")

    # Update: give Engineering a 10% raise
    db.execute("""
        UPDATE employees SET salary = salary * 1.10
        WHERE dept_id = (SELECT id FROM departments WHERE name = 'Engineering')
    """)
    updated = db.execute("""
        SELECT e.name, e.salary FROM employees e
        JOIN departments d ON e.dept_id = d.id
        WHERE d.name = 'Engineering'
    """).fetchall()
    print_section("AFTER 10% RAISE — Engineering")
    for r in updated:
        print(f"  {r['name']:<15} £{r['salary']:>10,.2f}")

    # Parameterised search
    print_section("PARAMETERISED SEARCH  (salary > £90,000)")
    rows = db.execute(
        "SELECT name, salary FROM employees WHERE salary > ? ORDER BY salary DESC",
        (90_000,)
    ).fetchall()
    for r in rows:
        print(f"  {r['name']:<15} £{r['salary']:>10,.2f}")

    # Delete and verify (remove assignments first to satisfy FK)
    db.execute("DELETE FROM assignments WHERE emp_id = (SELECT id FROM employees WHERE name = 'Dave Brown')")
    db.execute("DELETE FROM employees WHERE name = 'Dave Brown'")
    remaining = db.execute("SELECT COUNT(*) FROM employees").fetchone()[0]
    print_section(f"AFTER DELETE — remaining employees: {remaining}")