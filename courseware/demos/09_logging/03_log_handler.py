# type: ignore

import logging


# Create a custom log handler
class MyLogHandler(logging.Handler):
    def emit(self, record):
        # Customize how log messages are handled
        log_entry = self.format(record)
        with open("my_custom_log.log", "a") as log_file:
            log_file.write(log_entry + "\n")


# Configure the logging settings
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Create an instance of the custom log handler
my_handler = MyLogHandler()

# Add the custom log handler to the root logger
root_logger = logging.getLogger()
root_logger.addHandler(my_handler)

# Log some messages
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")

# Remove the custom log handler (optional)
root_logger.removeHandler(my_handler)
