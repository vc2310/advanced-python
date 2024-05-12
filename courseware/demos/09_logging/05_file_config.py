import logging.config

# Configure logging using the configuration file
logging.config.fileConfig("logging_config.ini")

# Create loggers
root_logger = logging.getLogger()
sample_logger = logging.getLogger("sampleLogger")

# Log some messages
root_logger.debug("This is a debug message from the root logger")
sample_logger.info("This is an info message from the sample logger")
