import logging
import os # used to create, accessing and storing data in directory
from datetime import datetime

LOGS_DIR="logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE=os.path.join(LOGS_DIR,f"{datetime.now().strftime('%m_%d_%Y')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, ## If level set as INFO, then logs that levels INFO and above INFO will be displayed. Above INFO we have 2 levels those are ERROR and WARNING
)

def get_logger(name): # function used to initialize loggers in different files
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger