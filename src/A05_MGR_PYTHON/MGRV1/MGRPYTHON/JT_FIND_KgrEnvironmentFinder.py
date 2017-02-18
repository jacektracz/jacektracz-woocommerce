
#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by jacek Tracz
#    
#==================================================================

import sys

import string
import os

from JT_Os import JT_Os
from JT_Logger import JT_Logger
from JT_FIND_Headers import JT_FIND_Headers
from JT_FIND_FilesHelper import JT_FIND_FilesHelper
from JT_FIND_Replacement import JT_FIND_Replacement
from JT_FIND_Replacements import JT_FIND_Replacements
from JT_FIND_Files import JT_FIND_Files
from JT_FIND_Files import JT_FIND_File
from JT_LoggerSettings import JT_LoggerSettings
from JT_FIND_Timestamp import JT_FIND_Timestamp

#==================================================================
#
#==================================================================
        
class JT_FIND_KgrEnvironmentFinder:


#==================================================================
#
#==================================================================

    def __init__(self):
        self.m_stamp = ""
        self.m_execute_replace = 0            
        self.m_for = ["0","1","2","3","4","5","6","7","8","9"]
        self.m_paths = []                    
        self.m_exts = []                        
        self.m_replacements = JT_FIND_Replacements()
        self.m_find_files = JT_FIND_Files()
        self.m_execute_copy_files_default_to_robo = 0
        self.m_execute_copy_files_template_to_def = 0
        self.m_execute_copy_files_robo_to_config = 0
        self.m_debug_mode = ""
                
    #======================================================================================================
    #
    #======================================================================================================
    
    def unset_replace(self):
        self.m_execute_replace = 0
        
    #==================================================================
    #
    #==================================================================
        
    def set_replace(self):
        self.m_execute_replace = 1
        
    #==================================================================
    #
    #==================================================================        
    
    def set_ext_all_files(self):
        JT_Logger.trace_hard_level_16( "[METHOD_IN][set_ext_all_files]" )
        self.m_exts.append("*.xml")
        self.m_exts.append("*.cfm")
        self.m_exts.append("*.conf")
        self.m_exts.append("*.properties")
        self.m_exts.append("*.params")
        self.m_exts.append("*.sh")
        self.m_exts.append("*.ksh")
        JT_Logger.trace_hard_level_16( "[METHOD_OUT][set_ext_all_files]" )
        
    #==================================================================
    #
    #==================================================================
                    
    def add_rksup_config_path(self,p_path):
        JT_Logger.trace_hard_level_16( "[METHOD_IN][add_rksup_config_path]" )        
        self.m_paths.append("/rksup/config/" + p_path)
        JT_Logger.trace_hard_level_16( "[METHOD_OUT][add_rksup_config_path]" )        
    
    #==================================================================
    #
    #==================================================================
        
    def add_word_pair_to_replacement(self,p_old,p_new):
        self.m_replacements.add_repl_sentences(p_old, p_new)
                                                                          
    #==================================================================
    #
    #==================================================================

    def build_list_of_files_with_find(self):        
        """build_list_of_files_with_find"""
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][build_list_of_files_with_find]" )
        
        self.m_builded_files_list  = []
        for path in self.m_paths:
            JT_Logger.trace_hard_level_16( "[INFO.REPLACE_IN_PATHS]" 
                                           + "[" + path + "]")
            
            JT_FIND_Headers().print_finding_header_path("[FINDING_IN_PATH]" 
                                           + "[path:" + path + "]")
            for ext in self.m_exts:                
                cmd = 'find ' + path + ' -name "' + ext + '" -print'         
                JT_Logger.trace_hard_level_16( '[INFO]cmd:' + cmd )
                        
                for l_file in os.popen(cmd).readlines():             
                    s_full_file_path = l_file[:-1]                     
                    self.m_find_files.add_raw_file_to_list(s_full_file_path)
                    
        JT_Logger.trace_hard_level_16( "[METHOD_OUT][build_list_of_files_with_find]" )

    #==================================================================
    #
    #==================================================================

    def add_raw_file_to_list(self,p_file):
        """build_list_of_files"""
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                        + "[add_kgr_file_to_list]" 
                                        + "[p_file:"  + p_file + "]")
        
        self.m_builded_files_list.append(p_file)
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                        + "[build_list_of_files]" )


    #==================================================================
    #
    #==================================================================
        
    def create_stamp(self):
        JT_Logger.trace_hard_level_16 ( "[METHOD_IN]" 
                                        + "[create_stamp]")
        
        self.m_stamp = JT_FIND_Timestamp().create_stamp()        
        JT_Logger.trace_hard_level_16 ( "[create_stamp]" 
                                        + "[" + self.m_stamp + "]")                                    
        
    #==================================================================
    #
    #==================================================================

    def print_settings(self):
        """print_settings"""
        self.print_settings_files()
        self.print_settings_words()
        
    #==================================================================
    #
    #==================================================================
        
    def print_settings_files(self):
        """print_settings_files"""
        
        JT_Logger.print_output( "[METHOD_IN][EXECUTED_FILES]" )
        
        for ii_find_file in self.m_find_files.m_find_files:
            ii_find_file_typed =JT_FIND_File()
            ii_find_file_typed = ii_find_file
            JT_Logger.print_output( "")
            JT_Logger.print_output( "[FILE_TEMPLATE" + ii_find_file_typed.m_file_template + "]")            
            JT_Logger.print_output( "[FILE_DEF:" + ii_find_file_typed.m_file_def + "]")
            JT_Logger.print_output( "[FILE_ROBO:" + ii_find_file_typed.m_file_robo + "]")
            JT_Logger.print_output( "[FILE_CONFIG:" + ii_find_file_typed.m_file_config + "]")
            JT_Logger.print_output( "[FILE_INSTALL:" + ii_find_file_typed.m_file_install + "]")
            
        JT_Logger.print_output( "[METHOD_OUT][EXECUTED_FILES]" )
    #==================================================================
    #
    #==================================================================

    def print_settings_words(self):
        """print_settings_words"""
        JT_Logger.print_output( "[METHOD_IN]" 
                                + " [EXECUTED_WORDS]" )
                
        for ii_dd in self.m_replacements.m_repl_words:
            ii_dd_t = JT_FIND_Replacement()
            ii_dd_t = ii_dd
            JT_Logger.print_output( "[WORD_ORIGINAL:" + ii_dd_t.m_word_old + "]" 
                                    + "[WORD_NEW:" + ii_dd_t.m_word_new + "]")
            
        JT_Logger.print_output( "[METHOD_OUT]" 
                                        + " [EXECUTED_WORDS]" )
    #==================================================================
    #
    #==================================================================

    def execute_copy_files_robo_to_config(self):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                        + " [execute_copy_files_robo_to_config]" )
        
        for ii_find_file in self.m_find_files.m_find_files:
            ii_find_file_typed = JT_FIND_File()
            ii_find_file_typed = ii_find_file
            
            
            s_full_path_file_old = ii_find_file_typed.m_file_robo
            s_full_path_file_new = ii_find_file_typed.m_file_config
            
            if(self.m_execute_copy_files_robo_to_config == 1):
                
                JT_Logger.trace_hard_level_16( "[EXECUTE.COPY_FILE_ROBO_TO_CONFIG:") 
                JT_Logger.trace_hard_level_16( "[s_full_path_file_old:" + s_full_path_file_old + "]")
                JT_Logger.trace_hard_level_16( "[s_full_path_file_new:" + s_full_path_file_new + "]")
                                               
                JT_FIND_FilesHelper().copy_file(
                                                s_full_path_file_old
                                                , s_full_path_file_new)
            else:
                JT_Logger.print_output("")
                JT_Logger.print_output( "[TEST.COPY_FILE_ROBO_TO_CONFIG:]") 
                JT_Logger.print_output( "[s_full_path_file_old:" + s_full_path_file_old + "]")
                JT_Logger.print_output( "[s_full_path_file_new:" + s_full_path_file_new + "]")

        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                        + " [execute_copy_files_default_to_robo")
        
    #==================================================================
    #
    #==================================================================

    def execute_copy_files_default_to_robo(self):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                        + " [execute_copy_files_default_to_robo]" )
        
        for ii_find_file in self.m_find_files.m_find_files:
            ii_find_file_typed = JT_FIND_File()
            ii_find_file_typed = ii_find_file
            
            
            s_full_path_file_old = ii_find_file_typed.m_file_def
            s_full_path_file_new = ii_find_file_typed.m_file_robo
            if(self.m_execute_copy_files_default_to_robo == 1):
                
                JT_Logger.trace_hard_level_16( "[EXECUTE.COPY_FILE_DEFAULT_TO_ROBO:") 
                JT_Logger.trace_hard_level_16( "[s_full_path_file_old:" + s_full_path_file_old + "]")
                JT_Logger.trace_hard_level_16( "[s_full_path_file_new:" + s_full_path_file_new + "]")
                                               
                JT_FIND_FilesHelper().copy_file(
                                                s_full_path_file_old
                                                , s_full_path_file_new)
            else:
                JT_Logger.print_output("")
                JT_Logger.print_output( "[TEST.COPY_FILE_DEFAULT_TO_ROBO:]") 
                JT_Logger.print_output( "[s_full_path_file_old:" + s_full_path_file_old + "]")
                JT_Logger.print_output( "[s_full_path_file_new:" + s_full_path_file_new + "]")

        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                        + " [execute_copy_files_default_to_robo")
        

    #==================================================================
    #
    #==================================================================

    def execute_copy_files_template_to_default(self):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                        + " [execute_copy_files_template_to_default]" )
        
        for ii_find_file in self.m_find_files.m_find_files:
            ii_find_file_typed = JT_FIND_File()
            ii_find_file_typed = ii_find_file
            
            
            s_full_path_file_old = ii_find_file_typed.m_file_template
            s_full_path_file_new = ii_find_file_typed.m_file_def
            if(self.m_execute_copy_files_template_to_def == 1):
                
                JT_Logger.trace_hard_level_16( "[EXECUTE.COPY_FILE:") 
                JT_Logger.trace_hard_level_16( "[s_full_path_file_old:" + s_full_path_file_old + "]")
                JT_Logger.trace_hard_level_16( "[s_full_path_file_new:" + s_full_path_file_new + "]")                                               
                JT_FIND_FilesHelper().copy_file(
                                                s_full_path_file_old
                                                , s_full_path_file_new)
            else:
                JT_Logger.print_output("")
                JT_Logger.print_output( "[TEST.COPY_FILE_TEMPLATE_TO_DEF:]" )
                JT_Logger.print_output( "[s_full_path_file_old:" + s_full_path_file_old + "]")
                JT_Logger.print_output( "[s_full_path_file_new:" + s_full_path_file_new + "]")

        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                        + " [execute_copy_files_template_to_default")

        
    #==================================================================
    #
    #==================================================================
        
            
    def execute_replace_words_in_files_config(self):
        
        JT_Logger.print_output( "[METHOD_IN]" 
                                        + " [execute_replace_words_in_files_config]" )
        
        for ii_find_file in self.m_find_files.m_find_files:
            ii_find_file_typed =JT_FIND_File()
            ii_find_file_typed = ii_find_file
            s_file = ii_find_file_typed.m_file_config
            
            JT_Logger.print_output( "")
            JT_Logger.print_output( "[INFO][REPLACE_WORDS_IN_FILE]") 
            JT_Logger.print_output( "[FILE:" + s_file + "]")
            
            i_backup_already_created_for_file = 0
            i_backup_created_in_method = self.execute_replace_words_in_one_file(
                                                   s_file
                                                   ,i_backup_already_created_for_file)
            if( i_backup_created_in_method == 1):
                i_backup_already_created_for_file = 1
                    
        JT_Logger.print_output( "[METHOD_OUT]" 
                                        + " [execute_replace_words_in_files_config")


    #==================================================================
    #
    #==================================================================

    def execute_replace_words_in_founded_files(self):
        
        JT_Logger.print_output( "[METHOD_IN]" 
                                        + " [execute_replace_words_in_founded_files]" )
        
        for ii_find_file in self.m_find_files.m_find_files:
            ii_find_file_typed =JT_FIND_File()
            ii_find_file_typed = ii_find_file
            s_file = ii_find_file_typed.m_file_config
            
            JT_Logger.print_output( "")
            JT_Logger.print_output( "[INFO][REPLACE_WORDS_IN_FILE]") 
            JT_Logger.print_output( "[FILE:" + s_file + "]")
            
            i_backup_already_created_for_file = 0
            i_backup_created_in_method = self.execute_replace_words_in_one_file(
                                                   s_file
                                                   ,i_backup_already_created_for_file)
            if( i_backup_created_in_method == 1):
                i_backup_already_created_for_file = 1
                    
        JT_Logger.print_output( "[METHOD_OUT]" 
                                        + " [execute_replace_words_in_founded_files")

    #==================================================================
    #
    #==================================================================
        
            
    def execute_replace_words_in_files_robo(self):
        
        JT_Logger.print_output( "[METHOD_IN]" 
                                        + " [execute_replace_words_in_files_robo]" )

        JT_Logger.print_output( "[METHOD_IN]" 
                                        + " [execute_replace_words_in_files_robo]" )
        
        for ii_find_file in self.m_find_files.m_find_files:
            ii_find_file_typed =JT_FIND_File()
            ii_find_file_typed = ii_find_file
            s_file = ii_find_file_typed.m_file_robo
            
            JT_Logger.print_output( "")
            JT_Logger.print_output( "[INFO][REPLACE_WORDS_IN_FILE]") 
            JT_Logger.print_output( "[FILE:" + s_file + "]")
            
            i_backup_already_created_for_file = 0
            i_backup_created_in_method = self.execute_replace_words_in_one_file(
                                                   s_file
                                                   ,i_backup_already_created_for_file)
            
            if( i_backup_created_in_method == 1):
                i_backup_already_created_for_file = 1
                    
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                        + " [execute_replace_words_in_files_robo")

        JT_Logger.print_output( "[METHOD_OUT]" 
                                        + " [execute_replace_words_in_files_robo")

    #==================================================================
    #
    #==================================================================

    def execute_replace_words_in_one_file(self
                                          ,s_file
                                          ,pi_backup_already_created_for_file):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                        + "[execute_replace_words_in_one_file]"
                                        + "[FILE:" + s_file + "]"
                                        + "[backup:" + str(pi_backup_already_created_for_file) + "]"
                                        )
        i_backup_created_in_method = 0
        i_number_fined_patterns = 0 
        for ii_dd in self.m_replacements.m_repl_words:
            ii_dd_t = JT_FIND_Replacement()
            ii_dd_t = ii_dd
            
            is_word_finded = self.execute_find_string_in_file(
                                           ii_dd_t.m_word_old
                                           ,ii_dd_t.m_word_new
                                           ,s_file
                                           )
            if is_word_finded == 0:
                continue
            
            JT_Logger.print_output( "[FOUND_PATTERN]" 
                                       + "[" + str(ii_dd_t.m_word_old ) + "]" 
                                       + "[" + ii_dd_t.m_word_new + "]")
            
            if is_word_finded == 1:
                i_number_fined_patterns = i_number_fined_patterns +1                
                if self.m_execute_replace == 1 :
                    if(pi_backup_already_created_for_file == 0 
                       and i_backup_created_in_method == 0):
                        JT_FIND_FilesHelper().create_backup_file(
                                                                 s_file
                                                                 ,self.m_stamp)
                        i_backup_created_in_method = 1
                        
                self.execute_replace_string_in_file(
                                           ii_dd_t.m_word_old
                                           ,ii_dd_t.m_word_new
                                           ,s_file
                                           )
            
                    
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[execute_replace_words_in_one_file"
                                       + "[i_backup_created_in_method:" 
                                       + str(i_backup_created_in_method) + "]")
        
        JT_Logger.print_output( "[FOUND_PATTERNS_TO_REPLACE]" 
                                       + "[" + str(i_number_fined_patterns ) + "]")
        
        return i_backup_created_in_method
    
    #==================================================================
    #
    #==================================================================

    def execute_find_string_in_file(self
                                       ,seeking_text
                                       ,replaced_text
                                       ,p_full_file_path
                                       ):    
        
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[execute_find_string_in_file]" 
                                       + "[seeking_text:" + seeking_text + "]" 
                                       + "[replaced_text:" + replaced_text + "]" 
                                       + "[file:" + p_full_file_path + "]" )
        
                                
        is_word_finded =0
        dd_file = None
        
        try:
            dd_file = open(p_full_file_path)
        except:
            JT_Logger.trace_hard_level_16("[METHOD_OUT]" 
                                          + "[execute_find_string_in_file]" 
                                          + " [FILE_NOT_EXIST]" 
                                          + "[" + p_full_file_path + " ]")
            is_word_finded = 0
            return is_word_finded
        
        ll_lines = dd_file.readlines()
        
        for line in ll_lines:    
            pos = string.find(line, seeking_text)            
            if  pos >= 0:                    
                is_word_finded = 1
                JT_Logger.print_output( "")
                JT_Logger.print_output( "[TEST][TEST_REPLACE]" 
                                        + "[seeking_text:"+ seeking_text +"]" 
                                        + "[replaced_text:" + replaced_text + "]")
                        
                JT_Logger.print_output( "[TEST][TEST_REPLACE]" 
                                        + " [pos:" + str(pos) + "]" 
                                        + "[line: " + line[:-1] + "]")
                JT_Logger.print_output( "[TEST][TEST_REPLACE]"                                              
                                        + "[file:" + p_full_file_path + "]")
                 
                
                JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[execute_find_string_in_file]" 
                                       + "[" + str(is_word_finded) + "]")
                                    
        return is_word_finded
    
    #==================================================================
    #
    #==================================================================

    def execute_replace_string_in_file(self
                                       ,seeking_text
                                       ,replaced_text
                                       ,p_full_file_path
                                       ):    
        
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[execute_replace_string_in_file]" 
                                       + "[seeking_text:" + seeking_text + "]" 
                                       + "[replaced_text:" + replaced_text + "]" 
                                       + "[file:" + p_full_file_path + "]" )
        
        is_backup_created_in_method = 0                        
        
        dd_file = None
        
        try:
            dd_file = open(p_full_file_path)
        except:
            JT_Logger.trace_hard_level_16("[METHOD_OUT]" 
                                          + "[execute_replace_string_in_file]" 
                                          + "[FILE_NOT_EXIST]" 
                                          + "[" + p_full_file_path + " ]")
            
            is_backup_created_in_method = 0
            return is_backup_created_in_method
        
        ll_lines = dd_file.readlines()
        
        for line in ll_lines:    
            pos = string.find(line, seeking_text)            
            if  pos >= 0:                    
                if self.m_execute_replace == 1 :           
                    JT_Logger.print_output( "")         
                    JT_Logger.print_output( "[EXED][EXECUTE_REPLACE]" 
                                            + "[seeking_text:"+ seeking_text +"]" 
                                            + "[replaced_text:" + replaced_text + "]")
                            
                    JT_Logger.print_output( "[EXEC][EXECUTE_REPLACE]" 
                                            + "[pos:" + str(pos) + "]" 
                                            + "[line: " + line[:-1] + "]")
                    
                    JT_Logger.print_output( "[EXEC][EXECUTE_REPLACE]"                                              
                                            + "[file:" + p_full_file_path + "]")
                    
                                            
                    JT_FIND_FilesHelper().replace_string_in_file(
                                                p_full_file_path
                                                , seeking_text
                                                , replaced_text
                                                )
            
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[execute_replace_string_in_file]" )
        return is_backup_created_in_method
    
    #==================================================================
    #
    #==================================================================

    def build_list_of_install_config_files(self,p_kgr):        
        self.m_find_files.build_list_of_config_files(p_kgr)

    #==================================================================
    #
    #==================================================================
    
    def set_debug_mode_from_argv(self):
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[set_debug_mode_from_argv]")
        
        s_debug_mode = "no_debug_mode"
        s_tmp = self.get_argv_pos(1)
        
        if(s_tmp != "not_set"):
            s_debug_mode = s_tmp
         
        JT_LoggerSettings().uset_to_output()
        
        if( s_debug_mode == "debug_mode"):
            self.m_debug_mode = 1
            JT_LoggerSettings().set_to_output()
        else:
            self.m_debug_mode = 0
            JT_LoggerSettings().uset_to_output()

        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[set_debug_mode_from_argv]"
                                       + "[s_debug_mode:" + s_debug_mode + "]")
        return s_debug_mode
    
    #==================================================================
    #
    #==================================================================
    def set_cp_temp_to_def_from_argv(self):
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[set_cp_temp_to_def_from_argv]")
        s_cp_temp_to_def_mode  = "no_cp_temp_to_def"
        s_tmp = self.get_argv_pos(3)        
        if(s_tmp != "not_set"):
            s_cp_temp_to_def_mode = s_tmp

        self.m_execute_copy_files_template_to_def = 0        
        if(s_cp_temp_to_def_mode == "cp_temp_to_def"):
            self.m_execute_copy_files_template_to_def = 1            
        else:
            self.m_execute_copy_files_template_to_def = 0

            
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[set_cp_temp_to_def_from_argv]"
                                       + "[" + s_cp_temp_to_def_mode + "]")
   
    #==================================================================
    #
    #==================================================================
        
    def set_cp_def_to_robo_from_argv(self):
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[set_cp_def_to_robo_from_argv]")
        
        s_cp_def_to_robo_mode  = "no_cp_temp_to_def"
        s_tmp = self.get_argv_pos(4)        
        if(s_tmp != "not_set"):
            s_cp_def_to_robo_mode = s_tmp

        self.m_execute_copy_files_default_to_robo = 0        
        if(s_cp_def_to_robo_mode == "cp_def_to_robo"):
            self.m_execute_copy_files_default_to_robo = 1            
        else:
            self.m_execute_copy_files_default_to_robo = 0
            
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[set_cp_def_to_robo_from_argv]"
                                       + "[s_cp_def_to_robo_mode:" + s_cp_def_to_robo_mode + "]")
        return s_cp_def_to_robo_mode
    #==================================================================
    #
    #==================================================================
            
    def set_replace_mode_from_argv(self):
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[set_replace_mode_from_argv]")
        
        self.unset_replace()
        
        if(self.get_argv_pos(2) =="replace_mode"):        
            self.set_replace()
        else:
            self.unset_replace()

        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[set_replace_mode_from_argv]")
        
    #==================================================================
    #
    #==================================================================


    def get_argv_pos(self,p_ii):
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[get_argv_pos]" 
                                       + "[ii:" + str( p_ii ) + "]")
                
        s_debug = "not_set"
        if (len(sys.argv)) > p_ii:
            s_debug = sys.argv[p_ii]        

        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[get_argv_pos]"
                                       + "[s_debug:" + str( s_debug ) + "]"
                                       )
        return s_debug
    
            
    #==================================================================
    #
    #==================================================================
        
    def install_kgr_36JT(self, p_old, p_new):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[install_kgr_36JT]")
        
        self.create_stamp()      
        self.unset_replace()
        #self.set_replace()
        self.set_debug_mode_from_argv()
                  
        self.build_list_of_install_config_files("kgr36JT")
        
        self.m_replacements.init_replacement_words_from_active_config_kgr36JT()
        
        self.print_settings()
                        
        self.execute_replace_words_in_files_config()
        
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[install_kgr_36JT]")
        
    #==================================================================
    #
    #==================================================================
    
    def replace_generic_to_kgr35b_from_kgr35b_mask_xx_3xx(self):
                
        JT_Logger.trace_hard_level_16 ( "[METHOD_IN]" 
                                        + " [replace_generic_to_kgr35b_from_kgr35b_maskxx]")
        self.create_stamp()
        self.set_debug_mode_from_argv()
        self.unset_replace()
        self.set_ext_all_files()
        self.add_rksup_config_path("kgr35b")        
        
        self.build_list_of_files_with_find()
        self.m_replacements.build_words_by_mask_xx_3xx("10","10","5b","5b")
        
        self.print_settings()
        
        
        #self.execute_replace_words_in_files_config()
        JT_Logger.trace_hard_level_16 ( "[METHOD_OUT]" 
                                        + " [replace_generic_to_kgr35b_from_kgr35b_maskxx]")

    #==================================================================
    #
    #==================================================================

    def replace_generic_to_kgr36c_from_kgr36_mask_xx_3xx(self):
                
        JT_Logger.trace_hard_level_16 ( "[METHOD_IN]" 
                                        + " [replace_generic_to_kgr35b_from_kgr35b_maskxx]")
        self.create_stamp()
        self.set_debug_mode_from_argv()
        self.unset_replace()
        self.set_ext_all_files()
        self.add_rksup_config_path("kgr36c")        
        
        self.build_list_of_files_with_find()
        self.m_replacements.build_words_by_mask_xx_3xx("10","10","6c","6c")
        
        self.print_settings()
        
        
        #self.execute_replace_words_in_files_config()
        JT_Logger.trace_hard_level_16 ( "[METHOD_OUT]" 
                                        + " [replace_generic_to_kgr35b_from_kgr35b_maskxx]")
        
    #==================================================================
    #
    #==================================================================
        
    def replace_generic_to_kgr36JT_from_kgr35b_mask_xx_3xx(self):
                
        JT_Logger.trace_hard_level_16 ( "[METHOD_IN]]" 
                                        + "[replace_generic_to_kgr35b_from_kgr35b_maskxx]")
        self.create_stamp()
        self.unset_replace()
        self.set_debug_mode_from_argv()
        self.set_ext_all_files()                        
        self.add_rksup_config_path("kgr36JT")
        self.build_list_of_files_with_find()
        self.build_words_by_mask_xx_3xx("10","19","5b","6JT")
        self.print_settings()                
        #self.execute_replace_words_in_files_config()
        
        JT_Logger.trace_hard_level_16 ( "[METHOD_OUT]" 
                                        + "[replace_generic_to_kgr35b_from_kgr35b_maskxx]")

    #==================================================================
    #
    #==================================================================
    def make_directory_jboss_default(self,p_kgr):
        """make_directory_jboss_default"""
        try:
            JT_FIND_FilesHelper().make_directory("/rksup/config/" + p_kgr + "/jt_etc_default")
            JT_FIND_FilesHelper().make_directory("/rksup/config/" + p_kgr + "/jt_etc_default/bckp")
        except:
            JT_Logger.print_exception("[METHOD_OUT_EXC][make_directory_jboss_default]")
    #==================================================================
    #
    #==================================================================
        
    def make_directory_jboss_robo(self,p_kgr):
        """make_directory_jboss_robo"""
        try:
            JT_FIND_FilesHelper().make_directory("/rksup/config/" + p_kgr + "/jt_etc_robo")
            JT_FIND_FilesHelper().make_directory("/rksup/config/" + p_kgr + "/jt_etc_robo/bckp")
        except:
            JT_Logger.print_exception("[METHOD_OUT_EXC][make_directory_jboss_robo]")
            
    #==================================================================
    #
    #==================================================================
            
        
    def create_install_jboss_files(self):
        """create_install_jboss_files"""
        
        JT_Logger.trace_hard_level_16 ( "[METHOD_IN]]" 
                                        + "[create_install_jboss_files]")
        
        self.create_stamp()
        #self.set_replace()
        self.unset_replace()
        self.set_debug_mode_from_argv()

        #create default
        self.make_directory_jboss_default("kgr36JT")
        self.make_directory_jboss_robo("kgr36JT")
        self.m_find_files.init_list_of_files_to_empty()                    
        self.m_find_files.build_list_of_installed_jboss_files( "jt_etc_default"
                                                              , "jt_etc_robo"
                                                              , "kgr36JT"
                                                              , "36.01.010")
        
        self.print_settings()
        self.execute_copy_files_template_to_default()        
        
        JT_Logger.trace_hard_level_16 ( "[METHOD_OUT]" 
                                        + "[create_install_jboss_files]")

    #==================================================================
    #
    #==================================================================
       
    def exec_os_command(self,s_cmd):
        try:
            try:
                JT_Logger.print_output("")
                JT_Logger.print_output("[METHOD_IN][exec_os_command][" + s_cmd + "]")
                JT_Logger.print_output("")
                
            except:
                print "error_exec_os_command_header"
                
            JT_Os.run_subprocess_popen_strip_without_logging(s_cmd)          
              
        except:
            JT_Logger.print_exception("\nException_in_exec_os_command")
            print "exec_os_command"
            
        
        
    #==================================================================
    #
    #==================================================================
    def set_state_from_parameters(self
                           ,s_debug_mode
                           ,s_replace_mode
                           ,s_cp_temp_to_def
                           ,s_cp_def_to_robo):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[set_state_from_parameters]")
                                
        JT_Logger.print_output("[set_state_from_parameters][s_debug_mode:" + s_debug_mode + "]")
        JT_Logger.print_output("[set_state_from_parameters][s_replace_mode:" + s_replace_mode + "]")
        JT_Logger.print_output("[set_state_from_parameters][s_cp_temp_to_def:" + s_cp_temp_to_def + "]")        
        JT_Logger.print_output("[set_state_from_parameters][s_cp_def_to_robo:" + s_cp_def_to_robo + "]")
                                
        if(s_debug_mode == "debug_mode"):
            self.m_debug_mode = 1;
            JT_LoggerSettings().set_to_output()
        else:
            self.m_debug_mode = 0;
            JT_LoggerSettings().uset_to_output()
        
        self.unset_replace()        
        if(s_replace_mode =="replace_mode"):        
            self.set_replace()
        else:
            self.unset_replace()
            
        self.m_execute_copy_files_template_to_def = 0        
        if(s_cp_temp_to_def == "cp_temp_to_def"):
            self.m_execute_copy_files_template_to_def = 1            
        else:
            self.m_execute_copy_files_template_to_def = 0


        self.m_execute_copy_files_default_to_robo = 0            
        if(s_cp_def_to_robo == "cp_def_to_robo"):
            self.m_execute_copy_files_default_to_robo = 1            
        else:
            self.m_execute_copy_files_default_to_robo = 0
            
    #==================================================================
    #
    #==================================================================

    def build_jboss_default_36JT(self):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[build_jboss_default_36JT]")
                
        s_debug_mode = self.set_debug_mode_from_argv()              
        s_replace_mode = self.set_replace_mode_from_argv()
        s_cp_def_to_robo = self.set_cp_def_to_robo_from_argv()
        s_cp_temp_to_def = self.set_cp_temp_to_def_from_argv()
        
        self.internal_build_kgr(
                                "kgr36JT"
                                ,"36"
                                ,"36.01.010"
                                , s_debug_mode
                                ,s_replace_mode
                                ,s_cp_temp_to_def
                                ,s_cp_def_to_robo)
        
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[build_jboss_default_36JT]")
        
    #==================================================================
    #
    #==================================================================

    def internal_build_kgr(self
                           ,s_kgr
                           ,s_kgr_version
                           ,s_kgr_level
                           ,s_debug_mode
                           ,s_replace_mode
                           ,s_cp_temp_to_def
                           ,s_cp_def_to_robo):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN]" 
                                       + "[internal_build_kgr]")
        
        JT_Logger.print_output("[internal_build_kgr][s_debug_mode:" + s_debug_mode + "]")
        JT_Logger.print_output("[internal_build_kgr][s_replace_mode:" + s_replace_mode + "]")
        JT_Logger.print_output("[internal_build_kgr][s_cp_temp_to_def:" + s_cp_temp_to_def + "]")        
        JT_Logger.print_output("[internal_build_kgr][s_cp_def_to_robo:" + s_cp_def_to_robo + "]")
        
        self.create_stamp()
        self.unset_replace()
        self.set_state_from_parameters(
                                       s_debug_mode
                                       ,s_replace_mode
                                       ,s_cp_temp_to_def
                                       ,s_cp_def_to_robo)
                          
        self.make_directory_jboss_default( s_kgr )
        self.make_directory_jboss_robo( s_kgr )
                  
        JT_FIND_Files().show_jboss_files()                  
        self.m_find_files.init_list_of_files_to_empty()        
        self.m_find_files.build_list_of_installed_jboss_files(
                                                              "jt_etc_default"
                                                              , "jt_etc_robo"
                                                              , s_kgr
                                                              , s_kgr_level)
        
        self.m_find_files.build_list_of_installed_kgr_files(
                                                              "jt_etc_default"
                                                              , "jt_etc_robo"
                                                              , s_kgr
                                                              , s_kgr_level)
        self.m_replacements.m_kgr = s_kgr
        self.m_replacements.m_ver = s_kgr_level        
        self.m_replacements.init_replacement_words_from_active_config_kgr(
                                                                              s_kgr
                                                                              ,s_kgr_version
                                                                              ,s_kgr_level
                                                                              )
        
        self.print_settings()
        
        self.remove_backup_files_before(s_kgr)    
        
        self.execute_copy_files_template_to_default()
            
        self.execute_copy_files_default_to_robo()
                                
        self.execute_replace_words_in_files_robo()
        
        self.remove_backup_files_after(s_kgr)
                
        self.print_examples_of_commands(s_kgr)
        
        JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                       + "[internal_build_kgr]")
        
    
    #==================================================================
    #
    #==================================================================
    
    def remove_backup_files_before(self,s_kgr):
        if(self.m_execute_replace == 1):
            s_cmd = "mv /rksup/config/" + s_kgr + "/jt_etc_robo/*backupST* /rksup/config/" + s_kgr + "/jt_etc_robo/bckp"
            JT_Logger.print_output("[MOVE_BACKUP_FILES_BEFORE][" + s_cmd + "]")
            self.exec_os_command("mv /rksup/config/" + s_kgr + "/jt_etc_robo/*backupST* /rksup/config/" + s_kgr + "/jt_etc_robo/bckp")
            JT_Logger.print_output("[MOVE_BACKUP_FILES_BEFORE][SUCCEDDED]")
    #==================================================================
    #
    #==================================================================
    
    def remove_backup_files_after(self,s_kgr):
        if(self.m_execute_replace == 1):
            s_cmd = "mv /rksup/config/" + s_kgr + "/jt_etc_robo/*backupST* /rksup/config/" + s_kgr + "/jt_etc_robo/bckp"
            JT_Logger.print_output("[MOVE_BACKUP_FILES_AFTER][" + s_cmd + "]")
            self.exec_os_command( s_cmd )
            self.exec_os_command("mv /rksup/config/" + s_kgr + "/*0 /rksup/config/" + s_kgr + "/bckp")
            self.exec_os_command("mv /rksup/config/" + s_kgr + "/*1 /rksup/config/" + s_kgr + "/bckp")
            self.exec_os_command("mv /rksup/config/" + s_kgr + "/*2 /rksup/config/" + s_kgr + "/bckp")
            self.exec_os_command("mv /rksup/config/" + s_kgr + "/*3 /rksup/config/" + s_kgr + "/bckp")            
            JT_Logger.print_output("[MOVE_BACKUP_FILES_AFTER][SUCCEDDED]")
            
    #==================================================================
    #
    #==================================================================
        
    def print_examples_of_commands(self,s_kgr):
        JT_Logger.print_output( "mv /rksup/config/" + s_kgr + "/jt_etc_robo/*backupST* /rksup/config/kgr36JT/bckp")
        JT_Logger.print_output( "cp /rksup/config/" + s_kgr + "/jt_etc_default/* /rksup/config/kgr36JT/jt_etc_robo")
        JT_Logger.print_output( "cp /rksup/config/" + s_kgr + "/jt_etc_robo/* /rksup/config/kgr36JT/")
        JT_Logger.print_output( "grep '$V' /rksup/config/" + s_kgr + "/jt_etc_robo/*")

        
    #==================================================================
    #
    #==================================================================
    
    def replace_one_setting_in_kgr(self
                                       ,p_kgr
                                       ,p_world_old
                                       ,p_world_new
                                       ,p_debug_mode
                                       ,p_replace_mode):
                    
            JT_Logger.trace_hard_level_16 ( "[METHOD_IN]" 
                                            + " [replace_generic_to_kgr35b_from_kgr35b_maskxx]")
            self.create_stamp()
            self.m_debug_mode = p_debug_mode
            
            if (self.m_debug_mode == 1):
                JT_LoggerSettings().set_to_output()
            else:
                JT_LoggerSettings().uset_to_output()
            
            self.m_execute_replace = p_replace_mode
            #p_replace_mode 
            self.set_ext_all_files()
            self.add_rksup_config_path(p_kgr)        
            
            self.build_list_of_files_with_find()
            
            self.m_replacements.add_repl_sentences(
                                                   p_world_old
                                                   ,p_world_new)
            
            self.print_settings()
            JT_Logger.print_output("#####################################"
                                   + "#####################################")
            JT_Logger.print_output("#")
            JT_Logger.print_output("#           START REPLACE")
            JT_Logger.print_output("#")
            JT_Logger.print_output("#####################################"
                                   "#####################################")
                      
            self.execute_replace_words_in_founded_files()
            
            JT_Logger.print_output("#####################################"
                                   + "#####################################")
            JT_Logger.print_output("#")
            JT_Logger.print_output("#           STOP REPLACE")
            JT_Logger.print_output("#")
            JT_Logger.print_output("#####################################"
                                   "#####################################")
            
            #self.execute_replace_words_in_files_config()
            JT_Logger.trace_hard_level_16 ( "[METHOD_OUT]" 
                                            + " [replace_generic_to_kgr35b_from_kgr35b_maskxx]")
            
    #==================================================================
    #
    #==================================================================
                    
class JT_FIND_KgrEnvironmentFinder_Exec:
    def exec_main(self):
        cc = JT_FIND_KgrEnvironmentFinder()
        cc.create_stamp()
        #cc.replace_one_setting_in_kgr("kgr36c","17190","17200",0,0)
        cc.replace_one_setting_in_kgr("kgr36c","GDN_KGR36JC","GDN_KGR36C",0,1)
        
    #==================================================================
    #
    #==================================================================

if __name__ == '__main__':
    JT_FIND_KgrEnvironmentFinder_Exec().exec_main()
    
    #==================================================================
    #
    #==================================================================
        