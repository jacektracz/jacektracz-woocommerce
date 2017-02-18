
import sys
import os
from .. appcore.memory.DBG_Utils import *
from .. appcore.memory.DBG_MemoryTools import *
from .. fields.DBG_FieldsMapper import *
from .. remapport.DBG_Transport import *
from .. ahci.DBG_AhciController import *
from .. nvme.DBG_NvmePort import *
from .. DBG_AdapterBase import *
from .. appcore.config.DBG_PrintConfig import *

class DBG_Transports_Glob_Array(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_Transports_Glob_Array::__init__::method_in::")
                self.xx_set_class_name ( "remapport" )
                self.xx_set_full_class_name ( "iastora!remapport" )                
                self.m_parent = None
                self.m_range = 64
                self.m_transports = []
                self.m_fields = DBG_FieldsMapper("DBG_Transports_Glob_Array"
                                         ,self)
                
                self.xx_dbg("DBG_Transports_Glob_Array::__init__::method_out::")       
                
        def set_parent(self,pparent):
                self.xx_dbg("DBG_Transports_Glob_Array::set_parent::")
                self.m_parent = pparent
                self.xx_dbg("DBG_Transports_Glob_Array::set_parent::out")
                
        def prepare_object(self,pparent):
                try:
                        self.prepare_object_internal(pparent)                                
                except:
                        self.xx_exception("DBG_Transports_Glob_Array::print_object")
                                        
        def prepare_object_internal(self,pparent):
                self.xx_dbg("DBG_Transports_Glob_Array::initialize_ptr::")
                self.clear_messages()
                self.m_parent = pparent
                self.m_transports= []
                
                handled_paths = self.m_range
                
                if (DBG_PrintConfig().getItem().m_handle_transport_paths == 0):
                        handled_paths = 1
                        
                self.dbg_loc_hard("handled_paths:" + str(handled_paths))
                
                for ii_path in range(handled_paths):
                        if (self.path_in_range(ii_path) == 0):
                                self.dbg_loc_hard_if("path_not_handled:" + str(ii_path))
                                continue
                        else:
                                self.dbg_loc_hard("path_handled:" + str(ii_path))
                                
                        dd = DBG_Transport("DBG_Transports_Glob_Array")
                        dd.set_transport_idx(ii_path)
                        dd.xx_inc_tabs_ex( self.m_parent,2,"DBG_Transports_Glob_Array")                        
                        dd.xx_set_lg_compute_phy_addr("mTransport[" +str(ii_path) + "]")
                        dd.prepare_object()
                        self.m_transports.append(dd)
                self.xx_dbg("DBG_Transports_Glob_Array::initialize_ptr::out")
                
        def print_object(self):
                try:
                        self.xx_print_start()
                        self.print_object_internal()
                        self.xx_print_end()
                except:
                        self.xx_exception("DBG_Transports_Glob_Array::print_object")
                        
        def print_object_internal(self):                
                self.xx_dbg("DBG_Transports_Glob_Array::print_object::")
                
                self.xx_print_ptr("")
                self.print_transports()                
                self.xx_dbg("DBG_Transports_Glob_Array::print_object::out")

        def print_transports(self):
                self.xx_dbg("DBG_Transports_Glob_Array::print_transports::")
                print_all = DBG_PrintConfig().getItem().m_print_all_remap_transports
                ii = 0
                for dd_transport in self.m_transports:
                        if(dd_transport.mTransportOn != 0 or print_all == 1 ):
                                dd_transport.print_object()                                
                        self.add_message("Transport[" + str(ii) + "].mTransportOn = " + str(dd_transport.mTransportOn))
                        ii = ii +1
                        
                self.xx_dbg("DBG_Transports_Glob_Array::print_transports::out::")
                
        def path_in_range(self,p_ii):                
                return DBG_PrintConfig().getItem().path_in_range(p_ii)

        def dbg_loc_hard(self,tt):                
                print tt
                
        def dbg_loc_hard_if(self,tt):
                self.xx_dbg("DBG_Transports_Glob_Array::dbg_loc_hard_if::in::")
                self.xx_dbg("DBG_Transports_Glob_Array::dbg_loc_hard_if::out::")
                #print tt
