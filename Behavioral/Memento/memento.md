## Memento Design Pattern in Python
 
> <span style="color:green;">This example will simulate a text editor with undo/redo functionality, where the editor's state (text content) can be saved and restored using the Memento pattern.</span>

## Components:

1. Originator: The TextEditor class, which holds the current text content and can create/restore mementos.

2. Memento: The TextMemento class, which stores the state of the TextEditor.

3. Caretaker: The History class, which manages a stack of mementos for undo/redo functionality.

## Code Explanation:

- TextMemento:

Stores the state of the TextEditor (the content).

Provides a method (get_content) to retrieve the saved state.

- TextEditor:

Manages the current text content.

Provides methods to:

Write text (write).

Save the current state to a TextMemento (save).

Restore the state from a TextMemento (restore).

- History:

Manages two stacks:

_undo_stack: Stores mementos for undo operations.

_redo_stack: Stores mementos for redo operations.

Provides methods to:

Save a state (save_state).

Undo the last change (undo).

Redo the last undone change (redo).

- Client Code:

Simulates a text editor where the user writes text, saves the state, and performs undo/redo operations.

## Key Features of This Example:

- Undo/Redo Functionality:

The History class manages a stack of mementos, enabling undo and redo operations.

Each time a state is saved, the redo stack is cleared to maintain consistency.

- Encapsulation:

The TextMemento class encapsulates the state of the TextEditor, ensuring that the state is not directly exposed.

- Flexibility:

The TextEditor can save and restore its state at any point, making it easy to implement features like autosave or versioning.

## Use Cases:

Text Editors: Implement undo/redo functionality.

Graphic Design Tools: Save and restore the state of a canvas.

Games: Save and restore game progress or character states.

Transaction Systems: Roll back to a previous state in case of errors.

This advanced example demonstrates how the Memento pattern can be applied to real-world scenarios, providing a robust and maintainable solution for state management.