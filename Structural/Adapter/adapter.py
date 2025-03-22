# Target Interface
class ModernPrinter:
    def print(self):
        pass


# Adaptee
class LegacyPrinter:
    def print_document(self):
        print("Printing document using the legacy printer.")


# Adapter (Object Adapter)
class LegacyPrinterAdapter(ModernPrinter):
    def __init__(self, legacy_printer):
        self.legacy_printer = legacy_printer  # Composition

    def print(self):
        self.legacy_printer.print_document()  # Adapting the call


# Client
if __name__ == "__main__":
    legacy_printer = LegacyPrinter()
    modern_printer = LegacyPrinterAdapter(legacy_printer)
    modern_printer.print()  # Output: Printing document using the legacy printer.
