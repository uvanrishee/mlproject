import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exceptions import custom
def save(path,object):
    try:
        dir_path=os.path.dirname(path)
        os.makedirs(dir_path,exist_ok=True)

        with open(path,'wb') as file:
            dill.dump(object,file)
    except Exception as e:
        raise custom(e,sys)