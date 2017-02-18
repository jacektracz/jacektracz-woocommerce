import sys
import os
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appcore.logging.DBG_Log import *
from ... appsrc.raidtargets.DBG_RaidportTargetsPath import *
from ... appsrc.raidtargets.DBG_RaidportTarget_PyManager import *
from ... appcore.config.DBG_PrintConfig import *
from ... fields.DBG_FieldsMapper import *

class DBG_RaidportTargets_PyArray(DBG_AdapterBase):
        def __init__(self,spar,pparent):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "Raidport" )
                self.xx_set_full_class_name ( "iastora!Raidport" )                
                self.m_targets = []
                self.mNumPaths = 0
                self.mNumRaidportTargets = 0
                self.mNumLuns = 1
                self.m_fields = DBG_FieldsMapper("DBG_RaidportTargets_PyArray",self)
                self.xx_dbg("DBG_MpbDisk_PyArray::constructor::method_out::")
                
        def init_object_fields(self):
                self.xx_dbg("DBG_MpbDisk_PyArray::init_object_fields::method_in::")
                
                lunh = DBG_PrintConfig().getItem().m_is_handled_lun
                #print "LLLH:" + str(lunh)
                
                if(lunh == 1):
                        self.m_fields.add_fields_asstr_ints([
                                "mNumPaths"
                                ,"mNumTargets"
                                ,"mNumLuns"
                                ])
                                        
                if(lunh == 0):
                        self.m_fields.add_fields_asstr_ints([
                                "mNumPaths"
                                ,"mNumTargets"                                
                                ])
                        
                #self.m_fields.add_fields_int("mNumPaths")
                self.xx_dbg("DBG_MpbDisk_PyArray::init_object_fields::method_out::")
                
        def set_parent(self,pparent,path, targets):
                self.xx_dbg("DBG_RaidportTargets::set_parent::in")
                self.m_parent = pparent
                self.mNumPaths = path
                self.mNumRaidportTargets = targets                
                self.xx_dbg("DBG_RaidportTargets::set_parent::out")
                
        def prepare_object(self):
                self.xx_dbg("DBG_RaidportTargets::prepare_object::in::")
                self.init_object_fields()
                if(self.prepare_check() == 1):
                        self.xx_dbg("prepare_check::prepared_out::")
                        return
                                
                self.clear_messages()
                
                self.m_fields.set_fields_parent(self.m_parent)
                self.m_fields.prepare_object()
                
                self.prepare_attributes()
                self.prepare_targets()
                self.xx_dbg("DBG_RaidportTargets::prepare_object::out::")
                
        def prepare_attributes(self):
                self.xx_dbg("DBG_RaidportTargets::prepare_attributes::in::")
                
                if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):                        
                        self.mNumLuns = self.m_fields.get_fields_asstr_int("mNumLuns")
                else:
                        self.mNumLuns = 1
                                             
                self.xx_dbg("DBG_RaidportTargets::prepare_attributes::out::")
                
        def prepare_targets(self):
                self.xx_dbg("DBG_RaidportTargets::prepare_targets::in::")
                
                self.m_targets = []
                
                handled_paths = self.mNumPaths
                if (DBG_PrintConfig().getItem().m_handle_transport_paths == 0):
                        handled_paths = 1
                        
                for ii_paths in range(handled_paths):
                        if self.path_in_range(ii_paths) == 0:
                                continue
                        self.x_dbg("DBG_RaidportTargets::prepare_path::in::")
                        for ii_targets in range(self.mNumRaidportTargets):                                
                                self.x_dbg("DBG_RaidportTargets::prepare_target::in::")                                
                                for ii_luns in range(self.mNumLuns):
                                        self.x_dbg("DBG_RaidportTargets::prepare_lun::in::")            
                                        ddt = self.create_target(                                        
                                                        self.m_parent
                                                        ,       ii_paths
                                                        ,       ii_targets
                                                        ,       ii_luns)
                                        
                                        if(ddt != None):                                        
                                                self.m_targets.append ( ddt )
                                                                        
                self.x_dbg("DBG_RaidportTargets::prepare_targets::out::")
                
        def add_use_info(self, dd_raidport_target,i,j):
                try:
                        snum = "TARGET[" + str(i) + "][" + str(j) + "][0]"
                        if(dd_raidport_target.raidport_target_is_used()):
                                self.m_fields.add_raw_str(snum + " USED")
                except:
                        self.xx_exception("DBG_RaidportTargets::add_use_info::out")
                                
        
        def create_target(self, pparent, ppath, ptarget, plun):
                try:
                        self.xx_dbg("DBG_RaidportTargetsPath::prepare_object::method_in::")
                        
                        dd_ret_target = None
                        dd_target = DBG_RaidportTarget_PyManager("Parent::DBG_RaidportTargets")
                                                
                        if(DBG_PrintConfig().getItem().m_is_handled_lun == 1):
                                sadr = "mTarget[" + str(ppath) + "]["  + str(ptarget) + "][" + str(plun) +"]"
                                dd_target.set_addr(pparent,sadr)
                                dd_target.prepare_object()
                        else:
                                sadr = "mTarget[" + str(ppath) + "]["  + str(ptarget) + "]"
                                dd_target.set_addr(pparent,sadr)
                                dd_target.prepare_object()
                                
                        dd_ret_target = dd_target
                        self.xx_dbg("DBG_RaidportTargetsPath::prepare_object::method_out::")
                        return dd_ret_target
                except:
                        self.xx_exception("DBG_RaidportTargets::create_target")
                        return None

        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_RaidportTargets::print_object::in::")
                
                self.prepare_object()
                self.xx_print_ptr("")
                
                if(self.xx_is_object() == 1):
                        self.m_fields.print_object()
                        self.print_targets()
                        
                self.xx_dbg("DBG_RaidportTargets::print_object::out::")



        def print_targets(self):
                self.xx_dbg("DBG_RaidportTargets::print_targets::in::")
                for dd_target in self.m_targets:
                        dd_target.print_object()                                        
                self.xx_dbg("DBG_RaidportTargets::print_targets::out::")

        def path_in_range(self,p_ii):                
                return DBG_PrintConfig().getItem().path_in_range(p_ii)
