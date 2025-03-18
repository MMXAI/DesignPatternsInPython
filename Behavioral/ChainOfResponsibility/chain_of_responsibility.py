from abc import ABC, abstractmethod

# Handler interface
class Logger(ABC):
    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next(self, next_logger):
        self.next_logger = next_logger
        return next_logger

    @abstractmethod
    def log(self, message, severity):
        pass

# Concrete Handlers
class InfoLogger(Logger):
    def log(self, message, severity):
        if severity <= self.level:
            print(f"\n[INFO]: {message}\n")
        elif self.next_logger:
            self.next_logger.log(message, severity)
        else:
            print(f"Unknow severity level: {severity}\n")

class DebugLogger(Logger):
    def log(self, message, severity):
        if severity <= self.level:
            print(f"\n[DEBUG]: {message}\n")
        elif self.next_logger:
            self.next_logger.log(message, severity)
        else:
            print(f"Unknow severity level: {severity}\n")

class ErrorLogger(Logger):
    def log(self, message, severity):
        if severity <= self.level:
            print(f"\n[ERROR]: {message}\n")
        elif self.next_logger:
            self.next_logger.log(message, severity)
        else:
            print(f"Unknow severity level: {severity}\n")

# Client
if __name__ == "__main__":
    # Create the chain of loggers
    info_logger = InfoLogger(level=1)
    debug_logger = DebugLogger(level=2)
    error_logger = ErrorLogger(level=3)

    info_logger\
        .set_next(debug_logger)\
        .set_next(error_logger)

    # Send messages with different severity levels
    for i in range(1, 7):
        info_logger.log(f"This is a message with severity {i}.", severity=i)
