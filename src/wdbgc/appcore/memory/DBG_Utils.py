import sys
import logging
from pykd import *

from ... appcore.logging.DBG_Log import *
from ... appcore.htmlwriters.DBG_MainPrintDispatcher import *
from ... appcore.config.DBG_PrintConfig import *
from ... appcore.logging.DBG_ExceptionPrinter import *

class DBG_Utils:
    def __init__(self):             
            self.m_dbg_print = 0
    
    def xx_comm_start(self,s_i_1,s_i_2):
            try:
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "************************************************************************" )               
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*                START_COMMAND")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*" )               
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "************************************************************************")
                    
            except:
                    self.xx_exception(localAddr,"xx_safe_exe") 
            
    def xx_comm_info(self,s_i_1,s_i_2):
            try:
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "-------------------------------------------------------------------------")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*                        " + s_i_1       )
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*")
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "*" )               
                    DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "-------------------------------------------------------------------------")
                    
            except:
                    self.xx_exception(localAddr,"xx_safe_exe")      
    def xx_safe_exe(self,s_command,s_info):
        try:
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "=========================COMMAND START===============================")
                
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "")                
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "command: " + s_command)
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "info: " + s_info)
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "")
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "")
                d1 = self.xx_dbgCommand(s_command)
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( d1)
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( '=========================COMMAND END=================================')
        except:
            self.xx_exception(localAddr,"xx_safe_exe")
            
    def xx_get_addr(self,localAddr,sdbg=''):
        return self.xx_getAddress(localAddr)
    
    def xx_getAddress(self,localAddr,sdbg=''):
        try:
            res = self.xx_dbgCommand("x " + localAddr)
            if res.count("\n") > 1:
                DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "[-] Warning, more than one result for", localAddr)
            return res.split()[3]
        except:
            self.xx_exception(localAddr,"xx_getAddress")                 
                
    def xx_link(self,prefix,command,label):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( ".printf /D \"<link cmd=\"%s\">%s</link>\\n\"" % (command,label)
            #dbgCommand(".printf /D \"<link cmd=\\\"%s\\\">%s</link>\\n\"" % (command,label));
            dprintln("%s<link cmd=\"%s\">%s</link>"%(prefix,command,label),True)
        except:
            self.xx_exception(symbol,"xx_link")            
            
    def xx_link_ex(self,prefix,command,label):
        try:
            DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( ".printf /D \"<link cmd=\"%s\">%s</link>\\n\"" % (command,label))
            #dbgCommand(".printf /D \"<link cmd=\\\"%s\\\">%s</link>\\n\"" % (command,label));
            DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( prefix)
            DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( command)
            DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( label)
            s_cmm = prefix + "<link cmd=\"" + command + "\">" + label +"</link>"
            
            dprintln(s_cmm,True)
        except:
            self.xx_exception(symbol,"xx_link_ex")
            
    def xx_check_int(self,symbol):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            s_ex = ".printf \"\%i\"," + symbol
            i_int = self.xx_dbgCommandCheck_Out01( s_ex )
            return i_int
        except:
            i_out = self.xx_check_excpetion("xx_check_int",symbol,1)
            return i_out

        
    def xx_check_str(self,symbol,slen):
        try:
            self.dgb_symbol( symbol )
            s_str = dbgCommand(".printf \"\%ma\"," + symbol)
            s_str_check = self.get_str_ascii(s_str)
            #s_str_check = str(s_str)            
            return 1
        except:
            i_out = self.xx_check_excpetion("xx_check_str",symbol,slen)
            return i_out
        
    def get_str_ascii(self,tt):
        s_str_check = tt.encode('ascii', 'ignore').decode('ascii')
        return s_str_check
    
    def xx_check_u32(self,symbol):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            s_ex = ".printf \"\%lu\"," + symbol            
            i_int = self.xx_dbgCommandCheck_Out01( s_ex )
            return i_int
        except:
            i_out = self.xx_check_excpetion("xx_check_u32",symbol,1)
            return i_out

            
    def xx_getAsInt(self,symbol):
        try:
            self.xx_dbg("DBG_Utils::xx_getAsInt::method_in::" + str(symbol) )
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            sint = self.xx_dbgCommandEx(".printf \"\%i\"," + symbol, "-1")
            self.xx_dbg("DBG_Utils::xx_getAsInt::method_ret_tmp::" + str(symbol) + " " + str(sint))
            ddout = self.xx_get_int_from_str(sint)
            self.xx_dbg("DBG_Utils::xx_getAsInt::method_out::")
            return ddout
        except:
            self.xx_exception(symbol,"xx_getAsInt")
            return -1
        
    def xx_get_as_u32(self,symbol):
        try:
            self.xx_dbg("DBG_Utils::xx_get_as_u32::method_in::" + str(symbol) )
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            sint = self.xx_dbgCommandEx(".printf \"\%lu\"," + symbol, "-1" )
            self.xx_dbg("DBG_Utils::xx_get_as_u32::method_ret_tmp::" + str(symbol) + " " + str(sint))
            ddout = self.xx_get_int_from_str(sint)
            return ddout
        except:
            self.xx_exception(symbol,"xx_getAsInt")
            return -1
        
    def xx_get_int_from_str(self,pss):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            ddout =  int(pss)
            return ddout
        except:            
            return -1                        
            
    def xx_getAsPtr(self,symbol):
        try:
            self.xx_dbg("DBG_Utils::xx_getAsPtr::method_in::" + str(symbol) )
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            return self.xx_dbgCommandEx(".printf \"\%p\"," + symbol,"0")
        except:
            self.xx_exception(symbol,"xx_getAsStrEx")
            return 0
        
    def xx_get_as_addr(self,symbol):
        try:
            return self.xx_dbgCommandEx(".printf \"\%p\"," + symbol,"0")
        except:
            self.xx_exception(symbol,"xx_get_as_addr")
            return 0
        
    def xx_get_as_raw_output(self,symbol):
        try:
            s_expr = "?? " + symbol            
            s_out =  self.xx_dbgCommandEx(s_expr,"0")            
            #self.xx_get_splitted_output(s_out)
            return s_out
        except:
            self.xx_exception(symbol,"xx_get_as_addr")
            return 0
        
    def xx_get_splitted_output(self,s_out):
        try:
            s_split = s_out.split()
            print "start:" 
            for dd_ss in s_split:
                print "yyyyyyyyyyyyyy:" + dd_ss
            print ""                 
            return s_out
        except:
            self.xx_exception(symbol,"xx_get_as_addr")
            return 0

    def xx_getAsHex(self,symbol):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            return self.xx_dbgCommandEx(".printf \"\%x\"," +symbol, 0 )
        except:
            self.xx_exception(symbol,"xx_getAsStrEx")
            return 0

    def xx_get_str_unicode(self,symbol,slen):
        try:
            self.xx_dbg("DBG_Utils::xx_get_str_unicode::method_in::" + str(symbol) + " " +str(slen))
            s_comm = ".printf \"\%mu\","+symbol
            return self.xx_dbgCommand( s_comm )
        except:
            self.xx_exception(symbol,"xx_getAsStrEx")
            return ""

    def xx_get_str_unicode_struct(self,symbol,slen):
        try:
            self.xx_dbg("DBG_Utils::xx_get_str_unicode_struct::method_in::" + str(symbol) + " " +str(slen))
            symbol = ()
            s_comm = ".printf \"\%mu\","+symbol
            return self.xx_dbgCommand( s_comm )
        except:
            self.xx_exception(symbol,"xx_getAsStrEx")
            return ""

    def xx_getAsStr(self,symbol):
        try:
            self.xx_dbg("DBG_Utils::xx_getAsStr::method_in::" + str(symbol) )
            s_comm = ".printf \"\%ma\","+symbol
            return self.xx_dbgCommand( s_comm )
        except:
            self.xx_exception(symbol,"xx_getAsStrEx")
            return ""

    def xx_getAsStrEx(self,symbol,maxl):
        try:            
            sout = self.xx_dbgCommand(".printf \"\%ma\","+symbol)
            if len(sout) > maxl:
                    sout = sout[:maxl]
            return sout
        except:
            self.xx_exception(symbol,"xx_getAsStrEx")
            return ""
    
    def xx_getAsStrDbg(self,symbol):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            sout = self.xx_dbgCommand(".printf \"\%ma\","+symbol)
            return sout                
        except:
            self.xx_exception(symbol,"xx_getAsStrDbg")
            return ""
        
    def xx_dbgCommandEx(self,symbol,sdefault):
        s_ver = symbol
        try:
            self.xx_dbg("DBG_Utils::xx_dbgCommandEx::method_in::" + str(symbol) )
            self.dgb_symbol( symbol )
            sout = sdefault
            s_ver = self.xx_get_iastora_ver( symbol )
            sout = dbgCommand(s_ver)            
            #sout = dbgCommand(symbol)
            return sout
        except:
            self.xx_exception("DBG_Utils::xx_dbgCommandEx" + str(s_ver),"xx_dbgCommand")
            return sdefault
        
    def xx_dbgCommand(self,symbol):
        try:
            self.dgb_symbol( symbol )
            s_ver = self.xx_get_iastora_ver(symbol)
            sout = dbgCommand(s_ver)
            return sout
        except:
            self.xx_exception(symbol,"xx_dbgCommand")            
            return "0"
        
    def dgb_symbol(self,tt):
            if(DBG_PrintConfig().getItem().m_print_wdgb_symbols == 1):
                #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( tt )
                print tt
        
    def xx_dbgCommandCheck_Out01(self,symbol):
        try:
            s_ver = self.xx_get_iastora_ver(symbol)
            sout = dbgCommand(s_ver)
            return 1
        except:            
            return -1
        
    def xx_str(self,symbol,method=""):
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            sout = str(symbol)
            return sout                
             
            
    def xx_get_as_bool_by_str(self,symbol):
        try:
            return self.xx_get_as_bool_str_from_int(symbol)
        except:
            self.xx_exception(symbol,"xx_get_as_bool_by_str")
            return -1
        
    def xx_get_as_bool_str_from_int(self,symbol):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            bout = "0"
            di = self.xx_getAsInt(symbol)            
            if(di == 1):
                bout = "1"
            return bout
        except:
            self.xx_exception(symbol,"xx_get_as_bool_str_from_int")
            return -1

    def xx_get_as_bool_intb(self,symbol):
        try:
            #DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( symbol
            bout = "0"
            sb = self.xx_dbgCommand(".printf \"\%s\"," + symbol)
            if (sb == "true"):
                ddout =  "1"
            else:            
                ddout = "0"
                
            return ddout
        except:
            self.xx_exception(symbol,"xx_get_as_bool")
            return -1
            
            
    def xx_check_excpetion(self, pmethod,symbol, slen ):
        
            if(DBG_PrintConfig().getItem().m_verbose_check == 1):
                s_ex = "[DBG_Utils::" + pmethod + "::[" + str(symbol) + "][" + str(slen) + "]"
                self.xx_exception(s_ex,"")
                
            i_out = 1                
            if(DBG_PrintConfig().getItem().m_skip_check == 1):
                i_out = 1
            else:
                i_out = -1
                
            return i_out
            
    def xx_exception(self,symbol,method=""):            
        try:            
            DBG_Log().xx_exc("[" + str(method) + "][" +"[excp:" + str(symbol) + "]")
        except:
            DBG_ExceptionPrinter.print_exception("xx_exception")
            
    def get_thread_id(self):
        try:
            st = self.xx_dbgCommand("r @$thread")
            return st
        except:
            self.xx_exception("get_thread_id","")
            return ""
        
    def get_paths(self):
        try:
            st = []
            st.append(self.xx_dbgCommand(".sympath"))
            st.append(self.xx_dbgCommand(".srcpath"))                     
            return st
        except:
            self.xx_exception("get_paths","")
            st = []
            return st

    def get_class_info(self,tt):
        s_expr = "?? " + tt
        try:
            vv_sc = []
            vv_sc.append("addr:[" + tt + "]")
            vv_sc.append("expr:[" + s_expr + "]")
            if(tt!= ""):
                st = []            
                sc = self.xx_dbgCommand( s_expr )
                vv  = sc.split('\n')
                for sii in vv:
                    vv_sc.append(sii)
                
            return vv_sc
        except:
            self.xx_exception("get_class_info[" + s_expr + "]")
            st = []
            return st

    def get_stack(self,tt= ""):
        s_expr = tt
        try:
            vv_sc = []            
            vv_sc.append("expr:[" + s_expr + "]")            
            sc = self.xx_dbgCommand( s_expr )
            vv  = sc.split('\n')
            for sii in vv:
                vv_sc.append(sii)
                
            return vv_sc
        except:
            self.xx_exception("get_class_info[" + s_expr + "]")
            st = []
            return st
                
    def xx_dbg(self, ss):
        if ( self.m_dbg_print == 1 ):
            print "DBG_PRINT:" + str(ss)
            return
        
        i_print = DBG_PrintConfig().getItem().check_dbg_filter(ss)
        if( i_print == 1):
            print "DBG_PRINT:" + str(ss)
            
            
    def xx_get_iastora_ver(self,p_full_class_name):
        self.xx_dbg( "DBG_MemoryPtr::xx_get_iastora_ver::in::" + str(p_full_class_name))
        s_cn = p_full_class_name
        
        if( s_cn.find("hiber_iastora")>=0):
            return s_cn
        
        self.m_sys_name = DBG_PrintConfig().getItem().m_sys_name
        if( self.m_sys_name != "" and self.m_sys_name != "iastora"):
            s_cn = p_full_class_name				
            s_cn = s_cn.replace("iastora!",self.m_sys_name + "!")				
        else:
            self.xx_dbg( "DBG_MemoryPtr::not_dump_mode::")
        #print s_cn    
        self.xx_dbg( "DBG_MemoryPtr::xx_get_iastora_ver::out::" + str(s_cn))
        return s_cn
        