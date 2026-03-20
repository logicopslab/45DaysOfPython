def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

# Example
print(is_rotation("abcd", "cdab"))  # True
