# type: ignore

import logging


# Create a custom log formatter
class MyLogFormatter(logging.Formatter):
    def format(self, record):
        # Customize the format of log messages
        log_entry = f"[{record.levelname}] {record.message}"
        return log_entry


# Create a custom log handler
class MyLogHandler(logging.Handler):
    def emit(self, record):
        # Customize how log messages are handled
        log_entry = self.format(record)
        with open("my_custom_log.log", "a") as log_file:
            log_file.write(log_entry + "\n")


# Configure the logging settings
logging.basicConfig(level=logging.INFO)

# Create an instance of the custom log formatter
my_formatter = MyLogFormatter()

# Create an instance of the custom log handler
my_handler = MyLogHandler()

# Set the custom formatter for the custom handler
my_handler.setFormatter(my_formatter)

# Get the root logger and add the custom log handler
root_logger = logging.getLogger()
root_logger.addHandler(my_handler)

# Log some messages
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
