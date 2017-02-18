import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. appcore.memory.DBG_MemoryTools import *
from .. appcore.logging.DBG_Log import *
from DBG_Target import *


class DBG_TargetsPath:
        def __init__(self,spar,pparent,targets):
                self.x_dbg("DBG_TargetsPath::set_parent::in")
                self.m_targets = []
                self.m_parent = pparent
                self.m_path_idx = 0
                self.m_target_idx = 0
                self.x_dbg("DBG_TargetsPath::set_parent::out")
                                
        def prepare_object(self):
                self.x_dbg("DBG_Targets::prepare_object::in::")
                
                self.x_dbg("DBG_Targets::prepare_object::out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.x_dbg("DBG_Targets::print_object::in::")
                self.prepare_object()
                
                self.x_dbg("DBG_Targets::print_object::out::")
                
                
        def x_dbg(self,ss):
                DBG_Log().xx_dbg(ss)
                
class DBG_TargetsArray(DBG_AdapterBase):
        def __init__(self,spar,pparent):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_set_class_name ( "Target" )
                self.xx_set_full_class_name ( "iastora!Target" )
                self.m_paths = []                
                self.mNumPaths = 0
                self.mNumTargets = 0
                
        def set_parent(self,pparent,path, targets):
                self.x_dbg("DBG_Targets::set_parent::in")
                self.m_parent = pparent
                self.mNumPaths = path
                self.mNumTargets = targets                
                self.x_dbg("DBG_Targets::set_parent::out")
                
        def prepare_object(self):
                self.x_dbg("DBG_Targets::prepare_object::in::")
                self.prepare_targets()
                self.x_dbg("DBG_Targets::prepare_object::out::")
                
        def print_object(self):
                self.x_dbg("DBG_Targets::print_object::in::")
                self.prepare_object()
                self.xx_print_ptr("")
                
                for dd_paths in self.m_paths:
                        for dd_target in dd_paths.m_targets:
                                dd_target.print_object()
                                
                self.x_dbg("DBG_Targets::print_object::out::")
        
        def prepare_targets(self):
                self.x_dbg("DBG_Targets::prepare_targets::in::")
                
                for i in range(self.mNumPaths):
                        
                        ddp = DBG_TargetsPath("DBG_TargetsArray",self,self.mNumTargets)
                        
                        for j in range(self.mNumTargets):
                                self.x_dbg("DBG_Targets::prepare_target::in::")
                                ddt = self.create_target(self.m_parent,i,j)
                                ddp.m_targets.append(ddt)                                
                        self.m_paths.append(ddp);
                        
                self.x_dbg("DBG_Targets::prepare_targets::out::")                        
        
        def create_target(self,pparent,ppath,ptarget):
                self.x_dbg("DBG_TargetsPath::prepare_object::in::")
                
                dd_target = DBG_Target("Parent::DBG_TargetsPath")                                
                dd_target.xx_inc_tabs(pparent);
                sadr = "mTarget[" + str(ppath) + "]["  + str(ptarget) + "]"
                dd_target.xx_compute_arr_phy_by_parent(pparent,sadr)                
                self.x_dbg("DBG_TargetsPath::prepare_object::out::")
                return dd_target


        def x_dbg(self,ss):
            DBG_Log().xx_dbg(ss)
