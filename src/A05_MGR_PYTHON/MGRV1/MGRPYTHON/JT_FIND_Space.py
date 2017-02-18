import subprocess
class JT_FIND_Space:
    MESSAGES = "tail /var/log/messages"
    SPACE = "df -h"
    
    cmds = [MESSAGES, SPACE]
    
    def runCommands(self,commands=cmds):

        count=0
        for cmd in self.cmds:
            count+=1
            print "Running Command Number %s" % count
            subprocess.call(cmd, shell=True)
        

#==================================================================
#
#Class JTFind
#
#==================================================================
