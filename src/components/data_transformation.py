import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.logger import logging
from src.exceptions import custom
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from src.utils import save
import os
@dataclass
class datatransformationconfig:
    preprocessorfilepath=os.path.join("artifact","preprocessor.pkl")

class datatransform:
    def __init__(self):
        self.config=datatransformationconfig()
    def get_transform(self):
        try:
            num_col=['reading_score', 'writing_score']
            cat_col=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info("categorical columns ecoding completed")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,num_col),
                    ("cat_pipeline",cat_pipeline,cat_col)
                ]
            )

            return preprocessor
        except Exception as e:
            raise custom(e,sys)
    
    def initiate(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data")
            logging.info("obtaining preprocessor object")

            obj=self.get_transform()
            target_col='math_score'

            input_train=train_df.drop(columns=["math_score"],axis=1)
            target_train=train_df['math_score']

            
            input_test=test_df.drop(columns=["math_score"],axis=1)
            target_test=test_df['math_score']
            
            logging.info("spit target and input features")

            input_feature_train_arr=obj.fit_transform(input_train)
            input_feature_test_arr=obj.transform(input_test)

            train_arr=np.c_[input_feature_train_arr,np.array(target_train)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_test)] 
            logging.info("preprocessor completed")

            save(path=self.config.preprocessorfilepath
                 ,object=obj)
            
            return(train_arr,test_arr,self.config.preprocessorfilepath)
        except Exception as e:
            raise custom(e,sys)