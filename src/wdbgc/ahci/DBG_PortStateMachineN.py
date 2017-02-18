import sys
import os
import logging
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
from .. defs.DBG_PortStateMachineMap import *
from .. defs.DBG_PortStateMachineModeMap import *
class DBG_PortStateMachineN(DBG_AdapterBase):
        def __init__(self,spar):                
                DBG_AdapterBase.__init__(self,spar)
                self.xx_dbg("DBG_PortStateMachineN::__init__::in::")
                self.xx_set_class_name ( "PortStateMachine" )
                self.xx_set_full_class_name ( "iastora!PortStateMachine" )
                self.m_fields = DBG_FieldsMapper("DBG_PortStateMachineN"
                                         ,self)                                
                
                self.xx_dbg("DBG_PortStateMachineN::__init__::out::")
                
        def prepare_object(self):
                try:
                        self.xx_dbg("DBG_PortStateMachineN::prepare_object")
                        self.m_fields.set_fields_parent(self)
                        self.m_fields.add_fields_int_array([
                                "mNextState"
                                ,"mCurrentState"
                                ,"mTargetState"
                                ,"mRunning"
                                ,"mConfigured"
                                ,"mSlot"
                                ,"mStatus"
                                ,"mCurrentMode"
                                ,"mPreviousMode"])
                        
                        self.m_fields.add_fields_bool_array([
                                "mSynchronousMode"
                                ,"mConfigured"
                                ,"mReturnToPaused"
                                ,"mNcqErrorRecovery"
                                ])
                        
                        self.m_fields.prepare_object()
                        self.add_state("mCurrentState")
                        self.add_state("mNextState")
                        self.add_mode("mCurrentMode")
                        self.add_mode("mPreviousMode")
                except:
                        self.xx_exception("DBG_PortStateMachineN::prepare_object")


        def add_state(self,ii_state):
                try:
                        val_state = self.m_fields.get_fields_int(ii_state)
                        smb = DBG_PortStateMachineMap("").get_str( val_state )
                        self.m_fields.add_raw_str("State:" + ii_state + ":" + smb)
                        
                except:
                        self.xx_exception("DBG_PortStateMachineN::add_state")

        def add_mode(self,ii_mode):
                try:                                                
                        val_mode = self.m_fields.get_fields_int(ii_mode)
                        s_mode = DBG_PortStateMachineModeMap("").get_str( val_mode )
                        self.m_fields.add_raw_str("Mode:" + ii_mode + ":" + s_mode )
                except:
                        self.xx_exception("DBG_PortStateMachineN::add_state")

        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_PortStateMachineN::print_object::in")
                self.prepare_object()
                self.xx_print_ptr("")
                self.m_fields.xx_print_fields("")
                self.xx_dbg("DBG_PortStateMachineN::print_object::out::")

