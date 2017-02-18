#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by jacek Tracz
#    
#==================================================================
import os
import shutil

from JT_Logger import JT_Logger
from JT_FIND_FilesHelper import JT_FIND_FilesHelper
class JT_Trade_DealsInsert:
    
    #==================================================================
    #
    #==================================================================

    def create_deals(self
                     , i_ii):
        
        JT_Logger.trace_hard_level_16("[METHOD_IN][create_deals]")
                                      
        JT_Logger.trace_hard_level_16(s_ii)
        s_directory = "/rksup/log/rembrandt/importexport"
        s_file_pattern = "jt-insert-deal.tmp"
        s_file_pattern_full_path = "/rksup/log/rembrandt/importexport/jt-insert-deal.tmp"
        s_file_created_suffix = "jt-insert-deal-perftest-";
        
        for ii in range(i_ii):
            s_file_tmp = s_directory + "/" + s_file_created_suffix + ii + ".tmp"               
            dd_ff.copy_file(
                            s_file_pattern_full_path
                            ,s_file_tmp)

        for ii in range(i_ii):
            s_file_tmp = s_directory + "/" + s_file_created_suffix + ii + ".tmp"               
            dd_ff.replace_string_in_file(
                            s_file_tmp
                            ,"II_DEAL_STAMP"
                            ,"JT-" + ii)

        for ii in range(i_ii):
            s_file_tmp = s_directory + "/" + s_file_created_suffix + ii + ".tmp"
            s_file_xml = s_directory + "/" + s_file_created_suffix + ii + ".xml"               
            dd_ff.copy_file(
                            s_file_tmp
                            ,s_file_xml)

        JT_Logger.trace_hard_level_16("[METHOD_IN][create_deals]") 

if __name__ == '__main__':
    dd_deals = JT_Trade_DealsInsert()
    dd_deals.create_deals(5)


    
