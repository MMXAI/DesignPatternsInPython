# Abstract Classes & Decorators in Python:

---

### 1. **Decorator Basics**
   - Decorators add behavior to functions or methods without modifying their code.
   - Can be implemented as **functions** or **classes**.
   - Applied using the `@decorator` syntax.

---

### 2. **Decorators in Abstract and Concrete Classes**
   - If a method in an **abstract class** is decorated:
     - The decorator is **inherited** by concrete classes.
     - Overriding the method in a concrete class **does not automatically apply the decorator** unless you explicitly reapply it.
   - To preserve the decorator in a concrete class:
     - Reapply the decorator to the overridden method.
     - Or use `super().method()` to call the decorated method from the parent class.

---

### 3. **Key Scenarios**
   - **Without `super()` or reapplying the decorator**:
     - The decorator is **not applied** to the overridden method.
   - **With `super()`**:
     - The decorator is applied to the parent class's method.
   - **Reapplying the decorator**:
     - Ensures the decorator is applied to the overridden method.

---

### 4. **Example Summary**
   - **Abstract Class**:
     ```python
     class MyAbstractClass(ABC):
         @MyDecorator
         @abstractmethod
         def my_method(self):
             pass
     ```
   - **Concrete Class**:
     - Without decorator:
       ```python
       def my_method(self):
           print("No decorator applied.")
       ```
     - With `super()`:
       ```python
       def my_method(self):
           super().my_method()  # Decorator applied
       ```
     - Reapplying decorator:
       ```python
       @MyDecorator
       def my_method(self):
           print("Decorator reapplied.")
       ```

---

### 5. **Key Takeaway**
   - **Reapply decorators** or use `super()` in concrete classes to ensure decorator behavior is preserved. Otherwise, the decorator is **not applied** to overridden methods.

---