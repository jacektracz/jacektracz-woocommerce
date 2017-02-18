import sys
import os
import logging
from .. apptools.DBG_ToolsBase import *
from .. apptools.DBG_EnvItemData import *
from .. apptools.DBG_EnvManager import *
import subprocess 
class DBG_CreateEnv(DBG_ToolsBase):
        def __init__(self,spar):                
                DBG_ToolsBase.__init__(self,spar)
                self.xx_set_class_name ( "DBG_CreateEnv" )
                self.xx_set_full_class_name ( "iastora!Wcdl::DBG_CreateEnv" )
                self.m_items = []                

        def create_items(self):
                """ ccc """
                self.m_items = DBG_EnvManager("").getData().get_items()
                
        def crashdump(self, tt):
                #Crashdumptest.exe -c
                #crashdumptest.exe -dtm -y [SymbolsDirectory] -ypass
                #crashdumptest.exe -autorun -y [SymbolsDirectory] -dtm"
                self.xx_call(["Crashdumptest.exe", "-c"])
                self.xx_call(["Crashdumptest.exe", "-c"])

        def create_src(self, tt):
                self.xx_call(["Crashdumptest.exe", "-c"])
                self.xx_call(["Crashdumptest.exe", "-c"])
                
        def xx_call(self,tt):
                subprocess.call(tt)