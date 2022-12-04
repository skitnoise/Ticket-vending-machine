def my_decorator_func(func):

    def wrapper_func(*args):
        print("Your number is")
        func()
    return wrapper_func


