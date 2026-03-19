def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Example
text = "A man a plan a canal Panama"
print("Palindrome:", is_palindrome(text))
