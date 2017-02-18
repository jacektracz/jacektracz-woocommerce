import sys
import os
from pykd import *
from .. appcore.config.DBG_PrintConfig import *
from .. breakp.DBG_BreakpItem import *

class DBG_BreakpBase:
        def __init__(self,sdbg): 
                self.m_class_name = "DBG_BreakBase"
                self.m_full_class_name ="DBG_BreakBase"                
                self.m_remap_name = 0
                self.m_bp_command = "bu"
                self.m_print_dbg = 0
                self.m_print_command = 1
                self.m_sys_name = "iastora"
                self.m_sys_names = ["iastora"]
                self.m_bp_go = 0
                #self.clear_added_names()
                self.m_provided_handle = "X"
                self.m_default_bph = "1"
                self.clear_added_names()
                
        def xx_set_class_name(self,p_class_name):			
                self.m_class_name = p_class_name
        
        def xx_set_full_class_name(self,p_class_name):			
                self.m_full_class_name = p_class_name

        def clear_added_names(self):
                self.m_sys_names = ["iastora","hiber_iastora"]
                
        def xx_dbg(self, ss):
                """ """
                if(self.m_print_dbg ==1):
                        print ss
                
        def xx_exception(self,symbol,method=""):				
                logging.exception("")

        def xx_safe_exe_raw(self, s_command, s_info=""):
                self.xx_dbg("DBG_BreakpRaidport::xx_safe_exe_raw::method_in::" + s_command)
                rm_old = self.m_remap_name
                try:                                                
                        self.xx_dbg_command_no_remap(s_command)                        
                        self.xx_dbg("DBG_BreakpRaidport::xx_safe_exe_raw::method_out::" + s_command)
                except:
                    self.xx_exception("xx_safe_exe:" + s_command)

        def xx_print(self,tt):
            print tt
                
        def xx_safe_exe(self, s_command, s_info=""):
                try:
                        self.xx_dbg("DBG_BreakpRaidport::xx_safe_exe::method_in::" + s_command)
                        d1 = self.xx_dbg_command_remap(s_command)
                        self.xx_dbg("DBG_BreakpRaidport::xx_safe_exe::method_out::")
                except:
                    self.xx_exception("xx_safe_exe:" + s_command)
            
        def xx_gett(self, stabs):
            return ""
        
        def get_bp_handle(self):
                s_h = ""
                if(self.m_bp_go == 1):
                        s_h = ' "kb;dv;g"'
                return s_h

        def get_bp_echo(self, p_dd,s_exe):
                ss = ' "'
                ss = ss + '.echo '
                ss = ss + '\''                
                ss = ss + "========>"
                ss = ss + p_dd.m_system
                ss = ss +  " "
                ss = ss + p_dd.m_exec 
                #ss = ss + "========!"
                
                ss = ss +  '\''
                ss = ss  + s_exe
                ss = ss + ' "'
                return ss
        
        def get_bp_handle_item(self, p_dd):
                s_h = ""
                
                if(p_dd.m_handle == "1"):
                        s_h = self. get_bp_echo(p_dd,";g")

                if(p_dd.m_handle == "2"):
                        s_h = self. get_bp_echo(p_dd,";dv;g")
                
                if(p_dd.m_handle == "3"):
                        s_h = self. get_bp_echo(p_dd,"")
                        
                if(p_dd.m_handle == "4"):
                        s_h = self. get_bp_echo(p_dd,";kb;dv;g")
                        
                        
                return s_h
        
        def get_handle(self,tt,psys):
                try:
                        self.xx_dbg("DBG_BreakpRaidport::get_handle::method_in::")
                        dd_out = DBG_BreakpItem("")
                        dd_out.m_exec = tt
                        dd_out.m_handle = self.m_default_bph
                        dd_out.m_system = psys
                        if(tt.find("HANDLE[") >=0):
                                dd_out.m_handle = tt[7:8]
                                dd_out.m_exec= tt[9:]
                                
                        if(self.m_provided_handle != "X"):
                                dd_out.m_handle = self.m_provided_handle
                                
                        print "provided_handle:" + self.m_provided_handle        
                        print "handle:" + dd_out.m_handle
                        print "exec:" + dd_out.m_exec
                        self.xx_dbg("DBG_BreakpRaidport::get_handle::method_out::")
                        return dd_out
                        
                except:
                        self.xx_exception("get_handle:")
                        
        def xx_set_bpreakpoint_arr(self,pp):
                self.xx_dbg("DBG_BreakpRaidport::xx_set_bpreakpoint_arr::method_in::")                        
                for dd_ii in self.m_sys_names:
                        for dd_bp in pp :
                                ddh = self.get_handle(dd_bp,dd_ii)
                                s_handler = self.get_bp_handle_item( ddh )
                                s_ver = dd_ii + "!" + ddh.m_exec + s_handler
                                self.xx_set_bpreakpoint( s_ver )
                        
                self.xx_dbg("DBG_BreakpRaidport::xx_set_bpreakpoint_arr::method_out::")
                
        def xx_set_bpreakpoint_arr_raw(self,pp):
                self.xx_dbg("DBG_BreakpRaidport::xx_set_bpreakpoint_arr::method_in::")                        
                
                for dd_bp in pp :
                        s_ver = dd_bp + self.get_bp_handle()
                        self.xx_set_bpreakpoint( s_ver )
                        
                self.xx_dbg("DBG_BreakpRaidport::xx_set_bpreakpoint_arr::method_out::")
                
        def xx_set_commands_arr_raw(self,pp):
                self.xx_dbg("DBG_BreakpRaidport::xx_set_commands_arr_raw::method_in::")                        
                
                for dd_bp in pp :
                        s_ver = dd_bp
                        self.xx_dbg("DBG_BreakpRaidport::xx_set_commands_arr_raw::s_ver::" + str(s_ver) )
                        self.xx_safe_exe_raw( s_ver )
                        
                self.xx_dbg("DBG_BreakpRaidport::xx_set_commands_arr_raw::method_out::")
                
        def xx_set_handle_ex(self, paddr_logical, phandle):
                self.xx_dbg("DBG_BreakpRaidport::xx_set_handle_ex::method_in::[" + paddr_logical + "]")
                for dd_ii in self.m_sys_names:
                        s_ver = dd_ii + "!" + paddr_logical
                        self.xx_set_handle_ex_inner(s_ver, phandle)
                        
                self.xx_dbg("DBG_BreakpRaidport::xx_set_handle_ex::method_out::")

        def xx_set_handle_ex_inner(self, paddr_logical, phandle):                
                try:
                        self.xx_dbg("DBG_BreakpRaidport::xx_set_handle_ex_inner::method_in::[" + paddr_logical + "]")
                        paddr_logical_remap = self.xx_get_iastora_ver( paddr_logical )
                        self.xx_dbg("DBG_BreakpRaidport::xx_set_handle_ex_inner::hendler::" + paddr_logical_remap)
                        addr = self.xx_get_addr_i64(paddr_logical_remap)
                        if(addr == "0"):
                                return
                        self.print_dbg_command(paddr_logical_remap + " addr:" + str(addr))
                        setBp(addr, phandle)
                        self.xx_dbg("DBG_BreakpRaidport::xx_set_handle_ex_inner::method_out::")
                except:
                    self.xx_exception("xx_set_handle_ex_inner:" + str(paddr_logical_remap))
                    print "Can't set addr:" + paddr_logical_remap
                    return "0"
                
        def print_dbg_command(self,tt):
                self.xx_dbg("DBG_BreakpRaidport::print_dbg_command::method_in::")
                if self.m_print_command == 1:
                        print tt
                self.xx_dbg("DBG_BreakpRaidport::print_dbg_command::method_out::")
                
        def xx_set_bpreakpoint(self,tt):
                try:
                        self.xx_dbg("DBG_BreakpRaidport::xx_set_bpreakpoint::method_in::")
                        self.xx_safe_exe(self.m_bp_command + " " + tt)
                        self.xx_dbg("DBG_BreakpRaidport::xx_set_bpreakpoint::method_out::")
                except:
                    self.xx_exception("xx_set_bpreakpoint:" + str(tt))
                        
        def xx_get_addr_i64(self,tt):
                self.xx_dbg("DBG_BreakpBase::xx_get_addr_i64::method_in::")
                s_addr = self.xx_get_addr_raw(tt)
                
                if(s_addr == "0"):
                        return "0"
                
                s_addr = "0x" + s_addr
                i_addr = int(s_addr, 16)
                self.xx_dbg("DBG_BreakpBase::xx_get_addr_i64::method_out::" + str(i_addr))
                return i_addr
        
        def xx_get_addr_raw(self,localAddr):
                self.xx_dbg("DBG_BreakpBase::xx_get_addr_raw::method_in::")
                
                symbol = "x " + localAddr
                try:
                        res = dbgCommand( symbol )
                except:
                        print "can't access " + symbol
                        return "0"
                
                if res.count("\n") > 1:
                    print "[-] Warning, more than one result for" + symbol
                s_out =  res.split()[0]
                s_out = s_out.replace("`","")
                self.xx_dbg("DBG_BreakpBase::xx_get_addr_raw::method_out::" + str(s_out))                
                return s_out
        
        def xx_dbg_command_remap(self,symbol):
                try:
                    self.xx_dbg( "DBG_BreakpBase::xx_dbg_command_remap::" + symbol )
                    s_ver = self.xx_get_iastora_ver(symbol)
                    self.xx_dbg( "DBG_BreakpBase::xx_dbg_command_remap::remaped::" + s_ver )
                    self.print_dbg_command(s_ver)
                    sout = dbgCommand(s_ver)
                    self.xx_dbg( "DBG_BreakpBase::xx_dbg_command_remap::method_out::" )
                    return sout
                except:
                    self.xx_exception(symbol,"xx_dbg_command_remap")            
                    return "0"
                
        def xx_dbg_command_no_remap(self,symbol):
                try:
                    self.xx_dbg( "DBG_BreakpBase::xx_dbg_command_no_remap::" + symbol )
                    s_ver = symbol
                    self.xx_dbg( "DBG_BreakpBase::xx_dbg_command_no_remap::remaped::" + s_ver )
                    self.print_dbg_command(s_ver)
                    sout = dbgCommand(s_ver)
                    self.xx_dbg( "DBG_BreakpBase::xx_dbg_command_no_remap::method_out::" )
                    return sout
                except:
                    self.xx_exception(symbol,"xx_dbg_command_remap")            
                    return "0"        

        def xx_get_iastora_ver(self, p_command):
                self.xx_dbg( "DBG_BreakpBase::xx_get_iastora_ver::in::" + str(p_command))
                s_cn = p_command
                
                if( s_cn.find("hiber_iastora")>=0):
                    return s_cn
                        
                if(self.m_remap_name == 1):                            
                        if( self.m_sys_name != ""):				
                            s_cn = s_cn.replace("iastora!",self.m_sys_name + "!")
                    
                self.xx_dbg( "DBG_BreakpBase::xx_get_iastora_ver::out::[" + str(s_cn) + "]")
                return s_cn        

        def go_if_go(self):                
                self.xx_dbg("DBG_BreakpRaidport::go_if_go::method_in::")
                #go()
                self.xx_dbg("DBG_BreakpRaidport::go_if_go::method_out::")


        def add_ver(self, pp,ver):
                out_vv = []
                for dd_ii in add_ver:
                        out_vv.append(ver + dd_ii)
                return out_vv                        