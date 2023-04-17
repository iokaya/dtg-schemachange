import logging
from logging.handlers import RotatingFileHandler
import sys

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

# Create rotating file handler
log_file = './logs/monitor.log'
file_handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=2)
file_handler.setFormatter(formatter)

# Create console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Get root logger and add handlers
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
