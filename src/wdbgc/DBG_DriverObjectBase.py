import sys

from DBG_MemoryPtr import *
from appcore.memory.DBG_Utils import *

class DBG_DriverObjectBase(DBG_MemoryPtr):
    def __init__(self,spar):
        DBG_MemoryPtr.__init__(self,spar)
        self.xx_dbg("DBG_DriverObjectBase:in::")        
        self.xx_dbg("DBG_DriverObjectBase:out::")
        
    def xx_print_link(self):
        try:
            self.xx_dbg("DBG_DriverObjectBase::xx_print_link::")        
            #s_e = "@@C++(" + self.m_logical_ptr + ")"
            #self.tt.xx_link(self.m_tabs,"?? " + s_e ,self.m_class_desc)                        
        except:
            self.xx_exception("DBG_DriverObjectBase::xx_print_link::exception::")
            
    def xx_disp_adapter(self):
        try:
            self.xx_dbg("DBG_DriverObjectBase::xx_disp_adapter::in::")
            DBG_Utils().xx_safe_exe("!storagekd.storadapter " + self.xx_get_phy_addr("") + "","xx_dips_adapter")
            self.xx_dbg("DBG_DriverObjectBase::xx_disp_adapter::out::")
        except:
            self.xx_exception("DBG_DriverObjectBase::xx_print_link::exception::")
    
    def xx_disp_unit(self):
        try:
            DBG_Utils().xx_safe_exe("!storagekd.storunit " + self.xx_get_phy_addr("") + "","xx_dips_unit")
        except:
            self.xx_exception("DBG_DriverObjectBase::xx_print_link::exception::")
            
    def xx_disp_storloglist(self):
        try:
            self.xx_dbg("DBG_DriverObjectBase::xx_disp_storloglist")
            DBG_Utils().xx_safe_exe("!storagekd.storloglist " + self.xx_get_phy_addr("") + " 0 200 100",'SRB')
            self.xx_dbg("DBG_DriverObjectBase::xx_disp_storloglist::out::")
        except:
            self.xx_exception("DBG_DriverObjectBase::xx_print_link::exception::")

