import sys
import logging
from pykd import *
from appcore.memory.DBG_Utils import *
from appcore.memory.DBG_WdbgItemsPrinter import *
from appcore.logging.DBG_Log import *
from appcore.memory.DBG_MemoryTools import *
from appcore.htmlwriters.DBG_MainPrintDispatcher import *
from appcore.htmlwriters.DBG_Html import *
from appcore.printers.DBG_FieldInfos import *

from appcore.printers.DBG_BaseDbgPrinter import *
from appcore.printers.DBG_ClassRawPrinter import *
from appcore.printers.DBG_BaseHtmlPrinter import *
from appcore.printers.DBG_ParentsPathSeeker import *
from appcore.printers.DBG_StatePrinter import *
from appcore.printers.DBG_ExceptionHtmlPrinter import *
from appcore.config.DBG_PrintConfig import *
from appcore.globinfo.DBG_MainInformationsSet import *

class DBG_MemoryPtr:
		def __init__(self,spar):						
			self.tt = DBG_Utils()
			self.m_lg_ptr = "LGR_ADDRESS_NOT_SET"
			self.m_phy_addr = ""                
			self.m_class_name = ""
			self.m_full_class_name =""
			self.m_variable = ""
			self.m_class_descr = "XX"
			self.m_variable_accessor = ""
			self.m_parent_phy_addr = ""
			self.m_parent_lg_addr = ""
			self.m_addr_computation_type = "L"
			self.m_tabs = 0                
			self.m_parent = None
			self.m_stored_class_ptr_by_phy_addr = ""
			self.m_raw_variable = ""
			self.m_use_object = 1
			self.m_use_without_childs = 0			
			
			self.m_messages = DBG_FieldInfos("DBG_MemoryPtr",self)					
			self.m_exceptions = DBG_ExceptionHtmlPrinter(self,"DBG_MemoryPtr")
			self.m_number_of_child_ex = 0
			self.m_is_inbox = 0
			self.m_is_dump = 0
			self.m_path_object = DBG_ParentsPathSeeker(self,"DBG_MemoryPtr")
			self.m_sys_name	= ""
			self.m_hard_hard_print = 0
			self.m_is_prepared = 0
			self.m_class_printer = DBG_ClassRawPrinter(self,"DBG_MemoryPtr")
			self.m_selector_for_print = ""
			self.m_s_addr = ""
			self.m_class_ptr = ""
			self.xx_dbg("DBG_MemoryPtr__init__")
			
		def get_use_without_childs(self):
			return self.m_use_without_childs

		def set_selector_for_print(self,tt):
			self.m_selector_for_print = tt

		def get_selector_for_print(self):
			return self.m_selector_for_print
		
		def get_variable_from_selector_for_print(self):
			tt = self.m_selector_for_print
			if (tt == ""):
				tt = self.m_raw_variable
			return tt

		def prepare_init(self):
			self.m_is_prepared = 1

		def prepare_check(self):
			old_prep = self.m_is_prepared
			self.m_is_prepared = 1
			return old_prep

		def set_use_without_childs(self,pu):
			self.m_use_without_childs = pu
			
		def get_use_object(self):
			return self.m_use_object
		
		def set_use_object(self,pu):
			self.m_use_object = pu
		
		def xx_is_object(self):
			self.xx_dbg( "xx_is_object::method_in::")
			is_obj = 1
			if(is_obj == 1):
				if(self.m_phy_addr == self.get_0_addr()):
					is_obj = 0
					
			if(is_obj == 1):
				if(self.m_phy_addr == self.get_e_addr()):
					is_obj = 0
					
			if(is_obj == 1):	
				if(self.m_phy_addr == "0"):
					is_obj = 0
					
			if(is_obj == 1):		
				if(len(self.m_phy_addr.strip()) < 16):
					is_obj = 0
					
			self.xx_dbg( "xx_is_object::method_out::" + str(is_obj))
			
			return is_obj
		
		def get_0_addr(self):
			return "0000000000000000"

		def get_e_addr(self):
			return "eeee89abeeee89ab"
		
		
		
		def xx_get_lg_addr_str(self):
			sout = "" 
			+ self.m_parent_lg_addr 
			+  self.m_accessor                                      
			+ self.m_name + ""                                      
			return sout;

		def xx_get_phy_addr_str(self):
			sout = "" 
			+ self.m_parent_phy_addr 
			+  self.m_accessor                                      
			+ self.m_name + ""                                      
			return sout;

		def xx_set_tabs(self,itabs,sdeb=''):
			#DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( "tabs:" + sdeb + ":" + str(itabs)
			if(itabs == ""):
				self.m_tabs = 0
			else:
				self.m_tabs = itabs

		def xx_get_tabs(self):
			return self.m_tabs

		def xx_set_compute_phy_addr(self):
			s_addr = self.xx_get_cc(self.xx_get_phy_addr_str());
			self.m_phy_addr = DBG_Utils().xx_getAsPtr(s_addr)

		def xx_set_lg_addr(self):
			s_addr = self.xx_get_cc(self.xx_get_lg_addr_str());
			self.m_phy_addr = DBG_Utils().xx_getAsPtr(s_addr)
			
		def xx_inc_tabs(self, pparent, sdebug=''):
			self.m_parent = pparent
			self.xx_set_tabs(pparent.xx_get_tabs() + 1)

		def xx_inc_tabs_ex(self, pparent, pinc=1,sdebug=''):
			self.m_parent = pparent
			self.xx_set_tabs(pparent.xx_get_tabs() + pinc)
			
		#=================================================================
        #
		#       PHY ADDRESS
        #
		#=================================================================
        
		def xx_compute_arr_phy_by_global(self, pparent, pvariable,sdbg=''):
			self.xx_dbg( "xx_compute_phy_by_parent::method_in::")
			pprefix ="&"
			self.m_parent = pparent
			self.xx_compute_generic_phy_by_parent(pparent, pvariable,pprefix,sdbg)
        
		def xx_get_cc(self,ss):
			sout = "@@C++(" + str(ss) +  ")"     											 
			return sout
		
		def xx_ptr(self, pparent, pvariable,sdbg=''):
			self.m_parent = pparent
			return self.xx_compute_phy_by_parent(self, pparent, pvariable,sdbg='')
		
		def xx_compute_phy_by_parent(self, pparent, pvariable,sdbg=''):			
			self.xx_dbg( "xx_compute_phy_by_parent::method_in::")
			pprefix =""
			self.m_parent = pparent
			self.xx_compute_generic_phy_by_parent(pparent, pvariable,pprefix,sdbg)
			
		def xx_ptra(self, pparent, pvariable,sdbg=''):
			self.m_parent = pparent
			return self.xx_compute_arr_phy_by_parent(self, pparent, pvariable,sdbg='')
			
		def xx_compute_arr_phy_by_parent(self, pparent, pvariable,sdbg=''):
			self.xx_dbg( "xx_compute_phy_by_parent::method_in::")
			pprefix ="&"
			self.m_parent = pparent
			self.xx_compute_generic_phy_by_parent(pparent, pvariable,pprefix,sdbg)
			
		def xx_ptrc(self, pparent, pvariable,sdbg=''):
			self.m_parent = pparent
			return self.xx_compute_cpp_phy_by_parent(self, pparent, pvariable,sdbg='')
			
		def xx_compute_cpp_phy_by_parent(self, pparent, pvariable,sdbg=''):			
			self.xx_dbg( "xx_compute_phy_by_parent::method_in::")
			pprefix = "@@C++"
			self.m_parent = pparent
			self.xx_compute_generic_phy_by_parent(pparent, pvariable,pprefix,sdbg)

		def set_addr_arr_static(self, pparent,p_logical_addr):
			self.m_parent = pparent
			self.m_variable = p_logical_addr
			self.m_raw_variable = p_logical_addr
			s_adr = "((" + self.xx_get_full_class_name("") + "*)&(" + p_logical_addr + "))"
			self.xx_set_lg_compute_phy_addr(s_adr)
			
		def set_addr_static(self, pparent,p_logical_addr):
			self.m_parent = pparent
			self.m_variable = p_logical_addr
			self.m_raw_variable = p_logical_addr
			s_adr = "((" + self.xx_get_full_class_name("") + "*)(" + p_logical_addr + "))"
			self.xx_set_lg_compute_phy_addr(s_adr)
			
		def xx_set_lg_compute_phy_addr(self, p_logical_addr):
			try:
				self.xx_dbg( "xx_set_lg_compute_phy_addr:in")
				self.xx_hard_print("xx_set_lg_compute_phy_addr:[0]:" + self.m_lg_ptr)
				self.m_lg_ptr = self.xx_get_iastora_ver(p_logical_addr)
				self.m_phy_addr = self.get_0_addr()
				self.xx_dbg("xx_set_lg_compute_phy_addr:" + self.m_lg_ptr)
				self.xx_hard_print("xx_set_lg_compute_phy_addr::logical::" + self.m_lg_ptr)
				self.m_s_addr = self.xx_get_cc(self.m_lg_ptr);
				self.xx_hard_print("xx_set_lg_compute_phy_addr::s_addr::" + self.m_s_addr)
				self.m_phy_addr = DBG_Utils().xx_getAsPtr(self.m_s_addr)
				self.xx_hard_print( "xx_set_lg_compute_phy_addr::physical::" + self.m_phy_addr)		
				self.m_class_ptr = self.xx_get_class_ptr_by_phy_addr("")
				self.xx_hard_print( "xx_set_lg_compute_phy_addr::m_class_ptr::" + self.m_class_ptr)
				self.xx_set_stored_class_ptr_by_phy_addr( self.m_class_ptr )
			except:
				self.xx_exception("xx_set_lg_compute_phy_addr::exception:" + p_logical_addr)
				
			
		def xx_compute_generic_phy_by_parent(self, pparent, pvariable,pprefix,sdbg=''):
			try:
				self.xx_dbg( "xx_compute_phy_by_parent::method_in::")
				self.m_parent = pparent
				self.m_raw_variable = pvariable
				self.m_phy_addr = self.get_0_addr()
				lparaddr = pparent.xx_get_class_ptr_by_phy_addr("")
				if(pvariable=="SELF"):
					ptr_by_parent = pprefix + "((" + lparaddr + "))"
				else:					
					ptr_by_parent = pprefix + "((" + lparaddr + ")->" + pvariable + ")"
					
				s_ptr = "((" + self.xx_get_full_class_name("") +"*)" + ptr_by_parent + ")"
				
				self.xx_dbg( "PTR:" + s_ptr)
				
				self.m_lg_ptr = s_ptr			
				s_addr = self.xx_get_cc(self.m_lg_ptr);
				self.m_phy_addr = DBG_Utils().xx_getAsPtr(s_addr)								
				self.xx_set_stored_class_ptr_by_phy_addr( self.xx_get_class_ptr_by_phy_addr(""))
			except:
				self.xx_exception("xx_compute_generic_phy_by_parent::exception::" +  "[pvariable:" + pvariable + "][pprefix:" + pprefix)

		def xx_compute_generic_phy_by_phy(self,pparent, ptr_by_phy, pvariable,sdbg=''):
			try:
				self.xx_dbg( "xx_compute_phy_by_parent::method_in::")
				self.m_raw_variable = pvariable
				self.m_parent = pparent
				self.m_phy_addr = self.get_0_addr()
				s_ptr = "((" + self.xx_get_full_class_name("") +"*)" + ptr_by_phy + ")"
				
				self.xx_dbg( "PTR:" + s_ptr)
				
				self.m_lg_ptr = s_ptr			
				s_addr = self.xx_get_cc(self.m_lg_ptr);
				self.m_phy_addr = DBG_Utils().xx_getAsPtr(s_addr)								
				self.xx_set_stored_class_ptr_by_phy_addr( self.xx_get_class_ptr_by_phy_addr(""))
			except:
				self.xx_exception("xx_compute_generic_phy_by_parent::exception::" +  "[pvariable:" + pvariable + "][pprefix:" + pprefix)
						
		def xx_get_stored_class_ptr_by_phy_addr(self,sdebug=''):
			self.xx_dbg( "DBG_MemoryPtr::xx_get_stored_class_ptr_by_phy_addr::method_in::")
			return self.m_stored_class_ptr_by_phy_addr
		
		def xx_set_stored_class_ptr_by_phy_addr(self,saddr,sdebug=''):
			self.m_stored_class_ptr_by_phy_addr = saddr
			
		def xx_set_lg_ptr(self,p_ptr):
				self.m_lg_ptr = p_ptr

		def xx_get_lg_ptr(self,p_ptr):
				self.xx_dbg("xx_get_lg_ptr:" + self.m_lg_ptr)
				return self.m_lg_ptr

		def xx_compute_phy_from_lg_ptr(self):
			s_addr = self.xx_get_cc(self.m_lg_ptr);
			self.m_phy_addr = DBG_Utils().xx_getAsPtr(s_addr)

		#
		#	addr end
		#=================================================================
		
		def xx_set_phy_addr(self,p_phy_addr):
				self.m_phy_addr = p_phy_addr

		def xx_get_phy_addr(self,p_phy_addr):
				return self.m_phy_addr 

		def xx_set_class_name(self,p_class_name):			
			self.m_class_name = p_class_name

		def xx_set_full_class_name(self,p_class_name):			
			self.m_full_class_name = p_class_name

		def xx_get_full_class_name(self,p_class_name):
			s_cn = self.xx_get_iastora_ver(self.m_full_class_name)
			return s_cn
		

		def xx_get_iastora_ver(self,p_full_class_name):
			self.xx_dbg( "DBG_MemoryPtr::xx_get_iastora_ver::in::" + str(p_full_class_name))
			s_cn = p_full_class_name
			
			if( s_cn.find("hiber_iastora")>=0):
				return s_cn
				
			self.m_sys_name = DBG_PrintConfig().getItem().m_sys_name
			if( self.m_sys_name != ""):				
				s_cn = p_full_class_name				
				s_cn = s_cn.replace("iastora!",self.m_sys_name + "!")				
			else:
				self.xx_dbg( "DBG_MemoryPtr::not_dump_mode::")
				
			self.xx_hard_print( "DBG_MemoryPtr::xx_get_iastora_ver::out::" + str(s_cn))
			self.xx_dbg( "DBG_MemoryPtr::xx_get_iastora_ver::out::" + str(s_cn))
			return s_cn

		def xx_set_variable(self,p_variable):                        
				self.m_variable = p_variable

		def xx_set_parent(self,p_parent):                        
				self.m_parent = p_parent

		def xx_get_class_ptr_by_phy_addr(self,sdbg):
			try:
				s_ptr = "((" + self.xx_get_full_class_name("") +"*)0x" + self.xx_get_phy_addr("") +")";
				self.m_stored_class_ptr_by_phy_addr = s_ptr;
				return s_ptr
			except:
				self.xx_exception("xx_print_ptr::exception::")
				
		def xx_get_class_value_by_phy_addr(self,sdbg):
			try:
				s_ptr = "((" + self.xx_get_full_class_name("") +"*)0x" + self.xx_get_phy_addr("") +")";
				self.m_stored_class_ptr_by_phy_addr = s_ptr;
				return s_ptr
			except:
				self.xx_exception("xx_print_ptr::exception::")
			
		def xx_get_class_ptr(self,sdbg):
			s_ptr = "((" + self.xx_get_full_class_name("") +"*)0x" + self.xx_get_phy_addr("") +")";
			self.xx_dbg( "DBG_MemoryPtr::xx_print_ptr::xx_get_class_ptr::" + s_ptr)
			return s_ptr

		def xx_print_int(self,svariable,stitle,stabs=0):
			""" not_used """
			print "not_used_method::xx_print_int"
			#DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( str(self.m_tabs)
			#DBG_WdbgItemsPrinter().xx_print_int(self.xx_get_class_ptr(""),svariable,stitle,self.xx_gett(stabs))
			
		def xx_print_ptr(self,sdbg):
			try:
				self.xx_dbg( "DBG_MemoryPtr::xx_print_ptr::method_in::")
				
				dd_dbg = DBG_BaseDbgPrinter(self,"DBG_MemoryPtr")
				dd_dbg.prepare_object()
				dd_dbg.print_object()
				
				dd_html = DBG_BaseHtmlPrinter(self,"DBG_MemoryPtr")
				dd_html.set_parent(self)
				dd_html.prepare_object()
				dd_html.print_object()
				
				self.m_path_object = DBG_ParentsPathSeeker(self,"DBG_MemoryPtr")
				self.m_path_object.set_parent(self)
				self.m_path_object.prepare_object()
				self.m_path_object.print_object()
				
				
				dd_state = DBG_StatePrinter(self,"DBG_MemoryPtr")
				dd_state.set_parent(self)
				dd_state.prepare_object()				
				dd_state.print_object()

				
				self.m_class_printer.set_parent(self)
				self.m_class_printer.prepare_object()
				self.m_class_printer.print_object()
				
				self.xx_dbg( "DBG_MemoryPtr::xx_print_ptr::method_out:")
			except:
				self.xx_exception("xx_print_ptr::exception::")				
		
		def xx_get_full_path(self):
			try:
				s_path = self.m_path_object.get_full_path()
				return s_path
			except:
				return "path_exception"

			
		def xx_get_int_ptr(self,svar):
			try:
				self.xx_dbg( "DBG_MemoryPtr::xx_get_int_ptr::method_in::")
				sval = DBG_Utils().xx_getAsInt("@@C++((" + self.xx_get_class_ptr("") + ")." + svar + ")")
				return sval
			except:
				self.xx_exception("xx_get_int_ptr::exception::")
				return -1
			
		def xx_print_t(self,svariable, stabs=0):
			DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( self.xx_gett(stabs) + svariable)
			
		def xx_print_str(self,pparent,svariable, stabs=0):
			self.m_parent = pparent
			DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( pparent.xx_gett(stabs) + svariable)
			
		def xx_raw_print_state(self,ss):
			DBG_MainPrintDispatcher.xx_print_raw_and_write_div ( ss )
			
		def xx_gett(self, stabs):
			try:
				if(stabs == ""):
					stabs = 0
					
				if(self.m_tabs== ""):
					self.m_tabs = 0
				ltabs = 6
				try:
					ltabs = self.m_tabs + stabs
				except:
					ltabs = 6
				return DBG_WdbgItemsPrinter().get_tabs_from_int( ltabs )
			
			except:
				self.xx_exception("[exc][xx_gett]")
				

		def set_fields_parent(self, pparent):
			self.xx_dbg("DBG_MemoryPtr::set_fields_parent")
			#self.m_parent = pparent
			#self.m_fields.set_parent( pparent )
			
		def add_int(self,ss):
			self.xx_dbg("DBG_MemoryPtr::add_int")
			#self.m_fields.add_int(ss)
			
		def set_addr_arr(self,pparent,pvar):
				try:                
						self.xx_dbg("DBG_MemoryPtr::create_arr_adr::in")
						self.m_parent = pparent
						self.xx_inc_tabs(pparent);                
						self.xx_compute_arr_phy_by_parent(pparent,pvar)
						self.xx_dbg("DBG_MemoryPtr::create_arr_adr::out::")
				except:
						self.xx_exception("DBG_MemoryPtr::::set_addr_arr::exception::")


		def initialize_arr_by_addr(self, pitem, pparent, pfullclassname, prange):						
				pitem.xx_set_full_class_name ( pfullclassname )
				pitem.set_addr(pparent, "SELF")
				pitem.set_range( prange )
				pitem.prepare_object()
						
		def set_addr(self,pparent,pvar):
				try:                                
						self.xx_dbg("DBG_MemoryPtr::create_arr_adr::in")
						self.m_parent = pparent
						self.xx_inc_tabs(pparent);                
						self.xx_compute_phy_by_parent(pparent,pvar)
						self.xx_dbg("DBG_MemoryPtr::create_arr_adr::out::")
				except:
						self.xx_exception("DBG_MemoryPtr::::set_addr::exception::")
				
		def print_object_not_valid(self,sdbg):
				try:
					tabs = self.xx_gett(1)
					sout = "OBJ_NOT_VALID[" + sdbg + "]"					
					self.m_messages.add_message(sout)
				except:
					self.xx_exception("[print_object_not_valid][exception]")
					
		def print_object_not_used(self,sdbg):
				try:
						sout = "[OBJ_NOT_USED][" + sdbg + "]"						
						self.m_messages.add_message(sout)
				except:
					self.xx_exception("[print_object_not_valid][exception]")

		def print_object_is_used(self,sdbg):
				try:
						sout = "[OBJ_IS_USED][" + sdbg + "]"
						self.m_messages.add_message(sout)
				except:
					self.xx_exception("[print_object_not_valid][exception]")


		def xx_check_int(self, parent, svar):
			return DBG_MemoryTools().xx_check_int(parent,svar)

		def xx_check_str(self, parent, svar,slen):
			return DBG_MemoryTools().xx_check_str(parent,svar,slen)
		
		def xx_check_u32(self, parent, svar):
			return DBG_MemoryTools().xx_check_u32(parent,svar)
		
		def class_str(self):
			sii = self.__class__.__name__			
			return sii
		
		def xx_print_start(self,pss=""):
			try:
				self.xx_dbg("DBG_MemoryPtr::xx_print_start::in::")
				sout = DBG_ParentsPathSeeker(self,"xx_print_start").get_object_title(self)
				DBG_Html.xx_print_class_start(sout,self.class_str())
				self.xx_dbg("DBG_MemoryPtr::xx_print_start::out::")
			except:
					self.xx_exception("[DBG_MemoryPtr::xx_print_start][exception]")

		def clear_messages(self):
			try:
				self.xx_dbg("DBG_MemoryPtr::clear_messages::in::")
				self.m_messages.clear_messages()
				self.xx_dbg("DBG_MemoryPtr::clear_messages::out::")
			except:
					self.xx_exception("[DBG_MemoryPtr::xx_print_end][exception]")
					
		def xx_print_end(self, pss=""):
			try:
				self.xx_dbg("DBG_MemoryPtr::xx_print_end::in::")
				self.m_messages.print_object("system_messages")
				self.m_exceptions.print_object()		
				DBG_Html.xx_print_class_end(self.class_str())			
				self.xx_dbg("DBG_MemoryPtr::xx_print_end::out::")
			except:
					self.xx_exception("[DBG_MemoryPtr::xx_print_end][exception]")

		def xx_dis(self, pss=""):
			try:
				self.xx_dbg("DBG_MemoryPtr::xx_dis::in::")
				sc = self.class_str()
				DBG_Html.xx_dis(sc)			
				self.xx_dbg("DBG_MemoryPtr::xx_dis::out::")
			except:
					self.xx_exception("[DBG_MemoryPtr::xx_dis][exception]")

		def xx_die(self, pss=""):
			try:
				self.xx_dbg("DBG_MemoryPtr::xx_die::in::")
				DBG_Html.xx_die(self.class_str())
				self.xx_dbg("DBG_MemoryPtr::xx_die::out::")
			except:
					self.xx_exception("[DBG_MemoryPtr::xx_die][exception]")
					
		def xx_lis(self, pss=""):
			try:
				self.xx_dbg("DBG_MemoryPtr::xx_dis::in::")
				sc = self.class_str()
				DBG_Html.xx_lis(sc)			
				self.xx_dbg("DBG_MemoryPtr::xx_dis::out::")
			except:
					self.xx_exception("[DBG_MemoryPtr::xx_lis][exception]")
					
		def xx_lie(self, pss=""):
			try:
				self.xx_dbg("DBG_MemoryPtr::xx_dis::in::")
				sc = self.class_str()
				DBG_Html.xx_lie(sc)			
				self.xx_dbg("DBG_MemoryPtr::xx_dis::out::")
			except:
					self.xx_exception("[DBG_MemoryPtr::xx_lie][exception]")			

		#===============================================
		#
		# 					logging
		#
		#===============================================

		def xx_exc(self,symbol,method=""):				
			self.xx_exception(symbol,method)
			
		def xx_exception(self,symbol,method=""):
				s_ex = ""
				try:
					s_ex = "[" + str(method) + "][" +"[excp:" + str(symbol) + "]"					
					#self.m_exceptions.add_exception( s_ex )
					#DBG_ParentsPathSeeker(self,"DBG_MemoryPtr").add_exc_to_full_path(self,s_ex)
				except:
					s_ex = "error_in_xx_exception"					
					
						
				DBG_Log().xx_exc(s_ex)				
				
		def xx_exception_if_all(self,symbol,desc):
			self.xx_exception(symbol, desc)
				
		def xx_dbg(self,ss):
			DBG_Log().xx_dbg("[" + self.m_class_name + "]"+ ss)
			
		def x_dbg(self,ss):
			DBG_Log().xx_dbg("[" + self.m_class_name + "]" + ss)
			
		def add_exc_to_path(self, tt):			
			self.m_number_of_child_ex = self.m_number_of_child_ex +1
			
		def get_parent_tabs(self, parent,ii_tabs):
				tabsp = ""                                        
				try:
						self.xx_dbg("DBG_MemoryPtr::get_parent_tabs::in::")
						
						if(parent != None):
								if(hasattr(parent, 'xx_gett')):
										tabsp = parent.xx_gett(ii_tabs)
						self.xx_dbg("DBG_MemoryPtr::get_parent_tabs::out::")
						return tabsp   
				except:                        
						self.xx_exception("DBG_MemoryPtr::get_parent_tabs:exc::")                        
						return tabsp

		def add_message_global(self,tt):
			self.m_messages.add_message(tt)
			DBG_MainInformationsSet(self,"xx_exc").add_information ( tt )
					
		def add_message(self,tt):
			self.m_messages.add_message(tt)
			


		#tmp
		def xx_get_iastora_ver__(self,p_full_class_name):
			self.m_is_inbox = DBG_PrintConfig().getItem().m_is_inbox
			if(self.m_is_inbox == 1):
				s_cn = p_full_class_name				
				s_cn = s_cn.replace("iastora!","iastorav!")
				
			else:
				self.xx_dbg( "DBG_MemoryPtr::not_inbox_mode::")
				
				
			self.m_is_dump = DBG_PrintConfig().getItem().m_is_dump
			
			if( self.m_is_dump == 1):				
				s_cn = p_full_class_name				
				s_cn = s_cn.replace("iastora!","dump_iastora!")
				
			else:
				self.xx_dbg( "DBG_MemoryPtr::not_dump_mode::")
				
		def xx_hard_print(self , tt ):
			""" """
			if(self.m_hard_hard_print==1):
				print tt
			