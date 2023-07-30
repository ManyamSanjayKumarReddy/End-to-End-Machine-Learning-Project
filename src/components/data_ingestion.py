import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('articafts', "train.csv")
    test_data_path : str=os.path.join('articafts', "test.csv")
    raw_data_path : str=os.path.join('articafts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_congif = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered into data Ingestion Method or Component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            # makedir() is used for single directory but makedirs() used for creating all the intermediate directories
            os.makedirs(os.path.dirname(self.ingestion_congif.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_congif.test_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_congif.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_congif.raw_data_path, index=False, header=True)

            logging.info("Train test spplit-up initiated")
            train_set, test_set = train_test_split(df, test_size=20, random_state=51)

            train_set.to_csv(self.ingestion_congif.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_congif.test_data_path, index=False, header=True)

            logging.info("Data Ingestion Part has Completed")

            return(

                self.ingestion_congif.train_data_path,
                self.ingestion_congif.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
            


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()