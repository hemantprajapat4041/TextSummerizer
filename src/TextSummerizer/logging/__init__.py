import os 
import sys
import logging

logdir = "logs"
logging_str="%(asctime)s - %(levelname)s - %(message)s"

log_filepath=os.path.join(logdir,"continuous_logs.log")

os.makedirs(logdir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("textSummarizer")