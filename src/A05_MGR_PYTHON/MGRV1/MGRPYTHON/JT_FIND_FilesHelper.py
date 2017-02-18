#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by jacek Tracz
#    
#==================================================================
import os
import shutil

from JT_Logger import JT_Logger

class JT_FIND_FilesHelper:
    
    #==================================================================
    #
    #==================================================================

    def replace_string_in_file(self
                               , s_full_file_path
                               , sourceText
                               , replaceText):
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][replace_string_in_file]" 
                         + "[s_full_file_path:" + s_full_file_path + "]" 
                         + "[sourceText:" + sourceText + "]" 
                         + "[replaceText:" + replaceText + "]")         
        
        JT_Logger.trace_hard_level_16( s_full_file_path )
        
        if(os.path.exists(s_full_file_path)):
        
            s_full_temp_name = s_full_file_path + '~x~'        
            
            dd_source_file = open(s_full_file_path, 'rb' )
            s_source_file_lines = dd_source_file.read()
            dd_source_file.close()
            
            
            s_destination_replaced_lines = s_source_file_lines.replace(sourceText, replaceText)
            s_source_file_lines = s_destination_replaced_lines
            dd_destination_file = open(s_full_temp_name,'wb')
                    
            dd_destination_file.write(s_destination_replaced_lines)
            dd_destination_file.close()        
            os.remove(s_full_file_path)
            os.rename(s_full_temp_name, s_full_file_path)
        else:
            JT_Logger.print_output("[replace_string_in_file:FILE_NOT_EXISTS]" 
                                   + "[" + s_full_file_path + "]")
        
        JT_Logger.trace_hard_level_16( "[METHOD_IN][replace_string_in_file]") 

    #==================================================================
    #
    #==================================================================
    
    def replace_strings_in_file_with_backup(self
                                            ,s_full_file_path
                                            , sourceText
                                            , replaceText
                                            ,s_stamp):
        
        JT_Logger.trace_hard_level_16( "replace_strings_in_file_with_backup:" + s_full_file_path + "]" 
                         + "[" + sourceText + "]" 
                         + "[" + replaceText + "]")         
        
        JT_Logger.trace_hard_level_16( s_full_file_path )
        s_full_temp_name=s_full_file_path+'~x~'
        s_full_backup_file_name=s_full_file_path+'.backup'+ s_stamp
        
        dd_source_file = open(s_full_file_path,'rb')
        s_source_file_lines = dd_source_file.read()
        dd_source_file.close()
        
        
        s_destination_replaced_lines = s_source_file_lines.replace(sourceText,replaceText)
        s_source_file_lines = s_destination_replaced_lines
        dd_destination_file = open(s_full_temp_name, 'wb')
                
        dd_destination_file.write( s_destination_replaced_lines )
        dd_destination_file.close()
        JT_Logger.trace_hard_level_16("[INFO][create backup]:" + s_full_backup_file_name)
        
        if(os.path.exists(s_full_file_path)):
            shutil.copy2(s_full_file_path,s_full_backup_file_name)
        else:
            JT_Logger.print_output("[replace_strings_in_file_with_backup:FILE_NOT_EXISTS]" 
                                   + "[" + s_full_file_path + "]")
                        
        os.remove(s_full_file_path)
        os.rename(s_full_temp_name,s_full_file_path)

    #==================================================================
    #
    #==================================================================
            
    def create_backup_file(self,s_full_file_path,s_stamp):
        
        try:
            JT_Logger.trace_hard_level_16( "[METHOD_IN][create_backup_file:" + s_full_file_path + "]")         
            JT_Logger.print_output("[CREATE_BACKUP")         
            
            JT_Logger.trace_hard_level_16( s_full_file_path )        
            s_full_backup_file_name = s_full_file_path + '.backup' + s_stamp
            JT_Logger.print_output("[CREATE_BACKUP_FILE:" + s_full_backup_file_name + "]")
            if(os.path.exists(s_full_file_path)):        
                shutil.copy2(s_full_file_path , s_full_backup_file_name)            
                JT_Logger.print_output("[CREATE_BACKUP:SUCCESS]")        
            else:
                JT_Logger.print_output("[create_backup_file:FILE_NOT_EXISTS]" 
                                   + "[" + s_full_file_path + "]")
        except:
            JT_Logger.print_exception( "[METHOD_OUT_EXC]" + "[create_backup_file]")
            
    #==================================================================
    #
    #==================================================================
            
    def copy_file(self
                  ,s_full_path_file_old
                  ,s_full_path_file_new):
        try:
            JT_Logger.trace_hard_level_16( "[METHOD_IN]" + "[copy_file]" )
            JT_Logger.trace_hard_level_16( "[s_full_path_file_old:" + s_full_path_file_old + "]")
            JT_Logger.trace_hard_level_16( "[s_full_path_file_new:" + s_full_path_file_new + "]")
            
            JT_Logger.print_output("")         
            JT_Logger.print_output("[COPY_FILE]")
            JT_Logger.print_output("[s_full_path_file_old:" + s_full_path_file_old + "]")
            JT_Logger.print_output("[s_full_path_file_new:" + s_full_path_file_new + "]")
            
            if(os.path.exists(s_full_path_file_old)):
                shutil.copy2(s_full_path_file_old , s_full_path_file_new)
                JT_Logger.print_output("[COPY_FILE_SUCCESS]")
            else:
                JT_Logger.print_output("[COPY_FILE_FILE_NOT_EXISTS]" 
                                   + "[" + s_full_path_file_old + "]")
                
                    
            JT_Logger.trace_hard_level_16( "[METHOD_OUT]" + "[copy_file]")
        except:
            JT_Logger.print_exception( "[METHOD_OUT_EXC]" + "[copy_file]")
            
    #==================================================================
    #
    #==================================================================
                                    
    def make_directory(self
                  ,s_full_dir_path
                  ):
        """make_directory"""
        try:
            JT_Logger.trace_hard_level_16( "[METHOD_IN]" + "[make_directory]" 
                                           + "[s_full_dir_path:" + s_full_dir_path + "]"                                       
                                           )         
            JT_Logger.print_output("[make_directory]"
                                        + "[s_full_dir_path:" + s_full_dir_path + "]"        
                                        )
            if(os.path.exists(s_full_dir_path)):
                JT_Logger.print_output("[DIRECTORY_EXISTS][" + s_full_dir_path + "]")
            else:
                os.makedirs(s_full_dir_path)
                JT_Logger.print_output("[MAKE_DIR:SUCCESS]")
            
                    
            JT_Logger.trace_hard_level_16( "[METHOD_OUT]" 
                                           + "[make_directory]"
                                           + "[s_full_dir_path:" + s_full_dir_path + "]")
            
        except:
            JT_Logger.print_exception( "[METHOD_OUT_EXC]" + "[make_directory]")
            
                                        
