import sys
import os
import logging
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *

#from DBG_Target import *

from ... appsrc.raidtargets.DBG_EndDeviceTarget import *                
class DBG_PassthroughTarget(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_PassthroughTarget::__init__::in::")
                self.xx_set_class_name ( "PassthroughTarget" )
                self.xx_set_full_class_name ( "iastora!PassthroughTarget" )
                self.m_parent = None
                self.mEndDeviceTarget = DBG_EndDeviceTarget("Parent:DBG_PassthroughTarget")
                #self.m_target = DBG_Target("FROM::DBG_PassthroughTarget")
                self.xx_dbg("DBG_PassthroughTarget::__init__::out::")               
        
        def prepare_object(self):
                self.xx_dbg("DBG_PassthroughTarget::prepare_object::in::")
                if(self.xx_is_object()==1):                        
                        self.mEndDeviceTarget.set_addr(self,"mEndDeviceTarget")
                
                #self.m_target.xx_inc_tabs(self);                
                #self.m_target.xx_compute_arr_phy_by_parent(self,"mTarget")
                self.xx_dbg("DBG_PassthroughTarget::prepare_object::out::")

        def set_parent(self,pparent):
                self.xx_dbg("DBG_PassthroughTarget::set_parent::in::")
                self.m_parent = pparent
                self.xx_dbg("DBG_PassthroughTarget::set_parent::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_PassthroughTarget::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):                        
                        self.mEndDeviceTarget.print_object()
                
                #self.xx_print_ints()
                #self.m_target.print_object()
                self.xx_dbg("DBG_PassthroughTarget::print_object::out::")                