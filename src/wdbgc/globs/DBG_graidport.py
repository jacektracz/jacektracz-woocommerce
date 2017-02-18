import sys
import os

from .. DBG_AdapterBase import *
from .. raidport.DBG_Raidport import * 
        
class DBG_graidport(DBG_AdapterBase):

    def __init__(self,spar):                
        DBG_AdapterBase.__init__(self,spar)
        self.xx_set_class_name( "Raidport" )
        self.xx_set_full_class_name ( "iastora!Raidport" )
        self.xx_set_tabs(1,"DBG_Raidport")        						
        self.m_raidport = DBG_Raidport("FROM:DBG_Raidport")
        

    def prepare_object(self):
        self.xx_set_lg_compute_phy_addr( "iastora!g_raidport" )                
        self.m_raidport.set_addr_arr(self,"SELF")
    
    def print_object(self):        
        self.prepare_object()
        self.xx_print_ptr("")        
        self.m_raidport.print_object()
