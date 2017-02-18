#!/opt/csw/bin/python2.6
#!/usr/bin/python

import fileinput, glob, string, sys, os, shutil, subprocess, optparse, re, logging
from datetime import datetime, date, time


from os.path import join
# replace a string in multiple files
#filesearch.py

#==================================================================
#
#								Class JTBashGeneric
#
#==================================================================

class JT_Services:

	m_logger = []
	m_services = []
	
#==================================================================
#
#==================================================================

	def add_logger(self,plogger):
		self.m_logger.append(plogger)
#==================================================================
#
#==================================================================
	
	def logger_print(self,line):
		self.m_logger[0].trace_hard(line)
#==================================================================
#
#==================================================================
		
	def define_services(self):
		self.add_service_o(self.m_services,self.get_service("WebGui","18180"))
#==================================================================
#
#==================================================================

	def add_service_o(self, plist,p_dd):
		plist.append(p_dd)
#==================================================================
#
#==================================================================
		
	def add_service(self, plist, pport, pname):
		plist.append(self.get_service(pport,pname))
#==================================================================
#
#==================================================================
		
	def get_service(self,pport,pname):
		ds = JT_Service()
		ds.m_Port = pport
		ds.m_ServiceName=pname
		return ds
#==================================================================
#
#==================================================================

	def print_services(self):
		for dd_services in self.m_services:
			self.logger_print(dd_services.m_Port + " " + dd_services.m_ServiceName)
			
#==================================================================
#
#								Class JTBashGeneric
#
#==================================================================
			
class JT_Service:
	m_Port =""
	m_ServiceName=""
	

#==================================================================
#
#								Class JTBashGeneric
#
#==================================================================

class JTBashGeneric:
	
	
	#HOLDING_SPOT="""fake_command"""
	
	#Determines Home Directory Usage in Gigs
	HOMEDIR_USAGE = """
	du -sh $HOME | cut -f1
	"""
	
	#Determines IP Address
	IPADDR = """
	/sbin/ifconfig -a | awk '/(cast)/ { print $2 }' | cut -d':' -f2 | head -1
	"""
	
	VERBOSE=False
		
	#==================================================================
	#
	#==================================================================		
	
	def run_subprocess_popen(self,cmd) :
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return proc.communicate()[0]
		
	#==================================================================
	#
	#==================================================================		
	
	def run_subprocess_call(self, cmd):
			subprocess.call(cmd, shell=True)

	
	#==================================================================
	#
	#==================================================================		
	
	def run_os_variable(self, p_var,p_val):
			os.environ[p_var] = p_val
			os.system('python echoenv.py')

		
	#==================================================================
	#
	#==================================================================		
	
	def run_os_popen(self, cmd):
			os.popen(cmd)
	
	#==================================================================
	#
	#==================================================================		
				
	def run_subprocess_popen_strip(self,cmd):
	    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	    out = p.stdout.read().strip()
	    return out
	
		
	#==================================================================
	#
	#==================================================================		
	
	def report(output,cmdtype="UNIX COMMAND:"):
	
	   if self.VERBOSE:
	       print "%s: %s" % (cmdtype, output)
	   else:
	       print output
		
	#==================================================================
	#
	#==================================================================		
	
	
	def controller(self):	    
	    #Create instance of OptionParser Module, included in Standard Library
	    p = optparse.OptionParser(description='A unix toolbox',
	                                            prog='py4sa',
	                                            version='py4sa 0.1',
	                                            usage= '%prog [option]')
	    p.add_option('--ip','-i', action="store_true", help='gets current IP Address')
	    p.add_option('--usage', '-u', action="store_true", help='gets disk usage of homedir')
	    p.add_option('--verbose', '-v',
	                action = 'store_true',
	                help='prints verbosely',
	                default=False)
	
	    #Option Handling passes correct parameter to run_subprocess_popen_strip
	    options, arguments = p.parse_args()
	    if options.verbose:
	        self.VERBOSE=True
	    if options.ip:
	        value = self.run_subprocess_popen_strip(self.IPADDR)
	        report(value,"IPADDR")
	    elif options.usage:
	        value = run_subprocess_popen_strip(self.HOMEDIR_USAGE)
	        report(value, "HOMEDIR_USAGE")
	    else:
	        p.print_help()
	
		
	#==================================================================
	#
	#==================================================================		
	
	def main(self):
	    self.controller()
	
#==================================================================
#
#								Class JTSpace
#
#==================================================================

class JTSpace:
	MESSAGES = "tail /var/log/messages"
	SPACE = "df -h"
	
	cmds = [MESSAGES, SPACE]
	
	def runCommands(selef,commands=cmds):
	    
	    count=0
	    for cmd in cmds:
	        count+=1
	        print "Running Command Number %s" % count
	        subprocess.call(cmd, shell=True)
		

#==================================================================
#
#								Class JTFind
#
#==================================================================
	
class JTFind:

	m_trace = 0
	m_trace_opened_files = 0
	m_trace_hard = 1
	m_stamp=''
	m_execute_replace = 0
	m_log = logging.getLogger("finder_0")	
	m_for = ["0","1","2","3","4","5","6","7","8","9"]
	m_paths = ["/rksup/config/kgr35s"]
	m_log_file = "/rksup/config/kgr35s/finder_log.txt"
	m_paths_config = ["/rksup/config/kgr35s"]		
	m_exts = ["vbgtcyz"]
	
	#==================================================================
	#
	#==================================================================
	
	
	def set_ext_sh_only(self):
		self.m_exts = ["*.sh"]
		
	#==================================================================
	#
	#==================================================================		
	
	def set_ext_all_files(self):
		self.m_exts = ["*.xml","*.cfm","*.conf","*.properties","*.params","*.sh"]
		
	#==================================================================
	#
	#==================================================================
	
	def unset_replace(self):
		self.m_execute_replace = 0
		
	#==================================================================
	#
	#==================================================================
		
	def set_replace(self):
		self.m_execute_replace = 0
		
	#==================================================================
	#
	#==================================================================
		
	def setup_logging(self):			
		JTBashGeneric().run_subprocess_popen_strip("mv /rksup/config/kgr35jut/jut/python/finder_log/*.txt /rksup/config/kgr35jut/jut/python/finder_log/bck/")
		dt=datetime.now()
		ff="/rksup/config/kgr35jut/jut/python/finder_log/finder_logY" + str(dt.year) + "M" + str(dt.month) + "D" + str(dt.day) + "H" + str(dt.hour) + "M" + str(dt.minute) + "S" + str(dt.second) + ".txt"	
		logging.basicConfig(filename=ff) 
		self.m_log.setLevel(logging.DEBUG)
		self.m_log.setLevel(logging.INFO)
		
		
	#==================================================================
	#
	#==================================================================
	
		
		
	def exetute_logging(self,tt):		
		self.m_log.info(tt)
		
	#==================================================================
	#
	#==================================================================
	
		
	def set_paths(self):
		m_paths = ["/rksup/config/kgr35s"]
		
	#==================================================================
	#
	#==================================================================
	
	
	def trace_hard(self, tt):
		self.exetute_logging(tt)
		if self.m_trace_hard == 1:
			print tt
		
	#==================================================================
	#
	#==================================================================
	
				
				
	def trace_open_file(self, tt):
			if self.m_trace_opened_files == 1:
				print tt
				self.exetute_logging(tt)
		
	#==================================================================
	#
	#==================================================================
	

	def trace(self, tt):
			if self.m_trace == 1:
				print tt
				self.exetute_logging(tt)
			
	#==================================================================
	#
	#==================================================================
	
			
	def traceex(self, tt, impose):
			if self.m_trace == 1 or impose == 1:
				print tt
				self.exetute_logging(tt)
				
	#==================================================================
	#
	#==================================================================
	
	def replaceStringInFileEx2(self,filePath, sourceText, replaceText):
		self.trace_hard( "replaceStringInFileEx2:" + filePath + "][" + sourceText + "][" + replaceText + "]")		 
		
		self.trace_hard( filePath )
		tempName=filePath+'~x~'
		backupName=filePath+'.backup'+self.m_stamp
		
		inF = open(filePath,'rb')
		s=inF.read()
		inF.close()
		
		
		outtext=s.replace(sourceText,replaceText)
		s=outtext
		outF = open(tempName,'wb')
		
		#outF.write(outtext.encode('utf-8'))
		
		outF.write(outtext)
		outF.close()
		self.trace_hard("[INFO][create backup]:" + backupName)
		shutil.copy2(filePath,backupName)
		os.remove(filePath)
		os.rename(tempName,filePath)
		
	#==================================================================
	#
	#==================================================================
	
	def replaceStringInFile_nottested(self,filePath,findreplace):
		self.trace_hard( "replaceStringInFile_nottested:" + filePath )
		self.trace_hard( findreplace)
		print filePath
		tempName=filePath+'~x~'
		backupName=filePath+'.backup'
		
		inF = open(filePath,'rb')
		s=unicode(inF.read(),'utf-8')
		inF.close()
		
		for couple in findreplace:
			outtext=s.replace(couple[0],couple[1])
			s=outtext
		outF = open(tempName,'wb')
		outF.write(outtext.encode('utf-8'))
		outF.close()
		
		shutil.copy2(filePath,backupName)
		os.remove(filePath)
		os.rename(tempName,filePath)
		
	#==================================================================
	#
	#==================================================================
	
	def replacetext(self,filePath, sourceText, replaceText):
		self.trace_hard( "replacetext:" + filePath + "][" + sourceText + "][" + replaceText + "]")
		file = open(filePath, "r") 
		text = file.read() 
		file.close() 
		file = open(filePath, "w") 
		file.write(text.replace(sourceText, replaceText)) 		
		file.close() 
    
		
	#==================================================================
	#
	#==================================================================
	
	
	def search(self,stext,path):

		files = glob.glob(path)
		print files
		for line in fileinput.input(files,inplace=1):
			lineno = 0
			lineno = string.find(line, stext)
			if lineno > 0:
				print line
		
	#==================================================================
	#
	#==================================================================
	
			
				
	def searchex_test(self, seeking_text, path,ext):
		cmd = 'find ' + path + ' -name "' + ext + '" -print'         
		print cmd
		
	#==================================================================
	#
	#==================================================================
	

	def execute_replaceex_list(self,seeking_text,replaced_text,paths,exts):
		self.trace_hard( '[execute_replaceex_list:in]:' + "][" + seeking_text + "][" + replaced_text + "]" )
		for p in paths:
			self.traceex( '[INFO.REPLACE_IN_PATHS]:' + p, 1 )
			for e in exts:										
				self.traceex( '[INFO.REPLACE_FOR_TEXT]:' + e, 1 )					
				self.execute_replaceex(seeking_text,replaced_text,p,e)
	
		
	#==================================================================
	#
	#==================================================================
	
		
	def searchex_list(self,seeking_texts,paths,exts):
		self.trace_hard( '[searchex_list:in]:'  )
		for p in paths:
			self.traceex( '[INFO.SEEK_IN_PATHS]:' + p, 1 )
			for e in exts:
				self.traceex( '[INFO.SEEK_IN_EXT]:' + e, 1 )
				for t in seeking_texts:			
					self.traceex( '[INFO.SEEK_FOR_TEXT]:' + t, 1 )					
					self.searchex(t,p,e)

		
	#==================================================================
	#
	#==================================================================
	

	def execute_replaceex(self,seeking_text,replaced_text,path,ext):	
		s_tt = '[def::execute_replaceex:in]:' + "][seeking_text:" + seeking_text + "][replaced_text:" + replaced_text + "][path:" + path + "][ext:"  + ext + "]"
		self.trace_hard( s_tt )
		cmd = 'find ' + path + ' -name "' + ext + '" -print'         
	  
		self.trace( '[INFO]cmd:' + cmd )
		self.trace( '[INFO]seeking_text:' + seeking_text )
		 
	  
		for file in os.popen(cmd).readlines(): 
			num  = 1
			name = file[:-1]                       			
			self.trace( '[INFO]seeking in file:' + name )
			
			for line in open(name).readlines():    
				pos = string.find(line, seeking_text)
				if  pos >= 0:					
					if self.m_execute_replace == 0 :
						self.trace_hard( '[INFO]test.replace_text_in_file:[name:' + name + "][seeking_text:"+ seeking_text +"][replaced_text:" + replaced_text + "]")		
						self.trace_hard( '[INFO]test.replace_text_in_file:' + "[name:" + name + "][num:" + str(num) + "][pos:" + str(pos) + "][line: " + line[:-1] + "]")
					if self.m_execute_replace == 1 :
						self.trace_hard( '[EXED]execute.replace_text_in_file[name:' + name + "[seeking_text:"+ seeking_text +"][replaced_text:" + replaced_text + "]")		
						self.trace_hard( '[EXEC]execute.replace_text_in_file:' + "[name:" + name + "][num:" + str(num) + "][pos:" + str(pos) + "][line: " + line[:-1] +"]")					
						self.replaceStringInFileEx2(name,seeking_text,replaced_text)					
				num = num+1
			
	#==================================================================
	#
	#==================================================================
	
				
	def searchex(self,seeking_text,path,ext):	
		cmd = 'find ' + path + ' -name "' + ext + '" -print'         
	  
		self.trace( '[INFO]cmd:' + cmd )
		self.trace( '[INFO]seeking_text:' + seeking_text )
		 
	  
		for file in os.popen(cmd).readlines(): 
			num  = 1
			name = file[:-1]                       
			self.trace( '[INFO.searchex]seeking in file:' + name )
			self.trace_open_file( '[INFO.searchex]seeking in file:' + name )
			for line in open(name).readlines():    
				pos = string.find(line, seeking_text)
				if  pos >= 0:
					self.trace_hard( '[INFO.searchex]....' + name + " " + str(num) + " " + str(pos) + " " + line[:-1] )
				num = num+1
				
	#==================================================================
	#
	#==================================================================
			
	def find_genstring_genpath(self,port):
		self.trace_hard ( '[find_genstring_genpath][' + port + "][")
		paths = self.m_paths
		seeking_texts = [port]
		exts = self.m_exts
		self.searchex_list(seeking_texts, paths, exts)
		
	#==================================================================
	#
	#==================================================================
	
	def find_genstring_proppath(self,port):
		self.trace_hard ( '[find_genstring_proppath][' + port + "][")
		paths = self.m_paths
		seeking_texts = [port]
		exts = ["*.properties"]
		self.searchex_list(seeking_texts, paths, exts)
	#==================================================================
	#
	#==================================================================
		
	def create_stamp(self):
		self.trace_hard ( '[create_stamp]')
		dt = datetime.now()
		self.m_stamp = "ST_" + str(dt.year) + "_" + str(dt.month) + "_" + str(dt.day) + "_" + str(dt.hour) + "_" + str(dt.minute) + "_" + str(dt.second)
	#==================================================================
	#
	#==================================================================
		
	def replace_generic_in_config(self, seeking_text, replaced_text):
		self.trace_hard ( '[replace_generic]' + seeking_text + "][" + replaced_text + "]")
		paths = self.m_paths_config
		exts = self.m_exts
		self.execute_replaceex_list(seeking_text, replaced_text,paths, exts)
		
	#==================================================================
	#
	#==================================================================
		
	def replace_generic(self, seeking_text, replaced_text):
		self.trace_hard ( '[replace_generic]' + seeking_text + "][" + replaced_text + "]")
		paths = self.m_paths
		exts = self.m_exts
		self.execute_replaceex_list(seeking_text, replaced_text,paths, exts)
	#==================================================================
	#
	#==================================================================
		
	def setenv_db_kgr35s(self):
		self.trace_hard ( 'setenv_db_kgr35s')
		#JTBashGeneric().run_subprocess_popen_strip("setenv DSQUERY GDN_KGR35S")
		#JTBashGeneric().run_subprocess_popen_strip("set DSQUERY GDN_kgr35s")
		JTBashGeneric().run_os_variable("DSQUERY","GDN_KGR35")
	#==================================================================
	#
	#==================================================================
		
	def find_kns(self):
		self.trace_hard ( 'find_kns')
		self.trace_hard (JTBashGeneric().run_subprocess_popen_strip("ps -ef | grep -i kgrser"))
	#==================================================================
	#
	#==================================================================
		
	def startKNS(self):
		self.trace_hard ( 'startKNS')
		self.trace_hard (JTBashGeneric().run_subprocess_popen_strip("/rksup/config/startKNS kgr35s"))
	#==================================================================
	#
	#==================================================================
		
	def tailKNS(self):
		self.trace_hard ( 'tailKNS')		
		self.tail("/rksup/log/kgr35s/KGRServer_master__stdout.log")
	#==================================================================
	#
	#==================================================================

	def tail(self,p_ff):
		self.trace_hard ( 'tail' + p_ff )	
		p_ff.seek(0,2) 
		while True:
			line = p_ff.readline()
			if not line:
				time.sleep(0.1)
				continue
			yield line 
	
	#=============================================================
	#
	#									DEPRECATED
	#
	#=============================================================
	

	def go_throug_all_not_ok(self):
		self.trace_hard(  '[go_throug_all_not_ok]')
		paths = self.m_paths			
		seeking_texts = ["1810","1710","1610"]
		exts = ["*.xml","*.cfm","*.conf","*.properties"]
		
		self.searchex_list(seeking_texts, paths, exts)

	def go_throug_all_ok(self):
		self.trace_hard ('[go_throug_all_not_ok]')
		paths = self.m_paths			
		seeking_texts = ["1815","1715","1615"]
		exts = ["*.xml","*.cfm","*.conf","*.properties"]
		
		self.trace_hard ('[FINDED_OK]')
		self.searchex_list(seeking_texts, paths, exts)

	def go_throug_all_ok_db(self):
		self.trace_hard ('[go_throug_all_not_ok]')
		paths = self.m_paths
		seeking_texts = ["GDN_kgr35s","kgr35s"]
		exts = ["*.xml","*.cfm","*.conf","*.properties"]
		
		self.trace_hard ('[FINDED_OK_DB]')
		self.searchex_list(seeking_texts, paths, exts)

	def go_main(self):
		path = "/rksup/config/kgr35s/jut/python/"
		seeking_text = "print"
		ext = "*.py"
		self.searchex(seeking_text, path, ext)


	def go_throug_all_ok_18152(self):
		self.trace_hard ( '[go_throug_all_ok_18152]')
		self.find_genstring_genpath("18152")

	def find_17150string_genpath(self):
		self.trace_hard ( '[find_17150string_genpath]')
		self.find_genstring_genpath("17150")

		
	def find_17100string_genpath(self):
		self.trace_hard ( '[find_17100string_genpath]')
		paths = self.m_paths
		seeking_texts = ["17100"]
		exts = self.m_exts
		self.searchex_list(seeking_texts, paths, exts)
		
	def test_replace(self):
		self.trace_hard ( '[test_replace]')
		self.replaceStringInFileEx2("/rksup/config/kgr35s/jut/python/test_1715.py", "1715","1750")

	def test_replace_all(self):
		self.trace_hard ( '[test_replace_all]')
		paths = ["/rksup/config/kgr35s/jut/python/test"]
		seeking_text = "17100"
		replaced_text = "17150"
		exts = self.m_exts	
		self.execute_replaceex_list(seeking_text, replaced_text,paths, exts)
		
			
	def replace_ports_for_db_17150_to_17100(self):
		self.trace_hard ( '[replace_ports_for_db_17150_to_17100]')
		paths = self.m_paths
		seeking_text = "17150"
		replaced_text = "17100"
		exts = self.m_exts
		self.execute_replaceex_list(seeking_text, replaced_text,paths, exts)

	def replace_to_kgo(self):
		self.replace_generic("17100","17150")
		self.replace_generic("GDN_kgr35s","GDN_kgr35s")

		
	def find_kgr35s(self):
		cc.find_genstring_genpath("kgr35s")		
		cc.find_genstring_genpath("kgr35s")		
		cc.find_genstring_genpath("1710")		
		
	def find_GDN_kgr35s(self):
		cc.find_genstring_genpath("GDN_kgr35s")		
			
	def find_kgr35s(self):
		cc.find_genstring_genpath("kgr35s")		
		cc.find_genstring_genpath("kgr35s")		
		cc.find_genstring_genpath("1715")		
		
	def find_port_18152(self):
		cc.find_genstring_genpath("18152")
		
	def find_kgr35s_properties(self):
		cc.find_genstring_proppath("kgr35s")		
		cc.find_genstring_proppath("kgr35s")		
		cc.find_genstring_proppath("1715")		

	
	def find_4205(self):
		self.trace_hard ( 'find_4205')		
		cc.find_genstring_genpath("4205")		
		
	def find_04200(self):
		self.trace_hard ( 'find_04200')		
		cc.find_genstring_genpath("04200")
		
	def find_04500(self):
		self.trace_hard ( 'find_04500')		
		cc.find_genstring_genpath("04500")		
		
		
	def find_1X10X(self):
		self.trace_hard ( 'find_1X10X')		
		cc.find_genstring_genpath("1610")		
		cc.find_genstring_genpath("1710")		
		cc.find_genstring_genpath("1810")	
		cc.find_genstring_genpath("1910")		
		
	def find_1915(self):
		self.trace_hard ( 'find_1915')		
		cc.find_genstring_genpath("1915")		
		
	def find_123_110(self):
		self.trace_hard ( 'find_123_110')		
		cc.find_genstring_genpath("123.110")		
		
	def replace_1910_to_1915(self):
		self.trace_hard ( 'replace_1910_to_1915')			
		self.replace_generic_in_config("1910","1915")

	def replace_123_110_to_123_115_in_config(self):
		self.trace_hard ( 'replace_123_110_to_123_115')			
		self.replace_generic_in_config("123.110","123.115")
		
	def replace_123_110_to_123_115(self):
		self.trace_hard ( 'replace_123_110_to_123_115')			
		self.replace_generic("123.110","123.115")

	def replace_04200_04500(self):
		self.trace_hard ( 'replace_04200_04500')			
		self.replace_generic("04200","04500")
		
	def find_kgrLogger(self):
		self.trace_hard ( 'find_kgrLogger')		
		cc.find_genstring_genpath("kgrLogger")		
	
	
	def replace_to_kgr35s(self):
		self.replace_generic("1610","1615")
		self.replace_generic("1710","1715")
		self.replace_generic("1810","1815")
		self.replace_generic("1910","1915")
		self.replace_generic("04200","04500")
		self.replace_generic("04400","04500")


	def find_to_kgr35s(self):
		self.find_genstring_genpath("1610")
		self.find_genstring_genpath("1710")
		self.find_genstring_genpath("1810")
		self.find_genstring_genpath("1910")
		self.find_genstring_genpath("04200")
		self.find_genstring_genpath("04400")
		self.find_genstring_genpath("GDN_kgr35s")
		self.find_genstring_genpath("GDN_kgr35s")

	def find_is_kgr35s(self):
		self.find_genstring_genpath("1615")
		self.find_genstring_genpath("1715")
		self.find_genstring_genpath("1815")
		self.find_genstring_genpath("1915")		
		self.find_genstring_genpath("04500")		
		self.find_genstring_genpath("GDN_kgr35s")
		self.find_genstring_genpath("18150")
		
	def find_42073(self):
		self.find_genstring_genpath("42073")
		self.find_genstring_genpath("18153")
		self.find_genstring_genpath("18159")
		
	def find_1815(self):
		self.find_genstring_genpath("1815")
		
	def replace_42073_to_18159(self):
		self.replace_generic("42073","18159")
		
	#=============================================================
	#
	#									MAIN
	#
	#=============================================================
	
	def replace_generic_from_to_port(self,p_f,p_t,s_f,s_t):
		self.trace_hard ( 'replace_generic_from_to_port')			
		for ii in self.m_for:
			self.replace_generic("161" + p_f + ii,"161" + p_t + ii)
			
		for ii in self.m_for:		
			self.replace_generic("171" + p_f+ii,"171" + p_t + ii)
			
		for ii in self.m_for:					
			self.replace_generic("181" + p_f + ii,"181" + p_t + ii)
			
		for ii in self.m_for:				
			self.replace_generic("191" + p_f + ii,"191" +p_t + ii)		
		
		self.replace_generic("42073","181" + p_t + "9")
		self.replace_generic("kgr35" + s_f,"kgr35" + s_t)
		self.replace_generic("123.11" + p_f,"123.11" + p_t)
		self.replace_generic("GDN_KGR35"+ str.upper(s_f),"GDN_KGR35" + str.upper(s_t))
		self.replace_generic("GDN_kgr35"+ str.upper(s_t),"GDN_KGR35" + str.upper(s_t))
		self.replace_generic("GDN_kgr35"+ str.upper(s_t),"GDN_KGR35" + str.upper(s_t))
	#==================================================================
	#
	#==================================================================
	
	def replace_generic_to_kgr35s_from_kgr35b(self):		
		self.trace_hard ( 'replace_generic_to_kgr35s_from_kgr35b')			
		self.replace_generic_from_to_port("0","8","b","s")
	
	#==================================================================
	#
	#==================================================================
	
	def replace_generic_to_kgr35s_from_kgr35b(self):		
		self.trace_hard ( 'replace_generic_to_kgr35s_from_kgr35r')			
		self.replace_generic_from_to_port("0","8","b","s")
		
	#==================================================================
	#
	#==================================================================
	
	def replace_generic_to_kgr35s_from_kgr35r(self):		
		self.trace_hard ( 'replace_generic_to_kgr35s_from_kgr35r')			
		self.replace_generic_from_to_port("7","8","r","s")
	#==================================================================
	#
	#==================================================================
	
	def replace_to_kgr35s_1(self):
		self.trace_hard ( 'replace_to_kgr35s_1')			
		for ii in self.m_for:
			self.replace_generic("1617"+ii,"1618"+ii)
			
		for ii in self.m_for:		
			self.replace_generic("1717"+ii,"1718"+ii)
			
		for ii in self.m_for:					
			self.replace_generic("1817"+ii,"1818"+ii)
			
		for ii in self.m_for:				
			self.replace_generic("1917"+ii,"1918"+ii)		
		
		self.replace_generic("42073","18189")			
		self.replace_generic("kgr35r","kgr35s")
		self.replace_generic("123.110","123.118")
		self.replace_generic("GDN_KGR35R","GDN_KGR35S")
		self.replace_generic("GDN_kgr35r","GDN_KGR35S")
		self.replace_generic("GDN_kgr35s","GDN_KGR35S")
		
	#==================================================================
	#
	#==================================================================
		
	def replace_to_kgr35s_2(self):
		self.trace_hard ( 'replace_to_kgr35s_2')			
		self.replace_generic("kgr35r","kgr35s")
		self.replace_generic("GDN_kgr35r","GDN_KGR35S")
		self.replace_generic("GDN_kgr35s","GDN_KGR35S")
	#==================================================================
	#
	#==================================================================

	def replace_to_kgr35s_repair_last(self):
		self.replace_generic("GDN_KGR35R","GDN_KGR35S")
	#==================================================================
	#
	#==================================================================

	def find_to_kgr35s(self):
		self.find_genstring_genpath("1610")
		self.find_genstring_genpath("1710")
		self.find_genstring_genpath("1810")
		self.find_genstring_genpath("1910")
		self.find_genstring_genpath("04200")
		self.find_genstring_genpath("04400")
		self.find_genstring_genpath("GDN_kgr35s")
		self.find_genstring_genpath("GDN_KGR35")
	#==================================================================
	#
	#==================================================================

	def trace_header(self,ss):
		self.trace_hard ( 'find_basename')			
		self.trace_hard ( '/*==================================================================*/')
		self.trace_hard ( '/*')			
		self.trace_hard ( '/*                            ' + ss)			
		self.trace_hard ( '/*')			
		self.trace_hard ( '/*==================================================================*/')

	#==================================================================
	#
	#==================================================================
	
	def find_basename_generic_kgr35b(self):
		self.find_basename_generic("0","B")
		
	#==================================================================
	#
	#==================================================================
	
	def find_basename_generic_kgr35s(self):
		self.find_basename_generic("8","S")
		
	#==================================================================
	#
	#==================================================================		
	def find_basename_generic(self,p_n,p_s):
		self.trace_header("04400")		
		self.find_genstring_genpath("0440")		
		self.trace_header("04200")		
		self.find_genstring_genpath("0420")		
		self.trace_header("04500")		
		self.find_genstring_genpath("04500")		
		self.trace_header("GDN_KGR35"+ p_s)		
		self.find_genstring_genpath("GDN_KGR35"+p_s)
		self.trace_header("161" + p_n)		
		self.find_genstring_genpath("161" + p_n)
		self.trace_header("171" + p_n)		
		self.find_genstring_genpath("171" + p_n)
		self.trace_header("181" + p_n)		
		self.find_genstring_genpath("181" + p_n)
		self.trace_header("191" + p_n)		
		self.find_genstring_genpath("191" + p_n)
	#==================================================================
	#
	#==================================================================
		
	def find_basename(self):
		self.trace_header("04400")		
		self.find_genstring_genpath("0440")		
		self.trace_header("04200")		
		self.find_genstring_genpath("0420")		
		self.trace_header("04500")		
		self.find_genstring_genpath("0450")		
		self.trace_header("GDN_KGR35")		
		self.find_genstring_genpath("GDN_KGR35")
		self.trace_header("1617")		
		self.find_genstring_genpath("1617")
		self.trace_header("1717")		
		self.find_genstring_genpath("1717")
		self.trace_header("1817")		
		self.find_genstring_genpath("1817")
		self.trace_header("1917")		
		self.find_genstring_genpath("1917")

	#==================================================================
	#
	#==================================================================
		
	def test_log(self):
		self.exetute_logging("test log")		
		
	#==================================================================
	#
	#==================================================================
		
cc = JTFind()
cc.setup_logging()
cc.create_stamp()
dds = JT_Services()
dds.define_services()
dds.add_logger(cc)
#cc.set_replace()
cc.unset_replace()
#cc.set_ext_sh_only()
cc.set_ext_all_files()
#cc.find_basename()
#cc.replace_to_kgr35s_1()
#cc.replace_generic_to_kgr35s()
#cc.test_log()
#cc.replace_to_kgr35s_repair_last()
#cc.replace_generic_to_kgr35s_from_kgr35b()
#cc.find_basename_generic_kgr35b()
#cc.find_basename_generic_kgr35s()
dds.print_services()
#================= NOTES ========================
#replacet_text_in_file:
#/***********************
#
#python  /rksup/config/kgr35jut/jut/python/find.py		
#/rksup/config/kgr35s/jut/python/install_db.sh
#/rksup/config/kgr35s/jut/python/idb2.sh
#/rksup/config/kgr35s/install/Install.sh

#cd /rksup/config/kgr35s/install/
#python find.py	>> ./log/t.log 2>&1
#env | grep SYBASE
#env | grep KRED
#ls -l	> t.log 2>&1
# vi test_1715.py
#python find.py	>& ./log/t.log
#JTFind().go_throug_all_not_ok()
#JTFind().go_throug_all_ok()
#JTFind().go_throug_all_ok_db()
#JTFind().go_throug_all_ok_18152()
#JTFind().find_17150string_genpath()
#echo test 2>&1
#define STDIN_FILENO    0   
#/* Standard input.  */ 
#define STDOUT_FILENO   1   
#/* Standard output.  
#*/ #define STDERR_FILENO   2
#vi ./log/ports.log
#cp /rksup/config/kgr35s/.root.passwords /rksup/config/kgr35s/.root.passwords
#vi /rksup/config/kgr35s/jut/python/logger_log.txt
#/***********************cd 

#cc.test_replace_all()
#cc.find_17150string_genpath();
#cc.replace_ports_for_db_17150_to_17100()
#cc.find_17100string_genpath();
#cc.find_genstring_genpath("18152")
#cc.replace_to_kgo()
#cc.find_kgr35s()
#cc.find_kgr35s()
#cc.find_kgr35s_properties()
#cc.setenv_db_kgr35s()
#cc.find_GDN_kgr35s()
#cc.find_kns()
#cc.startKNS()
#cc.tailKNS()
#cc.find_4205()
#cc.find_1915()
#cc.replace_1910_to_1915()
#cc.find_1X10X()
#cc.find_123_110()
#cc.replace_123_110_to_123_115_in_config()
#cc.find_04200()
#cc.find_04500()
#cc.replace_04200_04500()
#cc.find_kgrLogger()
#cc.replace_to_kgr35s()
#cc.find_to_kgr35s()
#cc.find_42073()
#cc.replace_to_kgr35s_1()
#cc.replace_42073_to_18159()
#cc.find_is_kgr35s()
#cc.find_1815()
#cc.replace_to_kgr35s_2()
#cc.replace_to_kgr35s_repair_last()
#cc.find_basename()
# vi /rksup/config/kgr35s/finder_log.txt
# rm /rksup/config/kgr35s/finder_log.txt
