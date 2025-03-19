## Mediator Design Pattern in Python

> <span style="color:green;">This example will simulate an air traffic control system where multiple aircraft (colleagues) communicate with a central air traffic control tower (mediator) to coordinate their movements.</span>

## Problem:
In an air traffic control system, multiple aircraft need to communicate with each other to avoid collisions, request landing permissions, and update their positions. Direct communication between aircraft would lead to a tightly coupled and chaotic system. Instead, we use a mediator (the control tower) to manage and coordinate communication.

# Code Explanation:

1. Mediator Interface (AirTrafficControlTower):

Defines the contract for registering aircraft and sending messages.

2. Concrete Mediator (ControlTower):

Manages a list of registered aircraft.
Implements the logic for broadcasting messages to all aircraft except the sender.

3. Colleague (Aircraft):

Each aircraft has a name and a reference to the control tower.
Aircraft send messages and requests (e.g., landing) through the control tower.
Aircraft receive messages from the control tower.

- Communication Flow:
When an aircraft sends a message, it goes through the control tower, which broadcasts it to all other aircraft.

This ensures that aircraft don’t communicate directly, reducing coupling.

## Key Benefits in This Example:

1. Decoupling:

Aircraft don’t need to know about each other. They only interact with the control tower.

2. Centralized Control:

The control tower manages all communication, making it easier to add new aircraft or change communication rules.

3. Scalability:

Adding more aircraft doesn’t increase the complexity of communication, as all logic is handled by the mediator.

## When to Use This Pattern:

- In systems where multiple objects need to communicate in a structured way (e.g., chat systems, event handling, or distributed systems).

- When you want to avoid tight coupling between objects and centralize communication logic.

This advanced example demonstrates how the Mediator Pattern can be applied to real-world scenarios like air traffic control, ensuring a clean and maintainable design.


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
