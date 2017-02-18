import sys
import os

from ... appcore.printers.DBG_Base import *
from ... appcore.printers.DBG_FieldInfos import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.htmlwriters.DBG_Html import *
from ... appcore.memory.DBG_Utils import *
class DBG_ConfigHtmlPrinter(DBG_Base):
    def __init__(self,pparent,sdbg):
        DBG_Base.__init__(self,pparent,sdbg)
        self.m_parent = pparent
        self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)
        self.m_config = None
        
    def set_parent(self,pparent):
        self.xx_dbg( "DBG_ConfigHtmlPrinter::set_parent::method_in::")
        self.m_parent = pparent
        self.xx_dbg( "DBG_ConfigHtmlPrinter::set_parent::method_out::")
        
    def prepare_object(self):
        try:
            
            self.xx_dbg("DBG_StatelPrinter::prepare_object")
            self.m_config = DBG_PrintConfig().getItem()
            self.m_messages.set_parent(self.m_parent)
            self.m_messages.clear_array()    
            self.add_msg( 'm_out_file_name',self.m_config.m_out_file_name)
            self.add_msg( 'm_version', self.m_config.m_version)
            self.add_msg( 'm_version_1', self.m_config.m_version_1)
            self.add_msg( 'm_version_2', self.m_config.m_version_2)
            self.add_msg( 'm_version_3', self.m_config.m_version_3)
            self.add_msg( 'm_log_all_errors',self.m_config.m_log_all_errors)
            self.add_msg( 'm_exit_on_exception',self.m_config.m_exit_on_exception)
            self.add_msg( 'm_system_target',self.m_config.m_system_target)					
            self.add_msg( 'm_root_dir',self.m_config.m_root_dir)
            self.add_msg( 'm_prefix',self.m_config.m_prefix)
            self.add_msg( 'm_file',self.m_config.m_file)					
            self.add_msg( 'm_raid_targets_arr',self.m_config.m_raid_targets_arr)                        
            self.add_msg( 'm_store_errors',self.m_config.m_store_errors)
            self.add_msg( 'm_max_g_stored_errors',self.m_config.m_max_g_stored_errors)
            self.add_msg( 'm_max_obj_stored_errors',self.m_config.m_max_obj_stored_errors)
            self.add_msg( 'm_print_all_targets',self.m_config.m_print_all_targets)
            self.add_msg( 'm_dbg_all',self.m_config.m_dbg_all)
            self.add_msg( 'm_is_inbox',self.m_config.m_is_inbox)
            self.add_msg( 'm_is_dump',self.m_config.m_is_dump)
            self.add_msg( 'm_dbg_printer',str(self.m_config.m_dbg_printer))
            self.add_msg( 'm_handle_info',str(self.m_config.m_handle_info))
            self.add_msg( 'm_handle_env',str(self.m_config.m_handle_env))
            self.add_msg( 'm_handle_exc',str(self.m_config.m_handle_exc))
            self.print_threads()
            self.print_paths()
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
            self.m_messages.print_object("config")
            self.xx_dbg( "DBG_StatelPrinter::xx_print_link_ptr::method_in::")
        except:
            self.xx_exception("xx_print_link_ptr::exception::")
            
    def print_threads(self):
        try:
            """ """
            s_thread = DBG_Utils().get_thread_id()
            self.add_msg( 's_thread',s_thread)
        except:
            self.xx_exception("print_threads::exception::")
          
    def print_paths(self):
        try:
            """ """
            
            vv_paths = DBG_Utils().get_paths()
            if(len(vv_paths) > 0):
                self.add_msg( 'sympath',vv_paths[0])
                
            if(len(vv_paths) > 1):                
                self.add_msg( 'srcpath',vv_paths[1])
                
        except:
            self.xx_exception("print_threads::exception::")                    