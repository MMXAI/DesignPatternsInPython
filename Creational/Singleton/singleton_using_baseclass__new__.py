class SingletonBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            print("At Base Class __new__ : Hello \t FIRST TIME")
        print("At Base Class __new__ : Hello \t EVERY TIME")
        return cls._instance


class Singleton(SingletonBase):
    def __new__(cls):
        print("At Child class __new__ : Hello")
        instance = super().__new__(cls)  # Create the instance
        return instance

    def __init__(self):
        print("At Child class __init__ : Hello")
        self.data = "Singleton Data"


# Usage
print("\nCreating instance1\n")
instance1 = Singleton()
print("\nCreating instance2\n")
instance2 = Singleton()

print(instance1 is instance2)  # Output: True
