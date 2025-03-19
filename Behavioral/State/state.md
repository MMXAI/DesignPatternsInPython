## State Design Pattern in Python

> <span style="color:green;">A **vending machine** that changes its behavior based on its state (e.g., "No Coin", "Has Coin", "Dispensing", "Out of Stock").</span>


---

### Explanation of the Example:

1. **States**:
   - `NoCoinState`: The vending machine is waiting for a coin.
   - `HasCoinState`: The vending machine has received a coin and is waiting for the user to select an item.
   - `DispensingState`: The vending machine is dispensing the selected item.
   - `OutOfStockState`: The vending machine has no items left.

2. **State Transitions**:
   - When a coin is inserted, the machine transitions from `NoCoinState` to `HasCoinState`.
   - When an item is selected, the machine transitions from `HasCoinState` to `DispensingState`.
   - After dispensing, the machine transitions back to `NoCoinState` if items are still available, or to `OutOfStockState` if no items are left.

3. **Context**:
   - The `VendingMachine` class maintains the current state and delegates actions (e.g., `insert_coin`, `select_item`, `dispense_item`) to the current state object.

4. **Behavior**:
   - Each state defines its own behavior for the actions. For example:
     - In `NoCoinState`, selecting an item or dispensing an item will prompt the user to insert a coin first.
     - In `OutOfStockState`, no actions are allowed because the machine is empty.

---

### Benefits of the State Pattern in This Example:
- **Encapsulation**: Each state's behavior is encapsulated in its own class.
- **Avoids Conditionals**: Instead of using large `if-else` or `switch` statements to handle state-specific behavior, the logic is distributed across state classes.
- **Extensibility**: Adding a new state (e.g., "Maintenance Mode") is easy and doesn't require modifying existing code.

---

### When to Use the State Pattern:
- When an object's behavior depends on its state, and it must change its behavior at runtime based on that state.
- When you have a lot of conditional statements that check the object's state to determine its behavior.
- When you want to make state transitions explicit and easy to manage.

--- 

## `Note: Why we use self as the first parameter when defining methods of an objects?`

In Python, the `self` parameter in object methods is a convention used to refer to the instance of the class. It allows methods to access and modify the instance's attributes and call other methods on the same object. Here's why `self` is necessary:

### 1. **Instance Binding**
   - When you call a method on an instance, Python automatically passes the instance as the first argument to the method. This is how the method knows which instance it is operating on.
   - For example, if you have a method `my_method` and call it like `obj.my_method()`, Python translates this to `my_method(obj)` behind the scenes. The `self` parameter captures this instance.

### 2. **Access to Instance Attributes**
   - Inside a method, you often need to access or modify the instance's attributes. By passing `self`, you can refer to these attributes using `self.attribute_name`.
   - Without `self`, the method would have no way to access the instance's data.

### 3. **Explicit is Better Than Implicit**
   - Python follows the principle of explicitness. Requiring `self` makes it clear that you are working with the instance's data and not just local variables or global variables.

### 4. **Consistency with Class and Static Methods**
   - Python also supports class methods (`@classmethod`) and static methods (`@staticmethod`). Class methods use `cls` as the first parameter to refer to the class itself, while static methods don't take any special first parameter. The use of `self` in instance methods maintains consistency with these other types of methods.

### Example
```python
class MyClass:
    def __init__(self, value):
        self.value = value  # 'self' allows us to set an instance attribute

    def display(self):
        print(self.value)  # 'self' allows us to access the instance attribute

obj = MyClass(10)
obj.display()  # Output: 10
```

### What Happens Without `self`?
If you omit `self`, Python will raise an error because the method won't know which instance to operate on. For example:
```python
class MyClass:
    def display():  # Missing 'self'
        print("Hello")

obj = MyClass()
obj.display()  # Error: display() takes 0 positional arguments but 1 was given
```

### Summary
- `self` is a reference to the current instance of the class.
- It allows methods to access and modify instance-specific data.
- It is a convention in Python to make instance methods explicit and consistent.

While `self` is not a reserved keyword, it is a widely accepted convention in the Python community. You could technically use any name (e.g., `this`), but using `self` is recommended for readability and consistency.