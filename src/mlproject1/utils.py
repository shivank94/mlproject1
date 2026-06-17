import os
import sys
from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql


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