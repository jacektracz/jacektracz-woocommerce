import sys
import os
from  exttools.cms.DBG_Cms import *
from  exttools.cms.DBG_CmsDispatcher import *
class DBG_CmsStarter:
                                
    def exec_dispatch(self,ptt):
        if (ptt == "1"):
            dd = DBG_Cms()
            dd.get_list_dir()
            
        if (ptt == "2"):
            dd = DBG_CmsDispatcher()
            dd.get_list_dir("D:\lkd\komodo\w2_2\dat\arch\a05_core_docs\linux")                
                
#c:/python27/python     D:\lkd\komodo\w2_2\src\w2\wdbgc\DBG_CmsStarter.py

if __name__ == '__main__':
    DBG_CmsStarter().exec_dispatch("2")
            