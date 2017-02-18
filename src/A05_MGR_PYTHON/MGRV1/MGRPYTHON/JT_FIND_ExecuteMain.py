#from JT_Logger import JT_Logger
from JT_FIND_KgrEnvironmentFinder import JT_FIND_KgrEnvironmentFinder

    #==================================================================
    #
    #==================================================================

class JT_FIND_ExecuteMain:
    def exec_main(self):
        cc = JT_FIND_KgrEnvironmentFinder()
        #cc.create_stamp()
        #cc.replace_generic_to_kgr35a_from_kgr35a_maskxx()
        #cc.replace_generic_to_kgr35b_from_kgr35b_mask_xx_3xx()
        #cc.replace_generic_to_kgr36JT_from_kgr35b_mask_xx_3xx()
        #cc.install_kgr_36JT("PPP","UUU")    
        #cc.create_install_jboss_files()
        cc.build_jboss_default_36JT()        

    #==================================================================
    #
    #==================================================================
