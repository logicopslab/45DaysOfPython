def char_frequency(s):
    freq = {}
    for char in s:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return freq

# Example
print(char_frequency("hello world"))
