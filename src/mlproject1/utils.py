import os
import sys
from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

import pickle
import numpy as np


load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(host=host, 
                               user=user, 
                               password=password, 
                               database=db)
        logging.info("Connection to SQL database successful", mydb)
        df=pd.read_sql('SELECT * FROM student', con=mydb)
        print(df.head())

        return df
    except Exception as e:
        logging.info("Exception occurred while reading SQL database")
        raise CustomException(e,sys)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)