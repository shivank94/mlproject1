from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
from src.mlproject1.components.data_ingestion import DataIngestion
from src.mlproject1.components.data_ingestion import DataIngestionConfig
from src.mlproject1.components.data_transformation import DataTransformationConfig,DataTransformation
import sys


if __name__=="__main__":
    logging.info("the execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_path=train_data_path,test_path=test_data_path)

    except Exception as e:
        logging.info("the execution has failed")
        raise CustomException(e,sys)