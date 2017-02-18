#!/opt/csw/bin/python2.6
#!/usr/bin/python
import fileinput, glob, string, sys, os, shutil, subprocess, optparse, re, logging, pwd
from datetime import datetime, date, time

#import os,sys,re,pwd,logging
#import subprocess

#==================================================================
#
#								Class JT_Service
#
#==================================================================

class JT_Service:
	def __init__(self):
		self.m_Port =""
		self.m_ServiceName=""
	
#==================================================================
#
#								Class JTBashGeneric
#
#==================================================================

class JT_EnvironmentsData:
	def __init__(self):
		self.m_services = []
		
#==================================================================
#
#==================================================================
		
	def define_services(self):
		self.add_service(self.m_services,"WebGui","18180")
		self.add_service(self.m_services,"WebGui_Http","http://gdnssun23:18180/kgr/")
		
#==================================================================
#
#==================================================================

	def define_services_kgrStart(self):
		self.add_service(self.m_services,"WebGui","50000")
		self.add_service(self.m_services,"WebGui_Http","http://ptxslvsup01:50000/kgr")
#==================================================================
#
#==================================================================

		
	def add_service(self,plist,pport,pname):
		plist.append(self.get_service(pport,pname))
#==================================================================
#
#==================================================================

		
	def get_service(self,pport,pname):
		ds = JT_Service()
		ds.m_Port = pport
		ds.m_ServiceName=pname
		return ds;

#==================================================================
#
#==================================================================

def singleton(cls):
    instances = {}                                  
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()                  
        return instances[cls]
    return getinstance
    
#==================================================================
#
#==================================================================

class JT_Logger:

#==================================================================
#
#==================================================================
		
	@staticmethod	
	def trace_hard_level_20( tt):
		"""trace_hard_level_20"""
			#print tt
			#JT_StaticLogger.exetute_logging( tt )
#==================================================================
#
#==================================================================
			
	@staticmethod			
	def trace_method(tt):
		"""trace_method"""
		#print tt
		#JT_StaticLogger.exetute_logging( tt )
#==================================================================
#
#==================================================================
		
	@staticmethod	
	def trace_hard_level_19( tt):
		"""trace_hard_level_19"""
		#print tt
		#JT_StaticLogger.exetute_logging( tt )
		
#==================================================================
#
#==================================================================

	@staticmethod	
	def trace_hard_level_18( tt):
		"""trace_hard_level_18"""
		#print tt
		#JT_StaticLogger.exetute_logging( tt )
		
#==================================================================
#
#==================================================================
		
	@staticmethod	
	def trace_hard_level_17( tt):
		"""trace_hard_level_17"""
		#print tt
		#JT_StaticLogger.exetute_logging( tt )
		
#==================================================================
#
#==================================================================
		
	@staticmethod	
	def trace_hard_level_16( tt):
		"""trace_hard_level_16"""
		#print tt
		#JT_StaticLogger.exetute_logging( tt )

#==================================================================
#
#==================================================================

	@staticmethod	
	def print_to_log_only( tt):
		"""print_to_log_only"""		
		JT_StaticLogger.exetute_logging(tt)
		
#==================================================================
#
#==================================================================

	@staticmethod	
	def print_output( tt):
		"""print_output"""
		print tt
		JT_StaticLogger.exetute_logging(tt)
    
#==================================================================
#
#					JT_StaticLogger
#
#==================================================================

class JT_LoggerHelperGlobal:
	_shared_state_ = {}
	m_log = logging.getLogger("finder_0")			
	
#==================================================================
#
#==================================================================
			
	def __init__(self):
		self.__dict__ = self.__shared_state		
		
#==================================================================
#
#==================================================================
		
	def log_init(self):
		self.m_log.setLevel(logging.DEBUG)
		self.m_log.setLevel(logging.INFO)
		
#==================================================================
#
#					JT_StaticLogger
#
#==================================================================
	
class JT_StaticLogger:

#==================================================================
#
#==================================================================
	
	@staticmethod
	def setup_logging():
	
		JT_Os.run_subprocess_popen_strip("mv /rksup/config/kgr35jut/jut/python/finder_log/*.txt /rksup/config/kgr35jut/jut/python/finder_log/bck/")
		dt = datetime.now()
		ff = "/rksup/config/kgr35jut/jut/python/finder_log/finder_logY" + str(dt.year) + "M" + str(dt.month) + "D" + str(dt.day) + "H" + str(dt.hour) + "M" + str(dt.minute) + "S" + str(dt.second) + ".txt"	
		l = logging.INFO
		logging.basicConfig(level=l, filename=ff)		 			
		
#==================================================================
#
#==================================================================
		
	@staticmethod
	def exetute_logging(tt):		
		logging.info(tt)
	

#==================================================================
#
#==================================================================

class JT_Printer:
	@staticmethod	
	def DEF_PRINT_LINE():
		return 0
		
#==================================================================
#	what is it with it
#==================================================================
		
class JT_Strings:

	@staticmethod	
	def find_word_rx(w,line):     
		d_out= re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search (line)		
		if d_out:
			return 1		
		return -1
			
#==================================================================
#
#==================================================================
	
	@staticmethod		
	def find_word(line,w):     
		return JT_Strings.find_word_basic(line,w)
		#return JT_Strings.find_word_rx(line,w)
		
#==================================================================
#
#==================================================================
		
	@staticmethod		
	def find_word_basic(line,w):     
		return line.find(w)
	

#==================================================================
#
#				JT_Os
#
#==================================================================
	
class JT_Os:
	@staticmethod
	def run_subprocess_popen_strip(cmd):
	    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	    out = p.stdout.read().strip()
	    return out
		
#==================================================================
#
#==================================================================
	@staticmethod
	def get_euser() :
		"""returns effective user name used to run the script"""
		return pwd.getpwuid(os.getuid())[0]
		
#==================================================================
#
#==================================================================
	@staticmethod
	def get_ps_list() :		
		"""internal method, not to be called from outside the class"""
		JT_Logger.trace_method("[INFO_METHOD_IN].get_ps_list")
		return JT_Os.run_os_command(["ps","-ef"])
		
#==================================================================
#
#==================================================================
	@staticmethod	
	def run_os_command(cmd) :
		JT_Logger.trace_method("[INFO_METHOD_IN].run_os_command")
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return proc.communicate()[0]
		
#==================================================================
#
#==================================================================
	@staticmethod	
	def get_procinfo_from_ps_line(ps_line,pid_ps_regex) :	
		"""returns a tuple (user,PID)"""
		JT_Logger.trace_method("[INFO_METHOD_IN].get_procinfo_from_ps_line")		
		return pid_ps_regex.search(ps_line).group(1), pid_ps_regex.search(ps_line).group(2)
		
#==================================================================
#
#==================================================================

	@staticmethod
	def is_instance_for_pid(user,pid,instance,executed_user) :
		JT_Logger.trace_method("[INFO_METHOD_IN].get_instance_from_piduser:" + user + "][pid:" + str(pid) + "]")
		if user == executed_user :
			cmd = ["pargs",str(pid)]
		else :
			#cmd = ["ssh","-l",user,"localhost","pargs",pid] 
			cmd = ["pargs",str(pid)]

		JT_Logger.trace_hard_level_16("[CMD]")			
		JT_Logger.trace_hard_level_16(cmd)
		
		output = JT_Os.run_os_command(cmd)
		
 		if JT_Strings.find_word(output, instance) > -1:
 			return 1
 		
		cmd.insert(len(cmd)-1,"-e")
		output = JT_Os.run_os_command(cmd)
		
 		if JT_Strings.find_word(output, instance) > -1:
 			return 1
 			
 		return -1
 		
 		
#==================================================================
#
#==================================================================
	@staticmethod
	def get_instance_from_pid_old(self,user,pid) :
		JT_Logger.trace_method("[INFO_METHOD_IN].get_instance_from_pid_old:" + user + "][pid:" + pid + "]")
		if user == self.euser :
			cmd = ["pargs",pid]
		else :			
			cmd = ["ssh","-l",user,"localhost","pargs",str(pid)] 
			
		output = self.run_os_command(cmd)
		srch = self.kgr_regex.search(output)
		if srch and srch.group(0) in self.instances :
			return srch.group(0)
		else :
			cmd.insert(len(cmd)-1,"-e")
			output = self.run_os_command(cmd)
			srch = self.kgr_regex.search(output)
			if srch and srch.group(0) in self.instances :
				return srch.group(0)
			else :
				print "[dev] " + str(cmd)
				print "[dev] unknown KGR instance for process " + pid
				return None
#==================================================================
#
#==================================================================
			
class JT_PsLine:	
	def __init__(self):
		self.m_Line = ""

#==================================================================
#
#==================================================================

				
class JT_PsLines:
	def __init__(self):
		self.m_ps_lines = []
	
#==================================================================
#
#==================================================================
	
	def add_ps_line(self,pline):
		dd = JT_PsLine()		
		dd.m_Line = pline
		self.m_ps_lines.append(dd)
		
		
#==================================================================
#
#==================================================================

	def internal_init(self):
		m_ps_lines=[]
		
#==================================================================
#
#==================================================================
				
	def get_ps_line(self,name):
		dd = JT_PsLine()		
		return dd
		
#==================================================================
#
#==================================================================
		
	def add_ps_line(self,p_env):
		self.m_ps_lines.append(p_env)
		
#==================================================================
#
#==================================================================
	
class JT_ProcessDef :
	def __init__(self):
		self.m_PID = ""
		self.m_ServerName ="NN"
		self.m_State="0"
		self.m_KgrInstance = ""
		self.m_User = ""
		self.m_Counters = 0	
		self.m_LineOfProcess = ""
		
	def __cmp__(self,other):         
		cc =  cmp(self.m_KgrInstance,other.m_KgrInstance) 
		if cc != 0:
			return cc			
		cc1 = cmp(self.m_ServerName,other.m_ServerName)
		return cc1
		
#==================================================================
#
#==================================================================
				
	def print_process(self):
	
		line = ""
		if JT_Printer.DEF_PRINT_LINE()	== 1:
			line = self.m_LineOfProcess
			
		ll = "[KgrInstance:" + self.m_KgrInstance + "][ServerName:" + self.m_ServerName + "][USER:" +  " " + self.m_User + "][PID:" + str(self.m_PID) + "][line:" + line + "]"
		JT_Logger.print_output( ll )
		
#==================================================================
#
#==================================================================

	def print_process_to_log(self):
		line = self.m_LineOfProcess
		ll = "[KgrInstance:" + self.m_KgrInstance + "][ServerName:" + self.m_ServerName + "][USER:" +  " " + self.m_User + "][PID:" + str(self.m_PID) + "][line:" + line + "]"
		#JT_Logger.print_output( ll )
		JT_StaticLogger.exetute_logging( ll )
						
#==================================================================
#
#==================================================================

class JT_ProcessesDef :
	def __init__(self):
		self.m_processess = []	
	
#==================================================================
#
#==================================================================
	
	def __init__ (self):
		self.m_processess = []	
		
#==================================================================
#
#==================================================================
		
	def add_process_to_processes(self,pp):
		self.m_processess.append(pp)

#==================================================================
#
#==================================================================
		
	def print_processess(self):
		for dd_pp in self.m_processess:
			dd_pp.print_process()
		
	
#==================================================================
#
#==================================================================

class JT_ServerDef:
	def __init__(self):
		self.m_ServerName = ""
		self.m_ProcessName = ""
		self.m_Processes = JT_ProcessesDef()
		
#==================================================================
#
#==================================================================

class JT_ServersDef:
	def __init__(self):
		self.m_srvs = []
		
#==================================================================
#
#==================================================================
	
	def internal_init_servers_definition(self):	
		JT_Logger.trace_method("[INFO].internal_init_servers_definition.METHOD_IN")
		self.m_srvs.append(self.get_srv("KNS","KGRServer"))
		self.m_srvs.append(self.get_srv("KTS","KGRTaskServer"))
		self.m_srvs.append(self.get_srv("KIS","KGRImportServer"))
		self.m_srvs.append(self.get_srv("KAS","KGRAggregationServer"))
		self.m_srvs.append(self.get_srv("KVS","KGRVaRServer"))
		self.m_srvs.append(self.get_srv("KRMS","KGRRateManagerServer"))
		self.m_srvs.append(self.get_srv("Adapter","KGRAdapter"))
		self.m_srvs.append(self.get_srv("Agent","kglagent"))
		self.m_srvs.append(self.get_srv("Gateway","KGRKondorGatewayServer"))
		self.m_srvs.append(self.get_srv("GUI","KGRWebApp"))
		self.m_srvs.append(self.get_srv("EMS","tibems")) 
		
#==================================================================
#
#==================================================================
				
	def get_srv(self,name,pname):
		dd = JT_ServerDef()
		dd.m_ServerName= name
		dd.m_ProcessName = pname
		return dd
		
#==================================================================
#
#==================================================================
	
		
	def kpprs_print_data(self):
		#self.m_processess.sort(key=lambda x: x.m_KgrInstance, reverse=False )
		self.m_processess.sort()
		for dd in self.m_processess:
			print dd.m_KgrInstance," " , dd.m_ServerName,  " "  , dd.m_State, " " ,dd.m_User," " , dd.m_Counters, " " , dd.m_PID
		
#==================================================================
#
#==================================================================
		

class JT_KgrInstanceDef:	
	def __init__(self):
		self.m_KgrInstanceName = ""
		self.m_procs_for_kgrinstance = JT_ProcessesDef()
		
#==================================================================
#
#==================================================================
	
class JT_KgrInstancesDef:
	def __init__(self):
		self.m_kgr_instances = []
	
#==================================================================
#
#==================================================================
	def init_kgr_instances(self):
		self.init_kgr_instances_ptx()
#==================================================================
#
#==================================================================
		
	def init_kgr_instances_all(self):
		self.add_kgr_instance("kgr32")
		self.add_kgr_instance("kgr35s")
		self.add_kgr_instance("kgr35b")
		self.add_kgr_instance("kgrSet")
		self.add_kgr_instance("kgr35WebLogic")
		self.add_kgr_instance("kgr35RB")
		self.add_kgr_instance("fatih")
#==================================================================
#
#==================================================================
	
	def init_kgr_instances_gdy(self):
		#self.add_kgr_instance("kgr32")
		self.add_kgr_instance("kgr35s")
		self.add_kgr_instance("kgr35b")
#==================================================================
#
#==================================================================
		
	def init_kgr_instances_ptx(self):
		self.add_kgr_instance("kgr35WebLogic")
		self.add_kgr_instance("kgr35RB")
		self.add_kgr_instance("kgrSet")
		self.add_kgr_instance("fatih")
		self.add_kgr_instance("loki")
		self.add_kgr_instance("pegase")
		self.add_kgr_instance("persee")
		self.add_kgr_instance("riyad")
		self.add_kgr_instance("tcv")
		self.add_kgr_instance("thor")
		self.add_kgr_instance("thrall")
		self.add_kgr_instance("manucfg32")
		self.add_kgr_instance("jupiter")
		
#==================================================================
#
#==================================================================
		
	def add_kgr_instance(self,p_k):	
		dd_i = JT_KgrInstanceDef()
		dd_i.m_KgrInstanceName = p_k
		self.m_kgr_instances.append( dd_i )
		
#==================================================================
#
#
#==================================================================

	def fill_default(self):		
		self.init_kgr_instances()
		
#==================================================================
#
#==================================================================

	def is_kgr_instance_in_line(self, p_line):
		ii = 0
		ii_out = -1;
		for dd_ii in self.m_kgr_instances:
			if JT_Strings.find_word( p_line,dd_ii.m_KgrInstanceName):
				ii_out = ii
				break;				
		return ii_out	
	
#==================================================================
#
#==================================================================
		
	def is_kgr_instance(self, p_instance):
		ii = 0
		ii_out = -1;
		for dd_ii in self.m_kgr_instances:
			if dd_ii.m_KgrInstanceName == p_instance:
				ii_out = ii
				break;				
		return ii_out	
		
#==================================================================
#				JT_MonitorOs
#==================================================================
			
class JT_MonitorKgr:

	def print_end(self):
		"""print_end"""
		print '====================================='

	def __init__(self):
		self.m_servers = JT_ServersDef()
		self.m_kgr_def_instances = JT_KgrInstancesDef()
		self.m_ps_lines = JT_PsLines()
		self.m_founded_processes = JT_ProcessesDef()						
		self.output = [] 
		self.output_lines = []
		self.kgr_regex = []
		self.pid_ps_regex = []
		self.raw_instances = []
		self.euser = ""
		self.instances = []		
		
		
#==================================================================
#
#==================================================================
		
	def fill_environments(self,p_serv) :
		"""returns list of KGR instances, elements of which are running"""
		JT_Logger.trace_method("[INFO_METHOD_IN].fill_environments")		
		#self.m_kgr_def_instances.fill_default()
		if p_serv == "f":
			self.m_kgr_def_instances.init_kgr_instances_ptx()
		if p_serv == "g":
			self.m_kgr_def_instances.init_kgr_instances_gdy()
		
		self.m_servers.internal_init_servers_definition()				
		
		self.pid_ps_regex = re.compile("^\s+(\w+)\s+(\d+)")		
		self.euser = JT_Os.get_euser()
		self.output = JT_Os.get_ps_list()
		
		self.output_lines = self.output.splitlines()
		#self.raw_instances = self.kgr_regex.findall(self.output)
		#instances = list(set(self.raw_instances))  
		#instances.sort()
		
				
		for line in self.output_lines :
			JT_Logger.trace_hard_level_20("[INFO]" + line)
			self.m_ps_lines.add_ps_line(line)
			
#==================================================================
#
#==================================================================
			
	def fill_servers_in_env(self):		
		JT_Logger.trace_method("[INFO_METHOD_IN].fill_servers_in_env")
		JT_Logger.trace_hard_level_20("[INFO].fill_servers_in_env_IN_METHOD")
		was_printed = 0		
		for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:						
			count_ii_in = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)
			JT_Logger.trace_hard_level_20("KGR_INSTANCE_FOR_1:" + dd_kgr_instance.m_KgrInstanceName + "][count_ii_in:" + str(count_ii_in) + "]")			
			JT_Logger.trace_hard_level_20("[INFO.fill_servers_in_env:1].[" + dd_kgr_instance.m_KgrInstanceName + "]")															
			for dd_server in self.m_servers.m_srvs:			
				JT_Logger.trace_hard_level_20("[INFO].execution of server:[" + dd_server.m_ServerName + "]")										
				for dd_ps_line in self.m_ps_lines.m_ps_lines:			
				
					self.find_processes_for_server(dd_ps_line, dd_server,dd_kgr_instance)
					
					count_ii_out = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)					
					if was_printed == 0:
						if count_ii_out > count_ii_in :
							#self.print_servers_in_env()
							was_printed = 1
					
			count_ii_out = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)
			JT_Logger.trace_hard_level_20("KGR_INSTANCE_FOR_2:" + dd_kgr_instance.m_KgrInstanceName + "][count_ii:" + str(count_ii_out) + "]")

#==================================================================
#
#==================================================================

	def print_servers_in_env(self):		
				JT_Logger.trace_method("[INFO_METHOD_IN].print_servers_in_env")
				for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
					count_ii = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)					
					JT_Logger.print_output("KGR_INSTANCE_START_PRINT_DATA:" + dd_kgr_instance.m_KgrInstanceName + "][count_ii:" + str(count_ii) + "]")
					for dd_process in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
						dd_process.print_process()						
					JT_Logger.print_output("KGR_INSTANCE_END:" + dd_kgr_instance.m_KgrInstanceName + "]")
					
#==================================================================
#
#==================================================================
					
	def print_servers_in_env_to_log(self):		
				JT_Logger.print_to_log_only("[INFO_METHOD_IN].print_servers_in_env")
				for dd_kgr_instance in self.m_kgr_def_instances.m_kgr_instances:
					count_ii = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)					
					JT_Logger.print_to_log_only("KGR_INSTANCE_START_PRINT_DATA:" + dd_kgr_instance.m_KgrInstanceName + "][count_ii:" + str(count_ii) + "]")
					for dd_process in dd_kgr_instance.m_procs_for_kgrinstance.m_processess:
						dd_process.print_process_to_log()
					JT_Logger.print_to_log_only("KGR_INSTANCE_END:" + dd_kgr_instance.m_KgrInstanceName + "]")
	
	
					
#==================================================================
#
#==================================================================
				
	def print_server_info(self,dd_ps_line,dd_server,dd_kgr_instance):			
		"""print_server_info"""
		
#==================================================================
#
#==================================================================
		
	def is_kgr_in_ps(self,	dd_ps_line,kgr_instance_name):
		"""is_kgr_in_ps"""
		dd_out= JT_Strings.find_word(dd_ps_line,kgr_instance_name)			
		return dd_out
			
#==================================================================
#
#==================================================================
	def is_kgr_in_pargs(self,	user,pid,kgr_instance_name,euser):
		"""is_kgr_in_pargs"""
		dd_out = 	JT_Os.is_instance_for_pid(user,pid,kgr_instance_name,euser)
		return dd_out
				
#==================================================================
#
#==================================================================
				
	def find_processes_for_server(self,dd_ps_line,dd_server,dd_kgr_instance):			
		"""fill_server_in_env"""		
		JT_Logger.trace_method("[INFO_METHOD_IN].find_processes_for_server[m_ProcessName:"  + dd_server.m_ProcessName + "][m_KgrInstanceName:" + dd_kgr_instance.m_KgrInstanceName + "][line:" + dd_ps_line + "]")
		count_in = len(dd_kgr_instance.m_procs_for_kgrinstance.m_processess)		
		
		if JT_Strings.find_word(dd_ps_line,dd_server.m_ProcessName) > -1 :
			JT_Logger.trace_hard_level_18("[INFO][ADD_PROCESS_FOUND_PROCESS_IN_LINE][dd_server.m_ProcessName:" + dd_server.m_ProcessName + "]")	
			if self.line_excluded(dd_ps_line) == 0:
				if self.is_kgr_in_ps(dd_ps_line,dd_kgr_instance.m_KgrInstanceName) > -1 :
						user,pid = JT_Os.get_procinfo_from_ps_line(dd_ps_line,self.pid_ps_regex)
						dd_pta = self.get_process_to_add(dd_ps_line,pid,user,dd_kgr_instance,dd_server)						
						JT_Logger.trace_hard_level_18("[INFO][ADD_PROCESS][dd_server.m_ProcessName:" + dd_server.m_ProcessName + "][m_KgrInstanceName:" + dd_kgr_instance.m_KgrInstanceName + "][user:" + user + "][pid:" + pid + "][dd_ps_line:" + dd_ps_line + "]")
						dd_kgr_instance.m_procs_for_kgrinstance.add_process_to_processes(dd_pta)						
						self.m_founded_processes.add_process_to_processes(dd_pta)					
				else:							
					user,pid = JT_Os.get_procinfo_from_ps_line(dd_ps_line,self.pid_ps_regex)
					if self.is_kgr_in_pargs(user,id,dd_kgr_instance.m_KgrInstanceName,self.euser) > -1:
						dd_pta = self.get_process_to_add(dd_ps_line,pid,user,dd_kgr_instance,dd_server)						
						dd_kgr_instance.m_procs_for_kgrinstance.add_process_to_processes(dd_pta)						
						self.m_founded_processes.add_process_to_processes(dd_pta)				
							
			
#==================================================================
#
#==================================================================

	def get_process_to_add(self,line,pid,user,dd_kgr_instance,dd_server):
		JT_Logger.trace_method("[INFO_METHOD_IN].get_process_to_add")
		JT_Logger.trace_hard_level_18("[INFO_METHOD_IN].get_process_to_add")
		dd_pd = JT_ProcessDef()
		dd_pd.m_PID = pid
		dd_pd.m_KgrInstance = dd_kgr_instance.m_KgrInstanceName
		dd_pd.m_ServerName = dd_server.m_ServerName						
		dd_pd.m_User = user
		dd_pd.m_Counters = 1
		dd_pd.m_LineOfProcess = line
		return dd_pd
	
#==================================================================
#
#==================================================================

	def line_excluded(self, line):
		if (line.find(" tail -f ") != -1 or line.find(" tee ") != -1 or line.find("/java/") != -1 ):
			return 1
		return 0


#==================================================================
#
#										OLD THING
#
#==================================================================
		
#	
# Program execution starts here...
#
#logh = JT_LoggerHelper()
#logh.setup_logging()

JT_StaticLogger.setup_logging()

dd2 = JT_MonitorKgr()
dd2.fill_environments("g")
dd2.fill_servers_in_env()
dd2.print_servers_in_env()
dd2.print_servers_in_env_to_log()
dd2.print_end()
#dd2.m_founded_processes.print_processess()

