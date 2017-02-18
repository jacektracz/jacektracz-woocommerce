#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by jacek Tracz
#    
#==================================================================
import os
import shutil

from JT_Logger import JT_Logger

from JT_FIND_FilesHelper import JT_FIND_FilesHelper

class JT_MRP_Scenario_Data:
    def __init__(self):
        self.m_horizon = ""
        self.m_scenarios = ""
        self.m_name = ""

class JT_MRP_Deal_Data:
    def __init__(self):
        self.m_type = ""
        self.m_kp = ""
        self.m_kgr = ""
        self.m_time_stamp = ""
        self.m_folder = ""
        self.m_cpty = ""
        self.m_case = ""
        
    @staticmethod
    def get_deal(
        p_type
        ,p_kp
        ,p_kgr
        ,p_time_stamp
        ,p_folder
        ,p_cpty
        ,p_case):
                
        dd =  JT_MRP_Deal_Data()
        dd.m_type = p_type        
        dd.m_kp = p_kp
        dd.m_kgr = p_kgr
        dd.m_time_stamp = p_time_stamp
        dd.m_folder = p_folder
        dd.m_cpty = p_cpty
        dd.m_case = p_case
        return dd

        
    def create_deal(
        self
        , p_type
        , p_kp
        , p_kgr
        , p_time_stamp):
        self.m_type = p_type        
        self.m_kp = p_kp
        self.m_kgr = p_kgr
        self.m_time_stamp = p_time_stamp

class JT_MRP_Environment_Data:
    def __init__(self):
        self.m_filter = ""
        self.m_setup = ""
        self.m_pl_bck_set = ""        
        self.m_deals = []
        self.m_scenario = ""
        self.m_date = ""
        self.m_type = ""
        self.m_case = ""
        self.m_df_string = ""
        self.m_observations = 10
        self.m_historical_dates = []
        self.m_risc_classes = []
        self.m_mrp_scenarios = []
        
class JT_MRP_Environment_Manager:
    
    def __init__(self):
        self.m_env = []
        
    def create_envs(self):
        
        self.m_env.append(JT_MRP_Environment_Manager.get_env("JT-IAM-HIST-2"
                                                     ,  "JT-IAM-H-10-18"
                                                     ,  ""
                                                     ,  ""
                                                     ,  ""
                                                     ,  "16/01/2014"
                                                     ,  "MRP-BACKTEST"
                                                     ,  "BACKTEST_FOLDERS_WITH_AGGREGATION"))
        
        self.m_env.append(JT_MRP_Environment_Manager.get_env("JT-IAM-HIST-2"
                                                     ,  "JT-IAM-H-10-16"
                                                     ,  ""
                                                     ,  ""
                                                     ,  ""
                                                     ,  "16/01/2014"
                                                     ,  "MRP-BACKTEST"
                                                     , "BACKTEST_FOLDERS"))
        
        self.m_env.append(JT_MRP_Environment_Manager.get_env("JT-B-IAM-2"
                                                     ,"JT-IAM"
                                                     ,"JT-B-IAM-2-2" #JT-B-IAM-2-4
                                                     ,""
                                                     ,""
                                                     ,"16/01/2014"
                                                     ,"MRP-BACKTEST"
                                                     ,""))

        self.m_env.append(JT_MRP_Environment_Manager.get_env("KJ-BACK"
                                                     ,"KJ-IAM"
                                                     ,"KJ-BACK"
                                                     ,""
                                                     ,""
                                                     ,"16/01/2014"
                                                     ,"MRP-BACKTEST"
                                                     ,""))

        self.m_env.append(JT_MRP_Environment_Manager.get_env("XAD-PFE-CDS"
                                                     ,"XAD-PFE-CDS"
                                                     ,"XAD-PFE-CDS"
                                                     ,"CDS:574"
                                                     ,"XAD-PFE-13"
                                                     ,"04/07/2013"
                                                     ,"MRP"
                                                     ,""))
    def print_mrp(self):
        for ii_deal in self.m_env:
            print "MRP_START:"            
            print "SETUP:" + ii_deal.m_setup
            print "FILTER:" + ii_deal.m_filter
            print "PL_SET:" + ii_deal.m_pl_bck_set
            print "DATE:" + ii_deal.m_date
            print "MRP_END:"

        

        
    @staticmethod
    def get_backtest_1():
        dd =  JT_MRP_Environment_Data()
        dd.m_setup = "JT-B-IAM-2"        
        dd.m_filter = "JT-IAM"
        dd.m_pl_bck_set = "JT-B-IAM-2-6"
        dd.m_scenario = ""
        dd.m_date = "13-01-2014"
        dd.m_type = "Backtest"
        dd.m_case = "backtest folder"
        dd.m_observations = 2
        return dd
    @staticmethod
    
    def get_backtest_JT_B_IAM_2_8():
        dd =  JT_MRP_Environment_Data()
        dd.m_setup = "JT-B-IAM-2"        
        dd.m_filter = "JT-IAM"
        dd.m_pl_bck_set = "JT-B-IAM-2-8"
        dd.m_scenario = ""
        dd.m_date = "16-01-2014"
        dd.m_type = "Backtest"
        dd.m_case = "backtest folder"
        dd.m_observations = 4
        dd.m_df_string ="(Folders EQUALS KJ-TEST1) AND (((TypeOfDeal EQUALS IamDeals) AND (DealStatus EQUALS Real)) )"        
        return dd

    def get_backtest_JT_B_IAM_2_10():
        dd =  JT_MRP_Environment_Data()
        dd.m_setup = "JT-B-IAM-2"        
        dd.m_filter = "JT-IAM"
        dd.m_pl_bck_set = "JT-B-IAM-2-10"
        dd.m_scenario = ""
        dd.m_date = "16-01-2014"
        dd.m_type = "Backtest"
        dd.m_case = "backtest folder"
        dd.m_observations = 10
        dd.m_df_string ="(Folders EQUALS KJ-TEST1) AND (((TypeOfDeal EQUALS IamDeals) AND (DealStatus EQUALS Real)) )"
        
        d1= JT_MRP_Deal_Data()
        d1.m_time_stamp =  "IAM:12709641"
        d1.m_kp = "DS42"        
        dd.m_deals.append( d1 )        
        return dd
        
    def get_backtest_JT_IAM_HIST_2():
        dd =  JT_MRP_Environment_Data()
        dd.m_setup = "JT-IAM-HIST-2"        
        dd.m_filter = "JT-IAM"
        dd.m_pl_bck_set = "JT-B-IAM-10-18"
        dd.m_scenario = "JT-IAM-H-2"
        dd.m_historical_dates = ["16-01-2014","15-01-2014","14-01-2014"]
        dd.m_risk_classes = ["FX","IR","TOTAL"]
        dd.m_type = "historical"
        dd.m_case = "backtest folder"
        dd.m_observations = 10
        dd.m_df_string ="(Folders EQUALS KJ-TEST1) AND (((TypeOfDeal EQUALS IamDeals) AND (DealStatus EQUALS Real)) )"
        
        d1 = JT_MRP_Deal_Data()
        d1.m_time_stamp =  "IAM:12709641"
        d1.m_kp = "DS42"
        dd.m_deals.append( d1 )    
        
        dd_s = JT_MRP_Scenario_Data()
        dd_s.m_name ="JT-IAM-H-2"
        dd_s.m_scenarios = 10
        dd_s.m_horizon = 1         
        
        dd.m_mrp_scenarios.append(dd_s)    
        return dd
        
    @staticmethod
    def get_env(
        p_setup
        ,p_filter
        ,p_pl
        ,p_deal
        ,p_scenario
        ,p_date
        ,p_type
        ,p_case):                
        dd =  JT_MRP_Environment_Data()
        dd.m_setup = p_setup        
        dd.m_filter = p_filter
        dd.m_pl_bck_set = p_pl
        dd.m_pl_hist_set = p_pl
        dd.m_scenario = p_scenario
        dd.m_date = p_date
        dd.m_type = p_type
        dd.m_case = p_case        
        return dd
            
class JT_MRP_Deals:
    def __init__(self):
        self.m_deals = []
        
    def create_deals(self):
        self.m_deals.append(JT_MRP_Deal_Data.get_deal("IAM"
                                                 ,"DS42"
                                                 ,"PERKUN"
                                                 ,"IAM:12709643"
                                                 ,"JT-B4"
                                                 ,"JT-A1"
                                                 ,"ZCASE_01187603_MRP_BACKTEST_FOLDER_GROUP"))

    def print_deals(self):
        for ii_deal in self.m_deals:            
            print "TIME:" + ii_deal.m_time_stamp
            print "TYPE:" + ii_deal.m_type
            print "KGR:" + ii_deal.m_kgr
            print "KP:" + ii_deal.m_kp
            print "FOLDER:" + ii_deal.m_folder
            print "CASE:" + ii_deal.m_case
            print "CPTY:" +ii_deal.m_cpty

            

if __name__ == '__main__':
    print "start exec ..."
    dd_deals = JT_MRP_Deals()
    dd_deals.create_deals()
    dd_deals.print_deals()
    
    dd_mrp = JT_MRP_Environment_Manager()
    dd_mrp.create_envs()
    dd_mrp.print_mrp()
    
    print "all done ..."


    
