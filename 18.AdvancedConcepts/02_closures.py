# 02_closures.py

def outer_function(message):
    def inner_function():
        print("Message:", message)
    return inner_function


my_func = outer_function("Hello from closure")
my_func()
