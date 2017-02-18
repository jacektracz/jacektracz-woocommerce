import sys
import os
import logging

from ... appcore.config.DBG_PrintConfig import *
from ... appcore.logging.DBG_ExceptionPrinter import *

class DBG_LoggerItem:
    def __init__(self,sdbg,sfile):
            self.m_name = ""
            self.logger = logging.getLogger("DBG_LogData")
            self.logger.setLevel(logging.INFO)
            if(sfile == ""):
                self.handler = logging.FileHandler('c:/iastoralog2.txt')
            else:
                self.handler = logging.FileHandler(sfile)
            self.formatter = logging.Formatter('%(message)s')
            self.handler.setFormatter(self.formatter)            
            self.handler.setLevel(logging.INFO)
            self.logger.addHandler(self.handler)

