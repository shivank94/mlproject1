from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
from src.mlproject1.components.data_ingestion import DataIngestion
from src.mlproject1.components.data_ingestion import DataIngestionConfig
import sys


if __name__=="__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("the execution has failed")
        raise CustomException(e,sys)