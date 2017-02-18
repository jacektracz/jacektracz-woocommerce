import sys
import traceback
import logging


class DBG_ExceptionPrinter:
        
    def __init__(self):
        self.m_log_file = None
        
    @staticmethod    
    def print_exception( tt ):
        """print_exception_and_quit"""        

        try:
            logging.exception("")
            print 'print_exc():'
            traceback.print_exc(file=sys.stdout)
            print
            print 'print_exc(1):'
            traceback.print_exc(limit=1, file=sys.stdout)
        except:            
            print "DBG_ExceptionPrinter::exception::"

    @staticmethod    
    def xx_dbg( tt ):
        """print_exception_and_quit"""        
        sdbg = 0
        if(sdbg == 1):
            print tt