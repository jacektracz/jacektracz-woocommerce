import sys
import os
from pykd import *
from .. appcore.config.DBG_PrintConfig import *

class DBG_BreakpItem:
        def __init__(self,sdbg): 
                self.m_exec = ""
                self.m_handle ="1"
                self.m_system ="1"         
