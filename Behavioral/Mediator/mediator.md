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