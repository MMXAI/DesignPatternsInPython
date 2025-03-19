## Observer Design Pattern
a behavioral design pattern that defines a one-to-many dependency between objects. 
> <span style="color:green;">When one object (the **subject**) changes its state, all its dependents (**observers**) are notified and updated automatically. This pattern is commonly used in event handling systems, where one object's state change triggers actions in other objects.</span>

### Key Components of the Observer Pattern:
1. **Subject**: The object that holds the state and notifies observers when the state changes.
2. **Observer**: An interface or abstract class that defines the method(s) to be called when the subject's state changes.
3. **ConcreteSubject**: The concrete implementation of the subject. It maintains the state and sends notifications to observers.
4. **ConcreteObserver**: The concrete implementation of the observer. It registers itself with the subject and gets notified when the subject's state changes.


### Code Explanation:
1. **Observer Interface**: The `Observer` class defines the `update` method, which is implemented by concrete observers.
2. **Subject**: The `Subject` class maintains a list of observers and provides methods to attach, detach, and notify them.
3. **ConcreteSubject**: The `ConcreteSubject` class extends the `Subject` and manages its state. When the state changes, it notifies all observers.
4. **ConcreteObserver**: The `ConcreteObserver` class implements the `update` method to react to state changes in the subject.
5. **Usage**: Observers are attached to the subject, and when the subject's state changes, all observers are notified.

### Advantages of the Observer Pattern:
- Decouples the subject and observers, promoting loose coupling.
- Allows dynamic addition or removal of observers at runtime.
- Supports broadcast communication.

### Use Cases:
- Event handling systems.
- GUI frameworks (e.g., button clicks triggering actions).
- Notifications in distributed systems.

This pattern is widely used in Python libraries like `RxPy` (Reactive Extensions) and frameworks like Django's signal system.

---
## `Observer Pattern V.S. Mediator Pattern`

### **Key Differences**

| **Aspect**              | **Observer Pattern**                          | **Mediator Pattern**                          |
|--------------------------|-----------------------------------------------|-----------------------------------------------|
| **Purpose**              | Notify observers of state changes.            | Centralize complex communication logic.       |
| **Communication**        | Direct (subject notifies observers).          | Indirect (objects communicate via mediator).  |
| **Coupling**             | Loose coupling between subject and observers. | Loose coupling between interacting objects.   |
| **Number of Objects**    | One subject, many observers.                  | Many objects interacting through one mediator.|
| **Complexity**           | Simpler, focused on state propagation.        | More complex, handles interaction logic.      |
| **Example**              | Event handling, notifications.                | Chat systems, air traffic control systems.    |

---

### **When to Use Which?**
- Use the **Observer Pattern** when:
  - You need to notify multiple objects about state changes in a single object.
  - You want to decouple the subject from its observers.
  - Example: Event handling, notification systems.

- Use the **Mediator Pattern** when:
  - You have a complex web of interactions between multiple objects.
  - You want to centralize communication logic to reduce dependencies.
  - Example: Chat systems, UI components interacting with each other.

---

### **Summary**
- **Observer**: Focuses on one-to-many state propagation.
- **Mediator**: Focuses on managing many-to-many interactions through a central mediator.


### **In Short:**
- **Observer**: Use for **state propagation** (one → many).
- **Mediator**: Use for **complex interactions** (many ↔ many).
