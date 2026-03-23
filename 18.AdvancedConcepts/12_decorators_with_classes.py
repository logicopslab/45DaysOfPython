# 12_decorators_with_classes.py

def method_logger(func):
    def wrapper(self, *args):
        print(f"Method {func.__name__} called")
        return func(self, *args)
    return wrapper


class Calculator:

    @method_logger
    def add(self, a, b):
        return a + b


obj = Calculator()
print(obj.add(3, 4))
