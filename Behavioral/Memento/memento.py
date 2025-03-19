# Memento: Stores the state of the TextEditor
class TextMemento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


# Originator: The TextEditor that can save and restore its state
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        print(f"TextEditor: Writing '{text}'")
        self._content += text

    def save(self):
        print("TextEditor: Saving state to Memento.")
        return TextMemento(self._content)

    def restore(self, memento):
        self._content = memento.get_content()
        print(f"TextEditor: Restored state. Current content: '{self._content}'")

    def __str__(self):
        return f"TextEditor: Current content = '{self._content}'"


# Caretaker: Manages the history of mementos for undo/redo
class History:
    def __init__(self):
        self._undo_stack = []  # Stack for undo operations
        self._redo_stack = []  # Stack for redo operations

    def save_state(self, memento):
        self._undo_stack.append(memento)
        self._redo_stack.clear()  # Clear redo stack when a new state is saved
        print("History: State saved.")

    def undo(self):
        if not self._undo_stack:
            print("History: Nothing to undo.")
            return None
        memento = self._undo_stack.pop()
        self._redo_stack.append(memento)
        print("History: Undo performed.")
        return memento

    def redo(self):
        if not self._redo_stack:
            print("History: Nothing to redo.")
            return None
        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)
        print("History: Redo performed.")
        return memento


# Client Code
if __name__ == "__main__":
    # Create the text editor and history manager
    editor = TextEditor()
    history = History()

    # Write some text and save the state
    editor.write("Hello, ")
    history.save_state(editor.save())

    editor.write("world!")
    history.save_state(editor.save())

    editor.write(" How are you?")
    history.save_state(editor.save())

    print("\nCurrent state:")
    print(editor)

    # Perform undo
    print("\nUndoing last change:")
    editor.restore(history.undo())
    print(editor)

    # Perform undo again
    print("\nUndoing another change:")
    editor.restore(history.undo())
    print(editor)

    # Perform redo
    print("\nRedoing last undo:")
    editor.restore(history.redo())
    print(editor)

    # Perform redo again
    print("\nRedoing another undo:")
    editor.restore(history.redo())
    print(editor)