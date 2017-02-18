import sys
import os

from .. appcore.exceptions.DBG_MainBase import *
import ConfigParser
class DBG_Config(DBG_MainBase):
        def __init__(self):
                DBG_MainBase.__init__(self)
                self.m_root_dir = "C:/lkd/komodo/apps/srt_accelerated/"
                self.m_prefix = "iastora2.conf"
                self.m_file = "C:/lkd/komodo/apps/srt_accelerated/iastora2.txt"
                
        def prepare_object(self,s_file_name,s_ver):
                try:
                        self.xx_dbg("DBG_Config::print_object::in::")
                        self.xx_dbg("DBG_Config::print_object::out::")
                except:
                        self.xx_exception("DBG_DbgEntry::prepare_object::excp")
                        
        def get_file(self):
                return self.m_file
                
        def create_config(self):
                try:
                        self.xx_dbg("DBG_Config::print_object::in::")
                        config = ConfigParser.RawConfigParser()
                        config.add_section('Section1')
                        config.set('Section1', 'an_int', '15')
                        config.set('Section1', 'a_bool', 'true')
                        config.set('Section1', 'a_float', '3.1415')
                        config.set('Section1', 'baz', 'fun')
                        config.set('Section1', 'bar', 'Python')
                        #config.set('Section1', 'foo', '%(bar)s is %(baz)s!')
                        sf = self.get_file()
                        print sf
                        with open(sf, 'wb') as configfile:
                                config.write(configfile)
                        print " saved"
                        self.xx_dbg("DBG_Config::print_object::out::")
                except:
                        self.xx_exception("DBG_DbgEntry::prepare_object::excp")
                        
        def read_config(self):
              try:
                        self.xx_dbg("DBG_Config::print_object::in::")
                        config = ConfigParser.RawConfigParser()
                        config.read('example.cfg')                        
                        a_float = config.getfloat('Section1', 'a_float')
                        an_int = config.getint('Section1', 'an_int')
                        print a_float + an_int
                        self.xx_dbg("DBG_Config::print_object::out::")
              except:
                        self.xx_exception("DBG_DbgEntry::prepare_object::excp")
