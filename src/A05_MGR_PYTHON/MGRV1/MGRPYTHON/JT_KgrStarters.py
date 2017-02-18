#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

import pexpect 

class JT_KgrStarters:
    
    def __init__(self):
        self.m_kgr_env = ""

#==================================================================
#
#==================================================================

    def start_rksup_config(self,p_kgr,p_srv):
        """start_srv_rk"""          
        ll = "/rksup/config/"  + p_srv + " " + p_kgr  + " &"              
        pexpect.run(ll)

#==================================================================
#
#==================================================================

    def start_rksup_config_kgr(self,p_kgr,p_srv):
        """start_srv_rk"""          
        ll = "/rksup/config/" + p_kgr + "/" + p_srv  + " &"            
        pexpect.run(ll)

#==================================================================
#
#==================================================================

    def su_user(self,p_user):
        """set_kglenv"""                        
        ll = "su " + p_user             
        pexpect.run(ll)

#==================================================================
#
#==================================================================

    def set_kglenv(self,p_kgr):
        """set_kglenv"""                        
        ll = "kglenv " + p_kgr             
        pexpect.run(ll)
                
#==================================================================
#
#==================================================================


    def start_kgrs(self
                   ,p_kgr
                   ,p_user_kgr
                   ,p_user_kp
                   ,p_user_db):
        """start_kgrs"""
                                
        self.su_user(p_user_kgr)
        self.set_kglenv(p_kgr)
        self.start_rksup_config_kgr(p_kgr,"starttibems.sh")

        #self.su_user(p_user_kgr)
        #self.set_kglenv(p_kgr)
        self.start_rksup_config_kgr(p_kgr,"starttibems.sh")

        self.start_rksup_config_kgr(p_kgr,"startKGRWebApp_jboss.sh")

        self.su_user(p_user_kgr)
        self.set_kglenv(p_kgr)
        self.start_rksup_config(p_kgr,"startKNS")

        #self.su_user(p_user_kp)
        #self.set_kglenv(p_kgr)
        #self.start_rksup_config(p_kgr,"startkglagent.sh")

#==================================================================
#
#==================================================================


    def start_main_kgr35s(self):
        """start_main_kgr35s"""
        self.start_kgrs("kgr35s","rksup35","ksup30","rms_syb")
        
#==================================================================
#
#==================================================================
