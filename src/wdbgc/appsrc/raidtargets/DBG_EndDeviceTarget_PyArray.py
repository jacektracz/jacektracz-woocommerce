import sys
import os
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appcore.logging.DBG_Log import *
from ... appsrc.raidtargets.DBG_EndDeviceTarget import *
from ... fields.DBG_FieldsMapper import *
from ... appcore.config.DBG_PrintConfig import *

class DBG_EndDeviceTarget_PyArray(DBG_AdapterBase):
        def __init__(self,spar,pparent):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "TransportPath" )
                self.xx_set_full_class_name ( "iastora!TransportPath" )
                self.m_array_item = []                
                self.mNumTargets = 0
                self.mNumLuns = 0
                self.m_fields = DBG_FieldsMapper("DBG_EndDeviceTarget_PyArray"
                                         , self)
                self.m_target_info = DBG_FieldsMapper("DBG_EndDeviceTarget_PyArray"
                                         , self)
                self.m_target_info.m_tag = "target_info"
                self.m_items_count = 0
        
        def get_items_count(self):
                return self.m_items_count
                
        def set_parent(self):
                self.xx_dbg("DBG_EndDeviceTarget_PyArray::set_parent::in")
                self.m_parent = pparent
                self.xx_dbg("DBG_EndDeviceTarget_PyArray::set_parent::out")

                
        def set_range(self,i_targets,i_luns):
                self.xx_dbg("DBG_EndDeviceTarget_PyArray::set_range::in")
                self.mNumTargets = i_targets
                self.mNumLuns = i_luns
                self.xx_dbg("DBG_EndDeviceTarget_PyArray::set_range::out")
                
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::prepare_object::in::")
                        self.clear_messages()
                        self.m_fields.initialize_by_parent(self.m_parent)
                        self.m_target_info.initialize_by_parent(self.m_parent)
                        self.prepare_targets()
                        self.count_targets()
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::prepare_object::out::")
                except:
                        self.xx_exception("DBG_EndDeviceTarget_PyArray::prepare_object::exception")
                
        
        def prepare_targets(self):
                self.xx_dbg("DBG_EndDeviceTarget_PyArray::prepare_targets::in::")
                
                self.m_array_item = []
                for i_target in range(self.mNumTargets):                                                
                        for j_lun in range(self.mNumLuns):
                                self.x_dbg("DBG_EndDeviceTarget_PyArray::prepare_target::in::")
                                ddt = self.create_target(self.m_parent, i_target, j_lun)
                                if(ddt != None ):
                                        self.m_array_item.append(ddt)                                                                        
                        
                self.x_dbg("DBG_EndDeviceTarget_PyArray::prepare_targets::out::")
                                                
        
        def create_target(self, pparent, ptarget,plun):
                try:
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::prepare_object::method_in::")
                        
                        dd_target = DBG_EndDeviceTarget("Parent::DBG_EndDeviceTarget_PyArray")
                        sadr = ""                                                
                        if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                                sadr = "mTargetArray[" + str(ptarget) + "]["  + str(plun) + "]"
                                dd_target.set_addr(pparent,sadr)
                                dd_target.prepare_object()                                
                        else:
                                sadr = "mTargetArray[" + str(ptarget) + "]"
                                dd_target.set_addr(pparent,sadr)
                                dd_target.prepare_object()
                                                        
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::prepare_object::method_out::")
                        return dd_target
                except:
                        self.xx_exception("DBG_EndDeviceTarget_PyArray::create_target")
                        return None

        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_object::in::")
                
                self.prepare_object()
                self.xx_print_ptr("")
                
                if(self.xx_is_object() ==1 ):
                        self.m_fields.print_object()
                        self.print_targets()
                        self.m_target_info.print_object()
                        
                self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_object::out::")

        def print_targets(self):
                try:
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_targets::in::")
                        
                        for dd_target in self.m_array_item:
                                self.print_target(dd_target)
                                                                        
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_targets::out::")
                except:
                        self.xx_exception("DBG_EndDeviceTarget_PyArray::print_targets::excpetion")

        def count_targets(self):
                try:
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_targets::in::")                        
                        for dd_target in self.m_array_item:
                                if(dd_target.xx_is_object()==1):
                                        self.m_items_count = self.m_items_count + 1
               
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_targets::out::")
                except:
                        self.xx_exception("DBG_EndDeviceTarget_PyArray::print_targets::excpetion")

        def print_target(self, dd_target):
                try:
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_target::in::")
                        if(dd_target.xx_is_object()==1):                                
                                dd_target.print_object()
                                if(dd_target.is_raidtarget_attached()):
                                        self.m_target_info.add_raw_str("Target_has_raidtarget:" + dd_target.m_lg_ptr)
                                
                        self.xx_dbg("DBG_EndDeviceTarget_PyArray::print_target::out::")
                except:
                        self.xx_exception("DBG_EndDeviceTarget_PyArray::print_target::excpetion")
