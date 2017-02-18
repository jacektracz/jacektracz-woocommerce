#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by jacek Tracz
#    
#==================================================================
import os
import shutil

from JT_Logger import JT_Logger
from JT_FIND_FilesHelper import JT_FIND_FilesHelper

class JT_MRP_Backtest_data:
    def __init__(self):
        self.m_command = ""
        self.m_file = ""
        
class JT_MRP_Backtest_Manager:
    
    def execute_steps(self):
        print "JT_MRP_Backtest_Manager::execute_steps"
            

    def export_curve_structure(self):
        dd = JT_MRP_Backtest_data()
        dd.m_command = "./startValuationEngine /rksup/config/kgr35jut/ENV_DATA/MRP_BACKTEST/curve_synchron.req"
        
    def historizing_pl(self):
        dd = JT_MRP_Backtest_data()
        dd.m_command = "./rtmBatch -U kplus -P kplusds42 /rksup/config/kgr35jut/ENV_DATA/MRP_BACKTEST/histo_request.xml"
        dd.m_command = "./rtmBatch -U admin -P rknet /rksup/config/kgr35jut/ENV_DATA/MRP_BACKTEST/histo_request.xml"
if __name__ == '__main__':
    dd_manager = JT_MRP_Backtest_Manager()
    


    
