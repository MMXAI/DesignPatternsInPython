# Decorator Pattern in Python

Here’s a **full yet concise example** of a **class-based decorator** that includes all key features:

1. **Accepts arguments**: The decorator can take arguments to customize its behavior.
2. **Wraps the function**: The decorator modifies or extends the behavior of the decorated function.
3. **Preserves function metadata**: Uses `functools.wraps` to preserve the original function's name and docstring.

---

### Example: Class-Based Decorator with Arguments

```python
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
```

---

### Output:
```
Start - Before calling greet
End - After calling greet
Start Hello, Alice End
greet
Greets a person by name.
```

---

### Explanation:

1. **Decorator Arguments**:
   - The `CustomDecorator` class accepts `prefix` and `suffix` as arguments during initialization.
   - These arguments customize the behavior of the decorator.

2. **`__call__` Method**:
   - The `__call__` method is invoked when the decorator is applied to a function.
   - It returns a `wrapper` function that wraps the original function.

3. **Wrapper Function**:
   - The `wrapper` function adds behavior before and after calling the original function.
   - It also modifies the result of the original function by adding the `prefix` and `suffix`.

4. **Preserving Metadata**:
   - `functools.wraps(func)` is used to preserve the original function's name (`__name__`) and docstring (`__doc__`).

5. **Usage**:
   - The decorator is applied to the `greet` function with custom arguments (`prefix="Start"`, `suffix="End"`).
   - When `greet("Alice")` is called, the decorator's behavior is executed, and the result is modified.

---

### Key Features in This Example:
- **Accepts arguments**: The decorator can be customized with `prefix` and `suffix`.
- **Wraps the function**: Adds behavior before and after the function call.
- **Modifies the result**: Applies `prefix` and `suffix` to the function's output.
- **Preserves metadata**: Uses `functools.wraps` to maintain the original function's name and docstring.


---
# <span style="color:red;">*********************************************************</span>
---


You're asking how the `wrapper()` method in the `CustomDecorator` class "knows" about `*args` and `**kwargs` when they aren't explicitly referenced elsewhere in the class. Let me clarify this for you.

---

### The Role of `*args` and `**kwargs` in the Wrapper

The `*args` and `**kwargs` in the `wrapper()` method are **not tied to anything outside the `wrapper` itself**. They are simply parameters defined for the `wrapper` function to accept any arguments passed to it when the decorated function is called.

Here’s the key point:

- The `wrapper()` function is a **closure** that "wraps" the original function (`func`).
- When the decorated function is called, the arguments passed to it are **automatically forwarded** to the `wrapper()` function.
- The `wrapper()` function then uses `*args` and `**kwargs` to capture those arguments and forward them to the original function (`func`).

---


### Why Does the Wrapper "Know" About `*args` and `**kwargs`?

The `wrapper` function "knows" about `*args` and `**kwargs` because:

1. **It’s Defined to Accept Them**:
   - The `wrapper` function is explicitly defined with `*args` and `**kwargs` as parameters.
   - This means it can accept any number of positional and keyword arguments.

2. **Arguments Are Passed Automatically**:
   - When the decorated function (`greet`) is called, Python automatically passes the arguments to the `wrapper` function.
   - For example, when you call `greet("Alice")`, the argument `"Alice"` is passed to the `wrapper` as part of `*args`.

3. **Forwarding to the Original Function**:
   - The `wrapper` then forwards these arguments to the original function (`func`) using `func(*args, **kwargs)`.


---
# <span style="color:red;">*********************************************************</span>
---


Let’s clarify what happens when you return a `result` or a `wrapper` function in a class-based decorator.

---

### Key Concepts:
1. **Class-Based Decorators**:
   - A class-based decorator is a class that implements the `__call__` method.
   - The `__call__` method is invoked when the decorated function is called.

2. **Returning a Result**:
   - Inside the `__call__` method, you can return a **result** (e.g., the output of the decorated function).
   - This result is what the caller of the decorated function receives.

3. **Returning a Wrapper Function**:
   - If you return a **wrapper function**, the wrapper function is called instead of the original function.
   - This is useful for modifying or extending the behavior of the original function.

---

### Example 1: Returning a Result

Here’s a class-based decorator that modifies the result of the decorated function:

```python
class AddSuffixDecorator:
    def __init__(self, func):
        self.func = func  # The function being decorated

    def __call__(self, *args, **kwargs):
        # Call the original function and get its result
        result = self.func(*args, **kwargs)
        # Modify the result
        return f"{result} - Suffix Added"

# Usage
@AddSuffixDecorator
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```

---

### Output:
```
Hello, Alice - Suffix Added
```

---

### Explanation:
1. The `__call__` method calls the original function (`self.func`) and stores its result in `result`.
2. The decorator modifies the result by adding a suffix.
3. The modified result is returned to the caller.

---

### Example 2: Returning a Wrapper Function

Here’s a class-based decorator that uses a **wrapper function** to add behavior before and after the original function:

```python
class LoggingDecorator:
    def __init__(self, func):
        self.func = func  # The function being decorated

    def __call__(self, *args, **kwargs):
        # Define a wrapper function
        def wrapper(*args, **kwargs):
            print("Before the function is called.")
            result = self.func(*args, **kwargs)  # Call the original function
            print("After the function is called.")
            return result
        # Return the wrapper function
        return wrapper(*args, **kwargs)

# Usage
@LoggingDecorator
def add(a, b):
    return a + b

print(add(3, 5))
```

---

### Output:
```
Before the function is called.
After the function is called.
8
```

---

### Explanation:
1. The `__call__` method defines a **wrapper function** that adds behavior before and after calling the original function.
2. The wrapper function is called with the same arguments as the original function.
3. The result of the original function is returned by the wrapper function.

---

### Key Differences:
- **Returning a Result**:
  - The decorator directly modifies and returns the result of the original function.
  - Example: Adding a suffix to the result.
- **Returning a Wrapper Function**:
  - The decorator defines a new function (wrapper) that wraps the original function.
  - Example: Adding logging before and after the function call.

---

### When to Use Each Approach:
- Use **returning a result** when you want to modify the output of the function.
- Use **returning a wrapper function** when you want to add behavior around the function call (e.g., logging, timing, etc.).

---

### Summary:
- **Returning a result**: Modifies the output of the decorated function.
- **Returning a wrapper function**: Adds behavior before/after the function call.
- Both approaches are valid and serve different purposes depending on your use case.
