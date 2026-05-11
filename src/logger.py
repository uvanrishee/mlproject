import logging
import os
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(path,exist_ok=True)

LOG_FILE_PATH=os.path.join(path,log_file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

