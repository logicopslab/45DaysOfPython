# ============================================================
# Program 8: Strings & Regular Expressions
# Concepts: string methods, formatting, f-strings, textwrap,
#           re module (search, findall, sub, groups)
# ============================================================

import re
import textwrap

# ---- String methods overview --------------------------------
s = "  Hello, World! Python is Amazing.  "
print("Original  :", repr(s))
print("strip()   :", s.strip())
print("lower()   :", s.strip().lower())
print("upper()   :", s.strip().upper())
print("title()   :", s.strip().title())
print("replace() :", s.strip().replace("Python", "Ruby"))
print("split()   :", s.strip().split())
print("startswith:", s.strip().startswith("Hello"))
print("endswith  :", s.strip().endswith("Amazing."))
print("find()    :", s.find("World"))
print("count()   :", s.count("l"))

# ---- Formatting --------------------------------------------
print("\nF-STRING FORMATTING")
pi = 3.14159265358979
amount = 1_234_567.89
print(f"  Pi (4dp)   : {pi:.4f}")
print(f"  Pi (sci)   : {pi:.3e}")
print(f"  Amount     : ${amount:,.2f}")
print(f"  Left  pad  : {'hello':<15}|")
print(f"  Right pad  : {'hello':>15}|")
print(f"  Center pad : {'hello':^15}|")
print(f"  Zero pad   : {42:08d}")
print(f"  Binary     : {255:08b}")
print(f"  Hex        : {255:#010x}")

# ---- textwrap ----------------------------------------------
print("\nTEXTWRAP")
long_text = ("Python is a high-level, general-purpose programming language. "
             "Its design philosophy emphasises code readability with the use "
             "of significant indentation. Python is dynamically typed and "
             "garbage-collected.")
wrapped = textwrap.fill(long_text, width=50)
print(textwrap.indent(wrapped, "  "))

# ---- Regular Expressions -----------------------------------
print("\nREGULAR EXPRESSIONS")

text = ("Contact us at support@example.com or sales@company.org. "
        "Call +1-800-555-0199 or (312) 867-5309. "
        "Visit https://www.example.com or http://docs.python.org/3/")

# Find all email addresses
emails = re.findall(r'[\w.+-]+@[\w-]+\.\w+', text)
print("  Emails  :", emails)

# Find all phone numbers
phones = re.findall(r'[\+\(]?[\d\s\-\(\)]{10,}', text)
print("  Phones  :", [p.strip() for p in phones])

# Find all URLs
urls = re.findall(r'https?://[\w./\-]+', text)
print("  URLs    :", urls)

# Named groups
date_str = "Today is 2025-06-07 and tomorrow is 2025-06-08."
pattern  = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
for m in re.finditer(pattern, date_str):
    print(f"  Date: year={m.group('year')}, month={m.group('month')}, day={m.group('day')}")

# re.sub — redact emails
redacted = re.sub(r'[\w.+-]+@[\w-]+\.\w+', '[REDACTED]', text)
print("\n  Redacted text:")
print(textwrap.indent(textwrap.fill(redacted, 60), "    "))