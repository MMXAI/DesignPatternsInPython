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
            print(f"[INFO]: {message}")
        elif self.next_logger:
            self.next_logger.log(message, severity)

class DebugLogger(Logger):
    def log(self, message, severity):
        if severity <= self.level:
            print(f"[DEBUG]: {message}")
        elif self.next_logger:
            self.next_logger.log(message, severity)

class ErrorLogger(Logger):
    def log(self, message, severity):
        if severity <= self.level:
            print(f"[ERROR]: {message}")
        elif self.next_logger:
            self.next_logger.log(message, severity)

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
    info_logger.log("This is an info message.", severity=1)
    info_logger.log("This is a debug message.", severity=2)
    info_logger.log("This is an error message.", severity=3)
    info_logger.log("This is a critical message.", severity=4)