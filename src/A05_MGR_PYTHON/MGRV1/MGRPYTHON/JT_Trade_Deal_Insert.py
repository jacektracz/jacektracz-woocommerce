#==================================================================
#
#    Copyright (c) 2011 Thomson Reuters by jacek Tracz
#    
#==================================================================
import sys
import os
import shutil

from JT_Logger import JT_Logger
from JT_FIND_FilesHelper import JT_FIND_FilesHelper
class JT_Trade_DealsInsert:
    
    #==================================================================
    #
    #==================================================================

    def create_deals(self
                     , i_ii
                     , i_shift
                     , s_suffix):
        
        self.print_log("[METHOD_IN][create_deals][" + str(i_ii) + "]")
                                      
        #JT_Logger.trace_hard_level_16(i_ii)
        s_directory = "/rksup/log/rembrandt/importexport"
        s_file_pattern = "jt-insert-deal.tmp"
        s_file_pattern_full_path = "/rksup/log/rembrandt/importexport/jt-insert-deal-" + s_suffix + "0.tmp"
        s_file_created_suffix = "jt-insert-deal-perftest-" + s_suffix + "0-";
        
        for ii in range(i_ii):
            ii_shifted = ii + i_shift
            dd_ff = JT_FIND_FilesHelper()            
            s_file_tmp = s_directory + "/" + s_file_created_suffix + str(ii_shifted) + ".tmp"               
            dd_ff.copy_file(
                            s_file_pattern_full_path
                            ,s_file_tmp)

        for ii in range(i_ii):
            ii_shifted = ii + i_shift
            dd_ff = JT_FIND_FilesHelper()
            s_file_tmp = s_directory + "/" + s_file_created_suffix + str(ii_shifted) + ".tmp"               
            dd_ff.replace_string_in_file(
                            s_file_tmp
                            ,"II_DEAL_STAMP"
                            ,"JT-50-" + str(ii_shifted))

        for ii in range(i_ii):
            ii_shifted = ii + i_shift
            dd_ff = JT_FIND_FilesHelper()
            s_file_tmp = s_directory + "/" + s_file_created_suffix + str(ii_shifted) + ".tmp"
            s_file_xml = s_directory + "/" + s_file_created_suffix + str(ii_shifted) + ".xml"               
            dd_ff.copy_file(
                            s_file_tmp
                            ,s_file_xml)

        self.print_log("[METHOD_IN][create_deals]") 


    def delete_temp_files( self ):
        i_range = 100000
        for i_ii_1 in range(i_range):
            i_ii= 100000 + i_ii_1
            ss_suffix = "/rksup/log/rembrandt/importexport/jt-insert-deal-perftest-60-"            
            ss_file = ss_suffix + str( i_ii ) + ".tmp"
            self.remove_file(ss_file)
            ss_file = ss_suffix + str( i_ii ) + ".xml.success"
            self.remove_file(ss_file)
            ss_file = ss_suffix + str( i_ii ) + ".xml.failed"
            self.remove_file(ss_file)
            ss_file = ss_suffix + str( i_ii ) + ".xml.done"
            self.remove_file(ss_file)
            ss_file = ss_suffix + str( i_ii ) + ".xml.reply"
            self.remove_file(ss_file)


    def remove_file(self, ss_file):
        self.print_log( ss_file)
        try:
            os.remove(ss_file)
        except:
            self.print_log( "no_file")



    def print_log(self, ss):
            print ss

            
if __name__ == '__main__':
    
    dd_deals = JT_Trade_DealsInsert()
    deals_suffix = sys.argv[1]
    dd_deals.print_log( "deals_suffix:" + deals_suffix )
    number_of_deals = sys.argv[2]
    dd_deals.print_log( "number_of_deals:" + number_of_deals )
    start_shift = sys.argv[3]
    dd_deals.print_log( "start_shift:" + start_shift )
    
    dd_deals.create_deals(
                          int(number_of_deals)
                          ,int(start_shift)
                          ,deals_suffix)
    
    #dd_deals.delete_temp_files()
    
    
