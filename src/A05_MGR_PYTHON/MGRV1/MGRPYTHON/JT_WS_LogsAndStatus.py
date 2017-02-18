import sys, os

here = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.normpath(os.path.join(here, '../SOAPpy')))

from SOAPpy import SOAPProxy

class JT_WS_LogsAndStatus:    
    def __init__(self):
        self.m_Line = ""
        self.m_user_id = ""
        self.m_pid_id = ""
        
    def exec_test(self):
        jobj = self.read_file("obj5.ser")
        pobj = javaobj.loads(jobj)
        print pobj

