import sys
import os
from ... appcore.memory.DBG_Utils import *
from ... appcore.logging.DBG_Log import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.htmlwriters.DBG_MainPrintDispatcher import *
class DBG_MemoryTools:
        
        def __init__(self):			
            self.xx_dbg("DBG_MemoryTools__init__")
            self.m_verbose = 1
            self.m_pattern = "numRaidDevs__"

            
        def xx_set_verbose(self, pvar):
            self.m_verbose = pvar
            
        def xx_show_var(self, svar, s_expr):
                if(self.m_verbose == 1 and svar == self.m_pattern):
                        DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( s_expr )
            
        def xx_get_int(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        
                        sval = 0
                        if(parent.xx_is_object()):                        
                                sval = DBG_Utils().xx_getAsInt(s_expr)
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return -1

        def xx_get_u32(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                                                
                        sval = 0
                        if(parent.xx_is_object()):                        
                                sval = DBG_Utils().xx_get_as_u32(s_expr)
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return -1
                       
        def xx_get_bool(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        sval = "0"
                        if(parent.xx_is_object()):
                                sval = DBG_Utils().xx_get_as_bool_by_str( s_expr )
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return 0

        def xx_get_as_raw_output(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        
                        sval = "0"
                        if(parent.xx_is_object()):
                                sval = DBG_Utils().xx_get_as_raw_output( s_expr )                                
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return "0000000000"

        def xx_get_as_addr(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        
                        sval = "0"
                        if(parent.xx_is_object()):
                                sval = DBG_Utils().xx_get_as_raw_output( s_expr )                                
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return "0000000000"
                
        
        def xx_get_hex(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        
                        sval = "0"
                        if(parent.xx_is_object()):
                                sval = DBG_Utils().xx_getAsHex( s_expr )
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return "-1"

        def xx_get_str(self, parent, svar,slen):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        
                        sval = ""
                        if(parent.xx_is_object()):                        
                                sval = DBG_Utils().xx_getAsStrEx( s_expr, slen )
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return "EXCEPTION:"

        def xx_get_str_unicode(self, parent, svar,slen):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        
                        sval = ""
                        if(parent.xx_is_object()):                        
                                sval = DBG_Utils().xx_get_str_unicode( s_expr, slen )
                        return sval
                except:
                       self.xx_exception("xx_get_str_unicode[expression:" + s_expr + "]")
                       return "EXCEPTION:"
                
                
        def xx_check_str(self, parent, svar,slen):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        self.xx_show_var(svar,s_expr)
                        
                        sval = -1
                        
                        if(parent.xx_is_object()):                        
                                sval = DBG_Utils().xx_check_str( s_expr, slen )
                                
                        return sval
                except:
                       self.xx_exception("xx_get_int[expression:" + s_expr + "]")
                       return -1
        

        def xx_check_int(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        sval = -1
                        if(parent.xx_is_object()==0):
                                return -1
                        sval = DBG_Utils().xx_check_int(s_expr)
                        return sval
                except:
                        if(DBG_PrintConfig().getItem().m_print_all_errors == 1):
                                 self.xx_exception("xx_get_int[expression:" + s_expr + "]")         
                        return -1


        def xx_check_u32(self, parent, svar):
                s_expr = self.xx_get_expr(parent, svar)
                try:
                        sval = -1
                        if(parent.xx_is_object()==0):
                                return -1
                        sval = DBG_Utils().xx_check_u32(s_expr)
                        return sval
                except:
                        if(DBG_PrintConfig().getItem().m_print_all_errors == 1):
                                 self.xx_exception("xx_get_int[expression:" + s_expr + "]")         
                        return -1

        def xx_exception(self, tt):
                DBG_Log().xx_exc(tt)

        def xx_dbg(self,ss):
                dd = 0
                if(dd == 1 ):
                        DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( ss )
                        
        def xx_get_expr(self,parent,svar):
                s_expr = "@@C++((" + parent.xx_get_class_ptr("") + ")->" + svar + ")"
                return s_expr

        def print_threads(self):
                threads = getProcessThreads()
                for t in threads:
                    print(hex(ptrPtr(t+0x24))[2:-1])
    