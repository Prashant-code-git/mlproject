from logger import logging
from exception import CustomeException
import sys

if __name__ == "__main__":
    logging.info("The exectution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custm Exception")
        raise CustomeException(e,sys)    
