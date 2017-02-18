import sys
import os        
from .. defs.DBG_Base_EnumState import *

class DBG_NvmePortState(DBG_Base_EnumState):
        def __init__(self,spar):
                DBG_Base_EnumState.__init__(self,spar)
                self.create_map()
                
        def create_map(self):            
                pp = [
                        "Stopped",
                        "Stopping",
                        "Initialized",
                        "Initializing",
                        "Started",
                        "Starting",
                        "ShutDown",
                        "ShuttingDown",
                        "Failed"]                        
                self.set_items(pp)