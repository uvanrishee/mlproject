import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()#provides info about while file and line error has occured
    file_name=exc_tb.tb_frame.f_code.co_filename#refer documentation
    mess="error in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return mess

class custom(Exception):
    def __init__(self,mess,error_detail:sys):
        super().__init__(mess)
        self.error_message=error_message_detail(mess,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

