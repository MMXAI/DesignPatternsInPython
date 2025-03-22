class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state  # Intrinsic state

    def operation(self, unique_state):
        print(f"Shared: {self.shared_state}, Unique: {unique_state}")


class FlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, shared_state):
        if shared_state not in cls._flyweights:
            cls._flyweights[shared_state] = Flyweight(shared_state)
        return cls._flyweights[shared_state]


# Client code
factory = FlyweightFactory()

# Adding objects with shared and unique states
flyweight1 = factory.get_flyweight("shared_data_1")
flyweight1.operation("unique_data_1")  # Shared: shared_data_1, Unique: unique_data_1

flyweight2 = factory.get_flyweight("shared_data_2")
flyweight2.operation("unique_data_2")  # Shared: shared_data_2, Unique: unique_data_2

# Reusing existing flyweight
flyweight3 = factory.get_flyweight("shared_data_1")
flyweight3.operation("unique_data_3")  # Shared: shared_data_1, Unique: unique_data_3
