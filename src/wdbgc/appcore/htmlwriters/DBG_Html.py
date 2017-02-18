import sys
import os

from ... appcore.filewriters.DBG_FileWriter import *
from ... appcore.logging.DBG_ExceptionPrinter import *
from ... appcore.config.DBG_PrintConfig import *

from cgi import escape

class DBG_Html:
	
	@staticmethod
	def m_sel_ol():
		return 1
	
	@staticmethod
	def m_sel_ul():
		return 0
	
	@staticmethod    
	def xx_print_start():
		try:
			ss ="""<!DOCTYPE html>
<html>
<head>
    <title></title>
    <meta charset="utf-8" />
	<link rel="stylesheet" type="text/css" href="assets/styles/_styles.css" media="screen">
	<link rel="stylesheet" type="text/css" href="./assets/styles/_styles.css" media="screen">
	<link rel="stylesheet" type="text/css" href="../assets/styles/_styles.css" media="screen">
	<link rel="stylesheet" type="text/css" href="../../assets/styles/_styles.css" media="screen">
	<link rel="stylesheet" type="text/css" href="../../../assets/styles/_styles.css" media="screen">
	<link rel="stylesheet" type="text/css" href="../../../../assets/styles/_styles.css" media="screen">
</head>
<body>
<ol class='tree'>
<li>	
    <a href ="../rst_menu.html">UP</a>
</li>	
</ol>
"""
			DBG_Html.xx_write_to_out(ss)
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_getsel::out::")

			
	@staticmethod	
	def xx_print_end():
		try:
			ss="""</body>
</html>"""
			DBG_Html.xx_write_to_out(ss)
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_getsel::out::")
		
		
	@staticmethod
	def xx_getsel(pclass="",pselclass="olt"):
		try:
			if(DBG_Html.m_sel_ol() == 1):
				DBG_Html.xx_write_to_out ("<ol class='" + pselclass + "'>")
				
			if(DBG_Html.m_sel_ul() == 1):
				DBG_Html.xx_write_to_out ("<ul>")
				
			DBG_Html.xx_write_to_out ("<!--" + pclass + "-->")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_getsel::out::")
		
	@staticmethod	
	def xx_getsele(pclass=""):
		try:
			if(DBG_Html.m_sel_ol() == 1):
				DBG_Html.xx_write_to_out ("</ol>")
				
			if(DBG_Html.m_sel_ul() == 1):
				DBG_Html.xx_write_to_out ("</ul>")
				
			DBG_Html.xx_write_to_out ("<!--" + pclass + "-->")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_getsel::out::")


	@staticmethod
	def xx_print_class_start(path,pclass=""):
		try:
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::in::")
			DBG_Html.xx_write_to_out ("<li>")
			
			DBG_Html.xx_write_to_out ("<div class='wdbg-class'><!--" + pclass + "-->")
		
				
			DBG_Html.xx_print_ol_label("mclass",path)
			
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::out::")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_print_class_start::out::")
		
	@staticmethod
	def xx_print_class_end( pclass=""):
		try:
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::in::")
			DBG_Html.xx_getsele (pclass)
			DBG_Html.xx_write_to_out ("</div><!--" + pclass + "-->")
			DBG_Html.xx_write_to_out ("</li>")
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::out::")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_print_class_end::out::")
		
	@staticmethod
	def xx_print_ol_label__( path=""):
		try:
			DBG_Html.xx_write_to_out ('<label for="subsubfolder1">')
			DBG_Html.xx_write_to_out ( path )
			DBG_Html.xx_write_to_out ("</label>")
			DBG_Html.xx_write_to_out ('<input type="checkbox" id="subsubfolder1" />') 
			DBG_Html.xx_getsel ("")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_print_ol_label__::out::")

	@staticmethod
	def xx_print_ol_label( pclass, path=""):
		try:
			DBG_Html.xx_write_to_out ('<label for="subsubfolder1" class="' + pclass +'">')
			DBG_Html.xx_write_to_out ( path )
			DBG_Html.xx_write_to_out ("</label>")
			DBG_Html.xx_write_to_out ('<input type="checkbox" id="subsubfolder1" />') 
			DBG_Html.xx_getsel ("")		
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_print_ol_label::out::")

		
	@staticmethod		
	def xx_dis( pclass=""):
		try:
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_dis::in::")
			DBG_Html.xx_write_to_out ("<div class='wdbg-el'><!--" + pclass + "-->")
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_dis::out::")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_dis::out::")

	@staticmethod
	def xx_die( pclass = "" ):
		try:
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::in::")
			DBG_Html.xx_write_to_out ("</div><!--" + pclass + "-->")
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::out::")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_die::out::")

	@staticmethod
	def xx_lis( pclass = "" ):
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::in::")
		DBG_Html.xx_write_to_out ("<li><!--" + pclass + "-->")
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::out::")
		
	@staticmethod
	def xx_lie( pclass = "" ):
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::in::")
		DBG_Html.xx_write_to_out ("</li><!--" + pclass + "-->")
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::out::")


	@staticmethod
	def xx_ols( pclass = "" ):
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::in::")
		DBG_Html.xx_getsel (pclass,"tree")
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::out::")
		
	@staticmethod
	def xx_ole( pclass = "" ):
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::in::")
		DBG_Html.xx_getsele (pclass)
		DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::out::")

	@staticmethod
	def xx_print_props_start(pclass=""):
		try:
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::in::")
			DBG_Html.xx_write_to_out ("<li>")
			
			DBG_Html.xx_write_to_out ("<div class='wdbg-class'><!--" + pclass + "-->")
			
			DBG_Html.xx_print_ol_label("props",pclass)
			
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::out::")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_die::out::")

	@staticmethod
	def xx_print_props_end( pclass=""):
		try:
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::in::")
			DBG_Html.xx_getsele ( pclass )
			DBG_Html.xx_write_to_out ("</div><!--" + pclass + "-->")
			DBG_Html.xx_write_to_out ("</li>")
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_print_end::out::")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_die::out::")

	@staticmethod
	def print_field_html_out( pss , pclass = ""):
		try:
			
			DBG_Html.print_field_out(pss, pclass)
			DBG_Html.print_field_html(pss, pclass)
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_die::out::")
			
	@staticmethod
	def print_field_out( pss , pclass = ""):
		try:
			if(DBG_PrintConfig().getItem().m_print_field_out == 1):
				print pss			
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_die::out::")


	@staticmethod
	def print_field_html( pss , pclass = ""):
		try:
				
			DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::in::")
			if(pss == ""):
				DBG_Html.xx_write_to_out ("<li><!--" + pclass + "-->")
				DBG_Html.xx_write_to_out ( '<br/>' )
				DBG_Html.xx_write_to_out ("</li><!--" + pclass + "-->")
			else:			
				DBG_Html.xx_write_to_out ("<li><!--" + pclass + "-->")
				DBG_Html.xx_write_to_out ( escape(pss.strip()) )
				DBG_Html.xx_write_to_out ("</li><!--" + pclass + "-->")
				DBG_Html.xx_dbg("DBG_MemoryPtr::xx_die::out::")
		except:
			DBG_ExceptionPrinter.xx_dbg("DBG_Html::xx_die::out::")
		
	@staticmethod
	def xx_dbg( pclass="" ):
		""" xx """
		
	@staticmethod
	def xx_write_to_out( ss = "" ):
		""" xx """
		DBG_FileWriter().write_to_log(ss)