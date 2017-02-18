#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

try:
    import os
    import pwd
except:
    print "error in import files"
       
class JT_OS_Getguid:
       
    @staticmethod
    def get_euser() :
        """get_euser"""
        try:
            dd_out =  pwd.getpwuid(os.getuid())[0]
        
            return dd_out
        except:
            print "EXCEPTION_IN_GETEUSER"
            return "exc_in_geteuser"