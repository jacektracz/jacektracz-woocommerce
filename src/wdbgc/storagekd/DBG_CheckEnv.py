import sys
import logging
from .. appcore.memory.DBG_Utils import *
from .. DBG_MemoryPtr import *
              

class DBG_CheckEnv:

		def xx_chk_sym_iastora(self):
            
			DBG_Utils().xx_safe_exe("!chksym iastora")

		def xx_chk_load_iastora(self):
			DBG_Utils().xx_safe_exe("!chksym iastora")

		def xx_set_env(self):

			DBG_Utils().xx_safe_exe('.reload /f iastora','CHECK_SYM')
			DBG_Utils().xx_safe_exe(".load C:\rst\src_14.6.0.1029\3party\BuildLab\10146\Program Files\Windows Kits\10\Debuggers\x64\winext\storagekd.dll")

		def xx_chk_env(self):

			DBG_Utils().xx_safe_exe('!chksym iastora','CHECK_SYM')

			DBG_Utils().xx_safe_exe('vertarget','[INIT__2]')

			DBG_Utils().xx_safe_exe('!lmi storport','[INIT__2]')

			DBG_Utils().xx_safe_exe('!lmi iastora','[INIT__2]')

			DBG_Utils().xx_safe_exe('.reload storport.sys','[INIT__2]')

			DBG_Utils().xx_safe_exe('dd nt!kd_default_mask','[INIT__2]')

			DBG_Utils().xx_safe_exe('!lmi nt','[INIT__2]')

			DBG_Utils().xx_safe_exe('.reload ntoskrnl.exe','[INIT]')

			DBG_Utils().safe_exe('!poaction','[POWER_STATE]')

			DBG_Utils().safe_exe('x iastora!g_raidport','[CHECK_IASTORA]')
