from abc import ABC, abstractmethod


# Step 1: Define the Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying ${amount} using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying ${amount} using PayPal")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paying ${amount} using Bitcoin")


# Step 3: Create the Context
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount: float):
        self._strategy.pay(amount)


# Step 4: Use the Context and Strategies
if __name__ == "__main__":
    # Create a context with an initial strategy
    context = PaymentContext(CreditCardPayment())
    context.execute_payment(100.0)  # Paying $100.0 using Credit Card

    # Change the strategy dynamically
    context.set_strategy(PayPalPayment())
    context.execute_payment(50.0)  # Paying $50.0 using PayPal

    context.set_strategy(BitcoinPayment())
    context.execute_payment(200.0)  # Paying $200.0 using Bitcoin
