
import javaobj
import os
import sys

class JT_ReadJavaObjects:    
    def __init__(self):
        self.m_Line = ""
        self.m_user_id = ""
        self.m_pid_id = ""
        
    def exec_test(self):
        jobj = self.read_file("obj5.ser")
        pobj = javaobj.loads(jobj)
        print pobj
        
    def exec_test_2(self):
        
        marshaller = javaobj.JavaObjectUnmarshaller(open("obj5.ser"))
        pobj = marshaller.readObject()
        print pobj                

    def exec_test_3(self):
        
        dd = "/files2/sybdevices/DS_PERKUN/KGR_FLAT_DATA/tmp/LogsAndStatusDump/201403241820/182850.180.dmp"
        marshaller = javaobj.JavaObjectUnmarshaller(open(dd))
        pobj = marshaller.readObject()
        print pobj                
        
    def exec_test_4(self):
        
        dd = "/files2/sybdevices/DS_PERKUN/KGR_FLAT_DATA/tmp/LogsAndStatusDump/201403241820/182850.180.dmp"        
        jobj = self.read_file(dd)
        pobj = javaobj.loads(jobj)
        print pobj
        
    def read_file(self,filename):
      fh = open(filename, "r")
      try:
          return fh.read()
      finally:
          fh.close()
    
    def write_file(filename, data):
      fh = open(filename, "w")
      try:
          fh.write(data)
      finally:
          fh.close()

    def exec_test_6(self):        
        dd = "/files2/sybdevices/DS_PERKUN/KGR_FLAT_DATA/tmp/LogsAndStatusDump/201403241820/"
        ll_files = self.get_filepaths(dd)
        for ii_ss in ll_files :
            print "FILE_START:" + ii_ss        
            jobj = self.read_file(ii_ss)
            pobj = javaobj.loads(jobj)
            print pobj
            print "FILE_END:" + ii_ss
          
    def get_filepaths(self,directory):
        """
        This function will generate the file names in a directory 
        tree by walking the tree either top-down or bottom-up. For each 
        directory in the tree rooted at directory top (including top itself), 
        it yields a 3-tuple (dirpath, dirnames, filenames).
        """
        file_paths = []  # List which will store all of the full filepaths.
    
        # Walk the tree.
        for root, directories, files in os.walk(directory):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
    
        return file_paths  # Self-explanatory.
    

    def exec_file(self):
        dd1 = sys.argv[1]
        #dd = "/files2/sybdevices/DS_PERKUN/KGR_FLAT_DATA/tmp/LogsAndStatusDump/201403241820/" + dd1        
        jobj = self.read_file(dd1)
        pobj = javaobj.loads(jobj)
        print pobj
        
    def exec_tests(self):
        print "start exec ..."
        dd_deals = JT_ReadJavaObjects()
        #dd_deals.exec_test_2()
        print "exec_test_3 ..."
        dd_deals.exec_test_3()
        print "exec_test_4 ..."
        dd_deals.exec_test_4()
        print "exec_test_6 ..."
        dd_deals.exec_test_6()
                    
        print "all done ..."
               
if __name__ == '__main__':
    
    print "start exec ..."
    dd_deals = JT_ReadJavaObjects()
    dd_deals.exec_file()
    print "end exec ..."
        