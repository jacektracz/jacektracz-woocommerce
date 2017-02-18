import sys
import os
import logging
from ... DBG_AdapterBase import *
from ... appcore.memory.DBG_MemoryTools import *
from ... appcore.logging.DBG_Log import *
from ... appsrc.raidtargets.DBG_RaidportTarget_PyManager import *

class DBG_RaidportTargetsPath(DBG_AdapterBase):
        def __init__(self,spar,pparent,targets):
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_RaidportTargetsPath::set_parent::in")
                self.m_targets = []
                self.m_parent = pparent
                self.m_path_idx = 0
                self.m_target_idx = 0
                self.xx_dbg("DBG_RaidportTargetsPath::set_parent::out")
                                
        def prepare_object(self):
                self.xx_dbg("DBG_RaidportTargets::prepare_object::in::")
                
                self.xx_dbg("DBG_RaidportTargets::prepare_object::out::")
                
        def print_object(self):
                try:
                        self.xx_print_start("")
                        self.print_object_internal()
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self):
                self.xx_dbg("DBG_RaidportTargets::print_object::in::")
                self.xx_print_start()
                self.prepare_object()
                self.xx_print_end()
                self.xx_dbg("DBG_RaidportTargets::print_object::out::")
                
