#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by Jacek Tracz
#    
#==================================================================

import re


from JT_Logger import JT_Logger



class JT_Strings_find_options:        
    mg_option_rx = []

#==================================================================
#
#==================================================================
    
    def init_reg_ex_option(self):
        self.mg_option_rx.append(0)

#==================================================================
#
#==================================================================

    def get_reg_ex_option(self):
        self.init_reg_ex_option()
        return self.mg_option_rx[0]

#==================================================================
#
#==================================================================
    
    def set_reg_ex_option(self):
        self.init_reg_ex_option()
        self.mg_option_rx[0] = 1

#==================================================================
#
#==================================================================
    
    def uset_reg_ex_option(self):
        self.init_reg_ex_option()
        self.mg_option_rx[0] = 1
        
#==================================================================
#
#==================================================================
                    
class JT_Strings:

    @staticmethod    
    def find_word_rx(w,line):    
        r_word =  "\b" + w + "\b"
        d_out= re.compile(r_word, flags=re.IGNORECASE).search (line)        
        if d_out:
            return 1        
        return -1
            
#==================================================================
#
#==================================================================
    
    @staticmethod        
    def find_word(line,w):     
        return JT_Strings.find_word_basic(line,w)
    
        #if (JT_Strings_find_options().mg_option_rx[0] == 0 ):
        #    return JT_Strings.find_word_basic(line,w)
        #else:
        #    return JT_Strings.find_word_rx(line,w)
        
#==================================================================
#
#==================================================================
        
    @staticmethod        
    def find_word_basic(line,w):     
        JT_Logger.trace_method("find_word_basic" + "[" + w + "]" )
        JT_Logger. log_ps_line("[" + line + "]")
        return line.find(w)
        
#==================================================================
#
#==================================================================
