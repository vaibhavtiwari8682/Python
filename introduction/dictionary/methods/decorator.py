#A decorator is a function that adds extra functionality to another function without changing its original code.
def my_decorator(func):
    def wrapper():
         print("Something is happening before the function is called")
         func()
         print("Something is happening after the function  is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()