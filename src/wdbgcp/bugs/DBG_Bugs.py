import sys
import os
import logging
from .. .. wdbgc.DBG_AdapterBase import *       
from .. .. wdbgc.helpers.DBG_Utils import *

class DBG_Bugs(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "Driver" )
                self.xx_set_full_class_name ( "iastora!Wcdl::Driver" )
                self.major_version = "";               
                
        def print_object(self):
                self.m_remapport.xx_inc_tabs( self,"DBG_Driver")                
                self.m_remapport.print_object()
                
        def bp_nvme(self):
                DBG_Utils().xx_safe_exe("bp NvmePort::processGetFeaturesIoctl","")
                DBG_Utils().xx_safe_exe("bp iastora!NvmePort::processGetFeaturesIoctl","")
                DBG_Utils().xx_safe_exe("bp SecPortStartIo","")
                DBG_Utils().xx_safe_exe("bp NvmePort::processNvmIoctl","")

        