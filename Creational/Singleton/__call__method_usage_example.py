class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling function: {self.func.__name__}")
        # new_args: tuple = tuple([arg.upper() for arg in args])
        new_args: tuple = tuple(["\nBeautiful\n" + args[0]])
        return self.func(*new_args, **kwargs)


@Logger
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
