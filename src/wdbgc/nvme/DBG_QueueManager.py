

import sys
import os
from .. DBG_AdapterBase import *
from .. fields.DBG_FieldsMapper import *
#from .. childdir.DBG_ApstTable import *
from .. nvme.DBG_CompletionQueue import *
from .. nvme.DBG_CompletionQueue import *
from .. nvme.DBG_SubmissionQueue import *
from .. nvme.DBG_NumaMap import *
from .. appcore.config.DBG_PrintConfig import *
class DBG_QueueManager(DBG_AdapterBase):
        def __init__(self,spar):
                DBG_AdapterBase.__init__(self,spar)                
                self.xx_dbg("DBG_QueueManager::__init__::m_in::")
                self.xx_set_class_name ( "QueueManager" )
                self.xx_set_full_class_name ( "iastora!QueueManager" )
                #self.m_child_item = DBG_ApstTable("Parent::DBG_QueueManager")
                self.m_fields = DBG_FieldsMapper("DBG_QueueManager"
                                         , self)
                
                if(DBG_PrintConfig().getItem().is_below( 15,0,0,1013 ) == 1):                                
                        self.m_fields.add_fields_int_array([
                                "mNumOfCompletionQueue"
                                ,"mNumOfSubmissionQueue"
                                ,"mMaxIoQueueEntriesCount"
                                ])
                
                self.mAdminCompletionQueue = DBG_CompletionQueue("DBG_QueueManager")
                self.mAdminSubmissionQueue = DBG_SubmissionQueue("DBG_QueueManager")
                self.mNumaMap = DBG_NumaMap("DBG_QueueManager")
                self.xx_dbg("DBG_QueueManager::__init__::m_out::")
               
        def prepare_object(self):
                try:
                        self.prepare_object_internal(self)
                except:
                        self.xx_exception("DBG_QueueManager::prepare_object::exc::")
                                        
        def prepare_object_internal(self, pparent):
                self.xx_dbg("DBG_QueueManager::prepare_object_internal::")
                
                if(self.xx_is_object()==1):
                        self.m_fields.set_fields_parent(self)
                        if(DBG_PrintConfig().getItem().is_below( 15,0,0,1013 ) == 1):                                
                                self.mAdminCompletionQueue.set_addr(self,"mAdminCompletionQueue")
                                self.mAdminSubmissionQueue.set_addr(self,"mAdminSubmissionQueue")
                        self.mNumaMap.set_addr_arr(self,"mNumaMap")

                        #self.m_child_item.set_addr_arr(self,"m_child_item")
                
                self.xx_dbg("DBG_QueueManager::prepare_object::m_out::")
                
        def print_object(self,sdbg=""):
                try:
                        self.xx_print_start("")
                        self.print_object_internal(sdbg)
                        self.xx_print_end("")
                except:
                        self.xx_exception("::print_object")
                        
        def print_object_internal(self,sdbg=""):
                self.xx_dbg("DBG_QueueManager::print_object::m_in::")
                self.prepare_object()                
                self.xx_print_ptr("")
                if(self.xx_is_object()==1):                
                        self.m_fields.xx_print_fields("")
                        if(DBG_PrintConfig().getItem().is_below( 15,0,0,1013 ) == 1):
                                self.mAdminCompletionQueue.print_object()
                                self.mAdminSubmissionQueue.print_object()
                        self.mNumaMap.print_object()
                        #self.m_child_item.print_object()
                self.xx_dbg("DBG_QueueManager::print_object::m_out::")

