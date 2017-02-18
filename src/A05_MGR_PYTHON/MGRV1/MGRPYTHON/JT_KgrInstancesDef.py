#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

from JT_Strings import JT_Strings
from JT_KgrInstanceDef import JT_KgrInstanceDef
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
        self.init_kgr_instances_gdy()
        self.init_kgr_instances_ptx()
        
#==================================================================
#
#==================================================================

    def init_kgr_instances_kgr35s(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr35s")
        self.add_kgr_instance("GDN_KGR35S")
        
#==================================================================
#
#==================================================================
        
    def init_kgr_instances_kgr35(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr35")
        #self.add_kgr_instance("GDN_KGR35")

#==================================================================
#
#==================================================================
        
    def init_kgr_instances_kgr35b(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr35b")
        self.add_kgr_instance("GDN_KGR35B")
        self.add_kgr_instance("gs17")
        self.add_kgr_instance("gs17")

#==================================================================
#
#==================================================================
        
    def init_kgr_instances_kgr32a(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr32a")
        self.add_kgr_instance("GDN_KGR32A")
        self.add_kgr_instance("gs04")
        #self.add_kgr_instance("gs17")
        
    def init_kgr_instances_kgr32b(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr32b")
        self.add_kgr_instance("GDN_KGR32B")
        self.add_kgr_instance("gs04")

#==================================================================
#
#==================================================================
        
    def init_kgr_instances_kgr32c(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr32c")
        self.add_kgr_instance("GDN_KGR32C")        
        #self.add_kgr_instance("gs17")
        self.add_kgr_instance("gs04")
        #self.add_kgr_instance("gs05")
        #self.add_kgr_instance("gs12")
        #self.add_kgr_instance("gs16")
        #self.add_kgr_instance("gs17")
        
#==================================================================
#
#==================================================================

    def add_kgr_instance_by_key(self,p_key):
        #self.add_kgr_instance("kgr32")
        if (p_key =="kgr35"):
            self.init_kgr_instances_kgr35()
            
        if (p_key =="kgr32"):
            self.add_kgr_instance("kgr32")
            
        if (p_key =="kgr32a"):
            self.add_kgr_instance("kgr32a")
            
        if (p_key =="kgr32b"):
            self.add_kgr_instance("kgr32b")
            
        if (p_key =="kgr32c"):
            self.add_kgr_instance("kgr32c")
            
        if (p_key =="kgr35s"):
            self.add_kgr_instance("kgr35s")
            
        if (p_key =="kgr35b"):
            self.add_kgr_instance("kgr35b")
            
        if (p_key =="kgr36JT"):
            self.add_kgr_instance("kgr36JT")

        if (p_key =="kgr36c"):
            self.add_kgr_instance("kgr36c")

        if (p_key =="kgr36"):
            self.add_kgr_instance("kgr36")
            
        if (p_key =="GDN_KGR35B"):
            self.add_kgr_instance("GDN_KGR35B")
            
        if (p_key =="GDN_KGR35S"):
            self.add_kgr_instance("GDN_KGR35S")
            
        if (p_key =="GDN_KGR36JT"):
            self.add_kgr_instance("GDN_KGR36JT")
            
        if (p_key =="GDN_KGR36"):
            self.add_kgr_instance("GDN_KGR36")
            
        if (p_key =="GDN_KGR32"):
            self.add_kgr_instance("GDN_KGR32")
            
        if (p_key =="GDN_KGR32A"):
            self.add_kgr_instance("GDN_KGR32A")
            
        if (p_key =="GDN_KGR32B"):
            self.add_kgr_instance("GDN_KGR32B")
            
        if (p_key =="GDN_KGR32C"):
            self.add_kgr_instance("GDN_KGR32C")
            
        if (p_key ==""):
            self.add_kgr_instance("gs04")
            
        if (p_key =="gs05"):
            self.add_kgr_instance("gs05")
            
        if (p_key =="gs12"):
            
            self.add_kgr_instance("gs12")
            
        if (p_key =="gs16"):
            self.add_kgr_instance("gs16")
            
        if (p_key =="gs17"):
            self.add_kgr_instance("gs17")
            #ptx
        if (p_key =="kgr35WebLogic"):
            self.add_kgr_instance("kgr35WebLogic")
            
        if (p_key =="kgr35RB"):
            self.add_kgr_instance("kgr35RB")
            
        if (p_key =="kgr35"):
            self.add_kgr_instance("kgr35")
            
        if (p_key =="kgrSet"):
            self.add_kgr_instance("kgrSet")
            
        if (p_key =="fatih"):
            self.add_kgr_instance("fatih")
            
        if (p_key =="loki"):
            self.add_kgr_instance("loki")
            
        if (p_key =="pegase"):
            self.add_kgr_instance("pegase")
            
        if (p_key =="persee"):
            self.add_kgr_instance("persee")
            
        if (p_key =="riyad"):
            self.add_kgr_instance("riyad")
            
        if (p_key =="tcv"):
            self.add_kgr_instance("tcv")
            
        if (p_key =="thor"):
            self.add_kgr_instance("thor")
            
        if (p_key =="thrall"):
            self.add_kgr_instance("thrall")
            
        if (p_key =="manucfg32"):
            self.add_kgr_instance("manucfg32")
            
        if (p_key =="jupiter"):
            self.add_kgr_instance("jupiter")
            
        if (p_key =="k33"):
            self.add_kgr_instance("k33")
            
        if (p_key =="ds36"):
            self.add_kgr_instance("ds36")
            
        if (p_key ==""):
            self.add_kgr_instance("ds50")
            
        if (p_key =="ds53"):
            self.add_kgr_instance("ds53")
            
        if (p_key =="K33"):
            self.add_kgr_instance("K33")
            
        if (p_key =="LVSUP04"):
            self.add_kgr_instance("LVSUP04")
            
        if (p_key =="DS_FATIH"):
            self.add_kgr_instance("DS_FATIH")
        
#==================================================================
#
#==================================================================
    
    def init_kgr_instances_gdy(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr35")
        self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr32a")
        self.add_kgr_instance("kgr32b")
        self.add_kgr_instance("kgr32c")
        self.add_kgr_instance("kgr35s")
        self.add_kgr_instance("kgr35b")
        self.add_kgr_instance("kgr36")
        self.add_kgr_instance("kgr36c")
        self.add_kgr_instance("kgr36e")
        self.add_kgr_instance("kgr36f")
        self.add_kgr_instance("kgr36g")
        self.add_kgr_instance("kgr36JT")
        self.add_kgr_instance("GDN_KGR35B")
        self.add_kgr_instance("GDN_KGR35S")
        self.add_kgr_instance("GDN_KGR36JT")
        self.add_kgr_instance("GDN_KGR32")
        self.add_kgr_instance("GDN_KGR32A")
        self.add_kgr_instance("GDN_KGR32B")
        self.add_kgr_instance("GDN_KGR32C")
        self.add_kgr_instance("gs04")
        self.add_kgr_instance("gs05")
        self.add_kgr_instance("gs12")
        self.add_kgr_instance("gs16")
        self.add_kgr_instance("gs14")
        self.add_kgr_instance("gs17")
        #self.add_kgr_instance("GDN_KGR35")
        #self.add_kgr_instance("java")
        #self.add_kgr_instance("all_env")
        
#==================================================================
#
#==================================================================
        
    def init_kgr_instances_gdy_36(self):
        #self.add_kgr_instance("kgr32")
        self.add_kgr_instance("kgr36")
        self.add_kgr_instance("kgr36c")
        self.add_kgr_instance("kgr36e")
        self.add_kgr_instance("kgr36f")
        self.add_kgr_instance("kgr36g")
        self.add_kgr_instance("gs14")        
        self.add_kgr_instance("GDN_KGR36C")
        self.add_kgr_instance("GDN_KGR36E")
#==================================================================
#
#==================================================================
    
    def init_kgr_instances_test(self):
        #self.add_kgr_instance("kgrSet")
        self.add_kgr_instance("kgr32c")
#==================================================================
#
#==================================================================
        
    def init_kgr_instances_kgrSet(self):
        self.add_kgr_instance("kgrSet")

#==================================================================
#
#==================================================================

    def init_kgr_instances_fatih(self):
        self.add_kgr_instance("fatih")
        self.add_kgr_instance("k33")
        self.add_kgr_instance("ds36")
        self.add_kgr_instance("ds50")
        self.add_kgr_instance("ds53")
        
#==================================================================
#
#==================================================================
        
    def init_kgr_instances_ptx(self):
        self.add_kgr_instance("kgr35WebLogic")
        self.add_kgr_instance("kgr35RB")
        self.add_kgr_instance("kgr35")
        self.add_kgr_instance("kgrSet")
        self.add_kgr_instance("fatih")
        self.add_kgr_instance("loki")
        self.add_kgr_instance("pegase")
        self.add_kgr_instance("persee")
        self.add_kgr_instance("rembrandt")
        self.add_kgr_instance("riyad")
        self.add_kgr_instance("tcv")
        self.add_kgr_instance("thor")
        self.add_kgr_instance("thrall")
        self.add_kgr_instance("manucfg32")
        self.add_kgr_instance("jupiter")
        self.add_kgr_instance("k33")
        self.add_kgr_instance("ds36")
        self.add_kgr_instance("ds50")
        self.add_kgr_instance("ds53")
        self.add_kgr_instance("K33")
        self.add_kgr_instance("LVSUP04")
        self.add_kgr_instance("DS_FATIH")
        #self.add_kgr_instance("java")
        
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

    def check_(self, p_line,pargs):
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
#
#==================================================================
