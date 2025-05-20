import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # log format

log_dir = "logs"
log_file_path = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level = logging.INFO, # Sets the minimum log level to INFO, so it will log INFO, WARNING, ERROR, CRITICAL messages
    format = logging_str,


    handlers = [
        logging.FileHandler(log_file_path), # writes all log messages
        logging.StreamHandler(sys.stdout) # prints all log messages to the console
    ]
)

logger = logging.getLogger("datasciencelogger")