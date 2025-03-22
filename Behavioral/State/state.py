# State interface
class VendingMachineState:
    def insert_coin(self, machine):
        pass

    def select_item(self, machine):
        pass

    def dispense_item(self, machine):
        pass


# Concrete States
class NoCoinState(VendingMachineState):
    def insert_coin(self, machine):
        print("Coin inserted.")
        machine.set_state(HasCoinState())

    def select_item(self, machine):
        print("Please insert a coin first.")

    def dispense_item(self, machine):
        print("Please insert a coin first.")


class HasCoinState(VendingMachineState):
    def insert_coin(self, machine):
        print("Coin already inserted.")

    def select_item(self, machine):
        if machine.item_count > 0:
            print("Item selected. Preparing to dispense.")
            machine.set_state(DispensingState())
        else:
            print("Item out of stock.")
            machine.set_state(OutOfStockState())

    def dispense_item(self, machine):
        print("Please select an item first.")


class DispensingState(VendingMachineState):
    def insert_coin(self, machine):
        print("Please wait, item is being dispensed.")

    def select_item(self, machine):
        print("Please wait, item is being dispensed.")

    def dispense_item(self, machine):
        print("Item dispensed.")
        machine.item_count -= 1
        if machine.item_count > 0:
            machine.set_state(NoCoinState())
        else:
            machine.set_state(OutOfStockState())


class OutOfStockState(VendingMachineState):
    def insert_coin(self, machine):
        print("Machine is out of stock. Cannot accept coins.")

    def select_item(self, machine):
        print("Machine is out of stock. No items available.")

    def dispense_item(self, machine):
        print("Machine is out of stock. No items to dispense.")


# Context
class VendingMachine:
    def __init__(self, item_count):
        self.item_count = item_count
        self._state = NoCoinState()  # Initial state

    def set_state(self, state):
        self._state = state

    def insert_coin(self):
        self._state.insert_coin(self)

    def select_item(self):
        self._state.select_item(self)

    def dispense_item(self):
        self._state.dispense_item(self)


# Client code
if __name__ == "__main__":
    vending_machine = VendingMachine(item_count=2)  # Vending machine with 2 items

    vending_machine.insert_coin()  # Coin inserted.
    vending_machine.insert_coin()  # Coin already inserted.
    vending_machine.select_item()  # Item selected. Preparing to dispense.
    vending_machine.insert_coin()  # Please wait, item is being dispensed.
    vending_machine.dispense_item()  # Item dispensed.

    vending_machine.insert_coin()  # Coin inserted.
    vending_machine.select_item()  # Item selected. Preparing to dispense.
    vending_machine.dispense_item()  # Item dispensed.

    vending_machine.insert_coin()  # Machine is out of stock. Cannot accept coins.
    vending_machine.select_item()  # Machine is out of stock. No items available.
    vending_machine.dispense_item()  # Machine is out of stock. No items to dispense.
