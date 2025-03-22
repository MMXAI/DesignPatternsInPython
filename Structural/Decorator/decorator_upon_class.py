# Class-based decorator to inject and override methods
class EnhanceClassDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.inject_methods()
        self.override_methods()

    def inject_methods(self):
        # Inject new method 1
        def greet(self):
            print(f"Hello! My value is: {self.value}")
        
        # Inject new method 2
        def double_value(self):
            return self.value * 2
        
        setattr(self.cls, 'greet', greet)
        setattr(self.cls, 'double_value', double_value)

    def override_methods(self):
        # Save original method
        original_str = self.cls.__str__ if hasattr(self.cls, '__str__') else lambda self: super(self.cls, self).__str__()

        # Define new __str__ method
        def new_str(self):
            return f"MyClass instance with value={self.value}"

        setattr(self.cls, '__str__', new_str)
        setattr(self.cls, '__original_str__', original_str)  # Optional: Keep access to original

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)

# Target class
@EnhanceClassDecorator
class MyClass:
    def __init__(self, value):
        self.value = value

# Usage
obj = MyClass(50)

# Injected methods
obj.greet()  # --> Hello! My value is: 50
print(obj.double_value())  # --> 100

# Overridden method
print(obj)  # --> MyClass instance with value=50
