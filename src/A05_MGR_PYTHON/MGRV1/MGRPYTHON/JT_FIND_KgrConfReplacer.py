
from JT_FIND_KgrEnvironmentFinder import JT_FIND_KgrEnvironmentFinder

class JT_FIND_KgrConfReplacer_Exec:
    def exec_main(self):
        cc = JT_FIND_KgrEnvironmentFinder()
        cc.create_stamp()
        #cc.replace_one_setting_in_kgr("kgr36c","17190","17200",0,0)
        cc.replace_one_setting_in_kgr("kgr36c","GDN_KGR36JC","GDN_KGR36C",0,1)
        
    #==================================================================
    #
    #==================================================================

if __name__ == '__main__':
    JT_FIND_KgrConfReplacer_Exec().exec_main()
