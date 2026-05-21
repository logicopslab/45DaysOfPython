# ============================================================
# Program 3: Control Flow — if / elif / else
# Concepts: conditionals, nested if, ternary, match-case
# ============================================================

def grade_report(score):
    """Return letter grade and feedback for a numeric score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        grade, feedback = "A", "Excellent!"
    elif score >= 80:
        grade, feedback = "B", "Good job!"
    elif score >= 70:
        grade, feedback = "C", "Satisfactory."
    elif score >= 60:
        grade, feedback = "D", "Needs improvement."
    else:
        grade, feedback = "F", "Please study harder."
    return f"Score: {score} → Grade: {grade} — {feedback}"

scores = [95, 83, 71, 65, 40, 101, -5]
print("GRADE REPORT")
print("-" * 40)
for s in scores:
    print(f"  {grade_report(s)}")

# ---- Ternary (conditional expression) ----------------------
print("\nTERNARY EXPRESSIONS")
print("-" * 40)
for n in [-3, 0, 7]:
    label = "positive" if n > 0 else ("zero" if n == 0 else "negative")
    print(f"  {n:>4} is {label}")

# ---- Nested if + membership test ---------------------------
print("\nNESTED IF & MEMBERSHIP")
print("-" * 40)
day = "Saturday"
hour = 14

if day in ("Saturday", "Sunday"):
    if 9 <= hour < 18:
        print(f"  {day} {hour:02d}:00 — Weekend daytime: parks are open!")
    else:
        print(f"  {day} {hour:02d}:00 — Weekend evening: enjoy!")
else:
    print(f"  {day} — Weekday: work time.")

# ---- match-case (Python 3.10+) structural pattern matching -
print("\nMATCH-CASE (HTTP status codes)")
print("-" * 40)

def describe_status(code):
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401 | 403:
            return "Auth error (401 Unauthorized / 403 Forbidden)"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

for code in [200, 201, 403, 404, 418]:
    print(f"  {code} → {describe_status(code)}")