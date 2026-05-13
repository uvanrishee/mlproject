import os
import sys
from src.exceptions import custom
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import datatransform,datatransformationconfig
@dataclass
class dataingestionconfig:
    train_path:str=os.path.join("artifact","train.csv")
    test_path:str=os.path.join("artifact","test.csv")
    raw_path:str=os.path.join("artifact","raw.csv")

class dataingestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfig()
    def initiate(self):
        logging.info("entered data ingestion")
        try:
            df=pd.read_csv("notebook\\data\\stud.csv")
            logging.info("read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_path,index=False,header=True)
            logging.info("train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_path,index=False,header=True)
            logging.info("ingestion of data is completed.") 

            return(
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
            )


        except Exception as e:
            raise custom(e,sys)

if __name__=="__main__":
    obj=dataingestion()
    train,test=obj.initiate()
    transf=datatransform()
    transf.initiate(train,test)