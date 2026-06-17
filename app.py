from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("the execution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("the execution has failed")
        raise CustomException(e,sys)