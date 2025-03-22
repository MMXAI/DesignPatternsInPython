# Chaining decorators in Python 

---

### How Chaining Works:
1. **Order of Application**:
   - Decorators are applied from **bottom to top** (i.e., the decorator closest to the function is applied first).
   - This means the **innermost decorator** is executed first, and the **outermost decorator** is executed last.

2. **Execution Flow**:
   - Each decorator wraps the function (or the result of the previous decorator) in its own logic.
   - When the function is called, the outermost decorator's logic runs first, followed by the inner decorators, and finally the original function.

---

### Example: Chaining Two Decorators


`Example with Class-Based Decorators`

Chaining works the same way with class-based decorators. Here’s an example:

```python
class AddPrefix:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return f"Prefix: {result}"

class AddSuffix:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return f"{result} - Suffix"

# Applying both decorators
@AddPrefix
@AddSuffix
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```


### Output:
```
Prefix: Hello, Alice - Suffix
```

---

### Explanation of Execution:
1. **Order of Application**:
   - `@add_suffix` is applied first (closest to the function).
   - `@add_prefix` is applied second (outermost decorator).

2. **Execution Flow**:
   - When `greet("Alice")` is called:
     - The `add_prefix` decorator runs first (outermost).
     - Inside `add_prefix`, the `add_suffix` decorator runs.
     - Inside `add_suffix`, the original `greet` function runs and returns `"Hello, Alice"`.
     - The `add_suffix` decorator modifies the result to `"Hello, Alice - Suffix"`.
     - The `add_prefix` decorator modifies the result to `"Prefix: Hello, Alice - Suffix"`.

---


---

### Summary:
- **Chaining decorators** applies them from **bottom to top** (innermost first, outermost last).
- Each decorator wraps the function (or the result of the previous decorator) in its own logic.
- The **order of decorators** matters and affects the final result.
- Chaining is a powerful way to combine multiple behaviors in a clean and modular way.
