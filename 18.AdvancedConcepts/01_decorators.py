# 01_decorators.py

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 3))
