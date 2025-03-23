# 🟢 **Liskov Substitution Principle (LSP) Cheat Sheet**

---

## 🔑 **LSP Definition:**

> **Subclasses must be replaceable for their base classes without altering program correctness.**

---

## 🚦 **3 Key Rules:**

| Rule               | Meaning in Code                                                                                           | Violation Example                              |
|--------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Method Signature**| Subclass methods must have: <br>• Same/more general inputs <br>• Same/more specific outputs                | Adding extra parameters, changing return type |
| **Precondition**    | Subclass **must NOT require stricter input conditions** than the base class                               | Subclass method demands extra/specific inputs |
| **Postcondition**   | Subclass **must NOT weaken output guarantees** of base class                                              | Subclass method fails or returns weaker output|

---

## 🔽 **Python Summary:**

```python
# Good LSP Example
class Bird:
    def move(self) -> str:
        return "Moves"

class Sparrow(Bird):
    def move(self) -> str:
        return "Flies"

# Bad LSP Violation
class Penguin(Bird):
    def move(self, speed: int) -> int:  # ❌ Changed signature
        return speed  # ❌ Unexpected return
```

---

## ⚙️ **Real-Life Analogy: Universal Plug Adapter**

| Principle         | Programming Equivalent                                       | Adapter Analogy                                      |
|-------------------|--------------------------------------------------------------|-----------------------------------------------------|
| Method Signature  | Accept same/more general inputs + return same/more specific outputs | Adapter accepts any plug & provides same voltage     |
| Precondition      | Subclass doesn’t impose stricter input rules                 | Adapter doesn’t require special plug types          |
| Postcondition     | Subclass fulfills same output guarantees                     | Adapter consistently delivers stable power output   |

---

## 🚩 **Quick Signs of LSP Violation:**
- Subclass requires **extra or stricter parameters**.
- Subclass returns **unexpected types/values**.
- Subclass raises errors where base works fine.
- Behavior changes when subclass replaces base class.

---

## 💡 **Pro Tips (Python Specific):**
- Use **ABC (Abstract Base Classes)** or **Protocols** to formalize behavior.
- Prefer **composition** over forcing subclass behavior if unsure.
- Always **test** substituting subclass in place of base class!


---
# <span style="color:red;">*********************************************************</span>
---


# **1. Method Signature Rule**

### **Rule:**  
**A subclass must have compatible method signatures with the superclass.**

### **In Practice:**
- **Parameters:** Subclass methods **must accept the same parameters or more general ones**.
- **Return Type:** Subclass methods **must return the same or a more specific (narrower) type**.

---

### **Python Example:**

```python
class Animal:
    def make_sound(self) -> str:
        return "Some sound"

class Dog(Animal):
    def make_sound(self) -> str:  # Same return type ✅
        return "Bark"
```

**Violating Signature:**

```python
class Cat(Animal):
    def make_sound(self, volume: int) -> int:  # ❌ Adds extra param + different return type
        return volume
```

💡 **Why Important?**  
If you expect to call `make_sound()` uniformly on `Animal`, you shouldn’t have to know or adapt to differences in `Dog`, `Cat`, etc.

---

# **2. Precondition Rule**

### **Rule:**  
**Subclass must NOT enforce stricter (stronger) conditions on inputs than superclass.**

---

### **What is Precondition?**
The **requirements BEFORE the method runs**, e.g., valid arguments, state.

---

### **Python Example:**

```python
class PaymentProcessor:
    def process(self, amount: float):
        assert amount > 0, "Amount must be positive"
        print(f"Processing ${amount}")

class StrictPaymentProcessor(PaymentProcessor):
    def process(self, amount: float):
        assert amount > 100, "Amount must be over 100"  # ❌ Stricter precondition!
        print(f"Processing VIP payment ${amount}")
```

Now, replacing `PaymentProcessor` with `StrictPaymentProcessor` **breaks the system when amount < 100** → violates LSP.

---

# **3. Postcondition Rule**

### **Rule:**  
**Subclass must NOT weaken the guarantees (results) promised by superclass.**

---

### **What is Postcondition?**
The **state or output AFTER the method finishes**.

---

### **Python Example:**

```python
class FileWriter:
    def write(self, data: str) -> bool:
        # Guarantee: returns True if successful
        print(f"Writing {data}")
        return True

class BuggyFileWriter(FileWriter):
    def write(self, data: str) -> bool:
        print("Oops, didn't write")
        return False  # ❌ Breaks the postcondition (should return True)
```

Code relying on the success (i.e., `True`) will fail if subclass doesn't maintain this guarantee.

---

# **🔑 Quick Summary Table:**

| Rule               | Meaning                                                                                         | Violation Example                             |
|--------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Method Signature**| Accept same/more general inputs, return same/more specific outputs                             | Adding extra params, changing return types    |
| **Precondition**    | Don't require stricter inputs than base class                                                  | Subclass demanding more specific inputs       |
| **Postcondition**   | Don’t weaken the output/result guarantees made by base class                                   | Subclass returning weaker/failing results     |

---

# **Final Thought:**

These rules ensure that **any code using the base class will continue to work perfectly when using the subclass**, which is the whole point of the **Liskov Substitution Principle (LSP)**.

