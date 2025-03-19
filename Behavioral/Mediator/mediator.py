from abc import ABC, abstractmethod
from typing import List

# Mediator Interface
class AirTrafficControlTower(ABC):
    @abstractmethod
    def register_aircraft(self, aircraft):
        pass

    @abstractmethod
    def send_message(self, sender, message):
        pass

# Concrete Mediator
class ControlTower(AirTrafficControlTower):
    def __init__(self):
        self._aircrafts: List[Aircraft] = []

    def register_aircraft(self, aircraft):
        self._aircrafts.append(aircraft)
        print(f"Control Tower: {aircraft.name} has entered the airspace.")

    def send_message(self, sender, message):
        for aircraft in self._aircrafts:
            if aircraft != sender:  # Don't send the message back to the sender
                aircraft.receive_message(sender, message)

# Colleague (Aircraft)
class Aircraft:
    def __init__(self, name, control_tower: AirTrafficControlTower):
        self.name = name
        self.control_tower = control_tower
        self.control_tower.register_aircraft(self)

    def send_message(self, message):
        print(f"{self.name} sends: {message}")
        self.control_tower.send_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.name} received from {sender.name}: {message}")

    def request_landing(self):
        print(f"{self.name} requests permission to land.")
        self.control_tower.send_message(self, "Requesting permission to land.")

    def confirm_landing(self):
        print(f"{self.name} confirms landing.")
        self.control_tower.send_message(self, "Landing confirmed.")

# Usage
if __name__ == "__main__":
    # Create the mediator (Control Tower)
    control_tower = ControlTower()

    # Create aircraft (colleagues)
    aircraft1 = Aircraft("Flight 101", control_tower)
    aircraft2 = Aircraft("Flight 202", control_tower)
    aircraft3 = Aircraft("Flight 303", control_tower)

    # Aircraft communicate through the control tower
    aircraft1.send_message("Entering airspace, maintaining altitude.")
    aircraft2.request_landing()
    aircraft3.send_message("Holding position, awaiting instructions.")

    # Simulate landing confirmation
    aircraft2.confirm_landing()