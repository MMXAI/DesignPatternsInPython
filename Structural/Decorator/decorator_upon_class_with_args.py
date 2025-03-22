# Parameterized class-based decorator
class DynamicEnhancer:
    def __init__(self, *, inject_greet=False, override_str=False):
        self.inject_greet = inject_greet
        self.override_str = override_str

    def __call__(self, cls):
        # Inject greet method if requested
        if self.inject_greet:

            def greet(self):
                print(f"Hi there! I'm {self.value}")

            setattr(cls, "greet", greet)

        # Override __str__ if requested
        if self.override_str:

            def custom_str(self):
                return f"CustomStr -> value: {self.value}"

            setattr(cls, "__str__", custom_str)

        return cls


# Apply decorator WITH arguments
@DynamicEnhancer(inject_greet=True, override_str=True)
class MyClass:
    def __init__(self, value):
        self.value = value


# Usage
obj = MyClass(10)
obj.greet()  # --> Hi there! I'm 10
print(obj)  # --> CustomStr -> value: 10
