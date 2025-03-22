# Step 1: Define the Observer interface
class Observer:
    def update(self, message):
        pass


# Step 2: Define the Subject
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Step 3: Create ConcreteSubject
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    def set_state(self, state):
        self._state = state
        self.notify(f"State updated to: {self._state}")


# Step 4: Create ConcreteObserver
class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message: {message}")


# Step 5: Use the Observer Pattern
if __name__ == "__main__":
    # Create a subject
    subject = ConcreteSubject()

    # Create observers
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    # Attach observers to the subject
    subject.attach(observer1)
    subject.attach(observer2)

    # Change the subject's state
    subject.set_state("State 1")
    subject.set_state("State 2")

    # Detach an observer
    subject.detach(observer1)

    # Change the subject's state again
    subject.set_state("State 3")
