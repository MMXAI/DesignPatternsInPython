class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print("At Meta Class (Unique and Once Only): Hello")
        print("At Meta Class(Repeatitive): Hello")
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def __new__(cls):
        print("At Normal Class (__new__): Hello")
        return super().__new__(cls)

    def __init__(self):
        print("At Normal Class (__init__): Hello")
        self.data = "Singleton Data"


# Usage
print("\nCreating instance1\n")
instance1 = Singleton()
print("\nCreating instance2\n")
instance2 = Singleton()

print(instance1 is instance2)  # Output: True
