import functools

# Class-Based Decorator that accepts arguments
class CustomDecorator:
    def __init__(self, prefix="", suffix=""):
        self.prefix = prefix  # Custom argument: prefix
        self.suffix = suffix  # Custom argument: suffix

    def __call__(self, func):
        @functools.wraps(func)  # Preserves function metadata
        def wrapper(*args, **kwargs):
            # Add behavior before the function call
            print(f"{self.prefix} - Before calling {func.__name__}")

            # Call the original function
            result = func(*args, **kwargs)

            # Add behavior after the function call
            print(f"{self.suffix} - After calling {func.__name__}")

            # Modify the result (optional)
            return f"{self.prefix} {result} {self.suffix}"
        return wrapper

# Using the decorator with arguments
@CustomDecorator(prefix="Start", suffix="End")
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}"

# Calling the decorated function
print(greet("Alice"))
print(greet.__name__)  # Preserves the original function name
print(greet.__doc__)   # Preserves the original docstring