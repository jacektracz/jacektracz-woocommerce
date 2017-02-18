import sys
import os
from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... apptools.DBG_EnvItemData import *
from ... apptools.DBG_EnvManager import *
from ... appcore.config.DBG_PrintConfig import *        

class DBG_EnvItemPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
        self.m_config = DBG_EnvItemData("")

    def initialize_data_by_selector(self):
        self.xx_dbg( "DBG_EnvItemPrinter::set_parent::method_in::")
        selector = DBG_PrintConfig().getItem().m_env_selector
        tt = DBG_EnvManager("").getData().get_by_selector( selector )
        if(tt != None):
            self.m_config = tt
        self.xx_dbg( "DBG_EnvItemPrinter::set_parent::method_out::")
        
    def set_parent(self, pparent):
        self.xx_dbg( "DBG_EnvItemPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_EnvItemPrinter::set_parent::method_out::")
        
    def set_data(self,dd_env_item):
        self.xx_dbg( "DBG_EnvItemPrinter::set_parent::method_in::")
        self.m_config = dd_env_item
        self.xx_dbg( "DBG_EnvItemPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            
            self.xx_dbg("DBG_StatelPrinter::prepare_object")
            self.m_messages.set_parent(self.m_parent)
            self.m_messages.clear_array()    
            self.add_msg( 'm_sympath',self.m_config.m_sympath)
            self.add_msg( 'm_srcpath', self.m_config.m_srcpath)
            self.add_msg( 'm_selector', self.m_config.m_selector)
            self.add_msg( 'm_load_command', self.m_config.m_load_command)
            self.add_msg( 'm_description', self.m_config.m_description)            
            self.add_msg( 'm_dump', self.m_config.m_dump)
            self.add_msg( 'm_srcpath_full', self.m_config.get_srcpath())
            self.add_msg( 'm_sympath_full', self.m_config.get_sympath())
            vv_info = self.get_msg_info()
            for inf in vv_info:
                self.m_messages.add_message(inf)
            self.xx_dbg("DBG_StatelPrinter::prepare_object")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
        
    def add_msg(self, title,tt):
        try:
            self.m_messages.add_message(str(title) + ":" + str(tt))
        except:
                self.xx_exception("DBG_FieldsMapper::add_msg::exception::")            
        
    def print_object(self):
                try:                        
                        self.print_object_internal()                        
                except:
                        self.xx_exception("DBG_FieldsMapper::print_object")
                
    def print_object_internal(self):
        try:
            self.xx_dbg( "DBG_StatelPrinter::xx_print_link_ptr::method_in::")
            self.m_messages.print_object("environment")
            self.xx_dbg( "DBG_StatelPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
    def get_msg_info(self):
        s_i = [
        "ed kd_storminiport_mask 0xFF"
        ,"ed kd_default_mask 0xFF"

        ,".load D:\lkd\kits\wk\8.1\Debuggers\x64\winext\pykd.pyd"
        
        ,"!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths win7_14"
        ,"!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 14a 20151217_win7_14_2"
        
        ,"!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths win7_15_dev"
        ,"!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ee 15 20151217_win7_15_dmp_1"
        
        ,"!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py ag bp1"        
        
        ,"!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py pths print"

		,"!py D:\lkd\komodo\w2_2\src\w2\rst_windbg_ext.py bugs win7crash bp0"
		
		,".load D:\lkd\kits\wk\dbg7\storkd64.dll"
		
		,".load D:\lkd\3party\BuildLab\10146\Program Files\Windows Kits\10\Debuggers\x64\winext\storagekd.dll"
        ]
        return s_i
