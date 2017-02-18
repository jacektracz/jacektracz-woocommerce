import string
import sys
from JT_Logger import JT_Logger
from JT_LogWritingAnaliser import JT_LogWritingAnaliser
from JT_FIND_Replacements import JT_FIND_Replacements
from JT_FIND_Replacement import JT_FIND_Replacement
from JT_FIND_Replacements import JT_FIND_WordsList
from JT_FIND_Replacements import JT_FIND_Words

#==================================================================
#
#==================================================================

class JT_FIND_Borders:
    def __init__(self):
        self.m_set_up = False
        self.m_border_start = ""
        self.m_border_end = ""
        self.m_started = False
        self.m_print_all = False        
#==================================================================
#
#==================================================================

    def set_state(self,p_line):
        if(self.m_set_up):            
            if( JT_FIND_WordsInFile.is_word_in_line(p_line, self.m_border_start)):
                print 'started'
                print p_line
                self.m_started = True
            if( JT_FIND_WordsInFile.is_word_in_line(p_line, self.m_border_end)):
                self.m_started = False
        return self.m_started
#==================================================================
#
#==================================================================
        
class JT_FIND_WordsInFile:

#==================================================================
#
#==================================================================

    @staticmethod
    def is_word_in_line(p_line, p_seeking_text):
        """is_word_in_line"""
        JT_Logger.trace_method("[METHOD_IN][is_word_in_line:enter]")
        is_in_line = False
        #p_dd = JT_FIND_Words()        
        pos = string.find(p_line, p_seeking_text)            
        if  pos >= 0:
            is_in_line = 1
                                                   
        JT_Logger.trace_method("[METHOD_IN][is_word_in_line:out]")
        
        return is_in_line
    
#==================================================================
#JT_FIND_WordsList
#==================================================================

    @staticmethod
    def is_all_word_in_line(p_line, p_dd):
        """print_whole_file_with_words"""
        JT_Logger.trace_method("[METHOD_IN][is_all_word_in_line:enter]")
        all_finded = 1
        #p_dd = JT_FIND_Words()        
        for ii_word in p_dd.m_words:            
            dd_word = JT_FIND_Replacement()
            dd_word = ii_word
            seeking_text = dd_word.m_word_new
            pos = string.find(p_line, seeking_text)            
            if  pos < 0:
                all_finded = 0
                break;                                   
            
        JT_Logger.trace_method("[METHOD_IN][is_all_word_in_line:out]")
        
        return all_finded
    
#==================================================================
#JT_FIND_WordsList
#==================================================================
    
    @staticmethod
    def print_whole_file_with_words_ex(p_filename,p_dd,p_borders):
        """print_whole_file_with_words_ex"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_whole_file_with_words_ex]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            dd_words_list = JT_FIND_WordsList()
            dd_words_list = p_dd
            lines = JT_LogWritingAnaliser.get_lines_for_opened_file( p_filename )
            
            ll_borders = JT_FIND_Borders()
            ll_borders = p_borders
            for ii_line in lines:                    
                        
                ll_borders.set_state(ii_line)
                                
                if(ll_borders.m_started == True):
                    
                    if(len(dd_words_list.m_words_lists) == 0):
                        JT_Logger.print_output_raw(ii_line)
                    else:                    
                        for ii_words in dd_words_list.m_words_lists:
                            dd_words = JT_FIND_Words()
                            dd_words = ii_words                            
                            pos = JT_FIND_WordsInFile.is_all_word_in_line(ii_line
                                                                          , dd_words)
                            if  pos == 1:                                        
                                JT_Logger.print_output_raw(ii_line)
                
            JT_Logger.trace_method("[METHOD_OUT][print_whole_file_with_words_ex]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_whole_file_with_words_ex]")

#==================================================================
#
#==================================================================
    
    @staticmethod
    def print_whole_file_with_words(p_filename,p_replacement):
        """print_whole_file_with_words"""

        
        try:
            JT_Logger.trace_method("[METHOD_IN][print_whole_file_with_words]")
            JT_Logger.trace_method("[p_filename:" + p_filename + "]")
        
            JT_Logger.print_output("\n/*====================================================/")
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*FILE:" + p_filename)
            JT_Logger.print_output("/*")
            JT_Logger.print_output("/*====================================================/")
            
            dd_repl = JT_FIND_Replacements()
            dd_repl = p_replacement
            lines = JT_LogWritingAnaliser.get_lines_for_opened_file(p_filename)
            
            for ii_line in lines:
                for ii_word in dd_repl.m_repl_words:
                    dd_word = JT_FIND_Replacement()
                    dd_word = ii_word
                    seeking_text = dd_word.m_word_old
                    pos = string.find(ii_line, seeking_text)            
                    if  pos >= 0:                                        
                        JT_Logger.print_output_raw(ii_line)
                
            JT_Logger.trace_method("[METHOD_OUT][print_whole_file_with_words]")
            
        except :
            JT_Logger.print_exception("\nException")
            JT_Logger.trace_method("[METHOD_OUT_EXC][print_whole_file_with_words]")

#==================================================================
#
#==================================================================

class JT_FIND_WordsInFile_Exec:
    
    def exec_main(self):
        cc = JT_FIND_WordsInFile()
        ll = sys.argv[1]        
        #cc.replace_one_setting_in_kgr("kgr36c","17190","17200",0,0)
        l_file = "/rksup/log/kgr36f/els/jtels_log_" + ll + "_.log";
        dd_repl = JT_FIND_Replacements()
        dd_repl.add_repl_sentences("REGISTERING_ON_SUBJECT:[_IN", "")
        dd_repl.add_repl_sentences("UNREGISTER_LISTENER::SUBJECT:_IN", "")
        dd_repl.add_repl_sentences("ACTIVATING_ON_SUBJECT:[_IN", "")        
        cc.print_whole_file_with_words(l_file, dd_repl)

#==================================================================
#
#==================================================================

    def exec_main_ex_del_list(self):
        cc = JT_FIND_WordsInFile()
        ll = sys.argv[1]                
        #l_file = "/rksup/log/kgr36f/els/jtels_log_" + ll + "_.log";
        l_file = ll
        dd_words_list = JT_FIND_WordsList()
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("~KNET_RealTimeLimitListener:enter:DELETING_LISTENER_RT")
        dd_words_list.add_words( dd_words )
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("KNEL_Event::~KNEL_Event")
        dd_words_list.add_words( dd_words )
        
        dd_borders = JT_FIND_Borders()
        dd_borders.m_set_up = False
        dd_borders.m_started = True
        cc.print_whole_file_with_words_ex(l_file, dd_words_list,dd_borders)
#==================================================================
#
#==================================================================
    
    def exec_main_ex_all_beetwen(self):
        cc = JT_FIND_WordsInFile()
        ll = sys.argv[1]                
        #l_file = "/rksup/log/kgr36f/els/jtels_log_" + ll + "_.log";
        l_file = ll
        dd_words_list = JT_FIND_WordsList()
                
        dd_borders = self.get_borders_insert_deal()
        
        cc.print_whole_file_with_words_ex(l_file, dd_words_list,dd_borders)
            
#==================================================================
#
#==================================================================
    def get_borders_empty(self):
        dd_borders = JT_FIND_Borders()
        dd_borders.m_set_up = False
        dd_borders.m_started = True
        return dd_borders
#==================================================================
#
#==================================================================

    def get_borders_insert_deal(self):
        dd_borders = JT_FIND_Borders()
        dd_borders.m_set_up = True
        dd_borders.m_started = False
        dd_borders.m_border_start = "INSERT_DEAL_START"
        dd_borders.m_border_end = "INSERT_DEAL_END"
        return dd_borders
#==================================================================
#
#==================================================================

        
    def exec_main_ex(self):
        cc = JT_FIND_WordsInFile()
        ll = sys.argv[1]        
        
        #l_file = "/rksup/log/kgr36f/els/jtels_log_" + ll + "_.log";
        
        l_file = ll
        
        dd_words_list = JT_FIND_WordsList()
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("KNET_ComputeResponseHandler")        
        dd_words_list.add_words(dd_words)
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("REGISTERING_ON_SUBJECT")
        dd_words.add_word_s("_IN")
        dd_words_list.add_words(dd_words)

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("UNREGISTER_LISTENER::SUBJECT:_IN")                    
        dd_words_list.add_words(dd_words)
                                
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("ACTIVATING_ON_SUBJECT:[_IN")                    
        dd_words_list.add_words(dd_words)
        
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("CREATING_LISTENER_RT:")
        dd_words.add_word_s("_IN")                    
        dd_words_list.add_words(dd_words)

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("DELETING_LISTENER_RT")
        dd_words.add_word_s("_IN")                    
        dd_words_list.add_words(dd_words)
        

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("~KNET_RealTimeLimitListener:enter:DELETING_LISTENER_RT")
        dd_words_list.add_words(dd_words)                
        

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("getResponseCb:enter:RESP_KEY")
        dd_words_list.add_words(dd_words)

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("removeResponseCb:UNREGISTER_HANDLER")
        dd_words_list.add_words(dd_words)
                
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("removeResponseCb")
        dd_words_list.add_words(dd_words)
        
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("KGLT_BaseServicesImpl::addServiceCb")
        dd_words_list.add_words(dd_words)

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("KGLT_BaseServicesImpl::removeResponseCb")
        dd_words_list.add_words(dd_words)

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("KGLT_BaseServicesImpl::removeResponseCb:UNREGISTER_HANDLER:CALL_ENTER:")
        dd_words_list.add_words(dd_words)
        
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("KGLT_SERV_LIMIT_DRILLDOWN")
        dd_words_list.add_words(dd_words)

        dd_words = JT_FIND_Words()
        dd_words.add_word_s("KGLT_ComputeResponseCxt")
        dd_words_list.add_words(dd_words)
        
        dd_words = JT_FIND_Words()
        dd_words.add_word_s("POSTBANK_C:KNEL_RmSessionImpl::eventCallback::CALLBACK_EVENT:")
        dd_words_list.add_words(dd_words)
        
        dd_borders = self.get_borders_insert_deal()
        
        cc.print_whole_file_with_words_ex(l_file
                                          , dd_words_list
                                          , dd_borders)
        
#==================================================================
#
#==================================================================

    def exec_main_dispatcher(self):
        JT_Logger.print_output_raw("exec_main_dispatcher:enter")
        ll = sys.argv[2]
        if ll == "1":
            JT_Logger.print_output_raw("exec_main_dispatcher:1")
            self.exec_main_ex()
                        
        if ll == "2":
            JT_Logger.print_output_raw("exec_main_dispatcher:2")
            self.exec_main_ex_del_list()
        
        if ll == "3":
            JT_Logger.print_output_raw("exec_main_dispatcher:2")
            self.exec_main_ex_all_beetwen()
        JT_Logger.print_output_raw("exec_main_dispatcher:out")
        
        
#==================================================================
#
#==================================================================

if __name__ == '__main__':
    #JT_FIND_WordsInFile_Exec().exec_main()
    #JT_FIND_WordsInFile_Exec().exec_main_ex()
    JT_FIND_WordsInFile_Exec().exec_main_dispatcher()
    
