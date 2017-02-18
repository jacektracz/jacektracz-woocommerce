
import pexpect

class JT_SSH:
    
    def __init__(self):
        self.child = None
        self.PROMPT = '[$#]' 
        
#==================================================================
#
#==================================================================
        
    def ssh_inner_initialize(self, user, password, host):
            self.child = pexpect.spawn("ssh %s@%s"%(user, host))
            if self.child != None:
                i = self.child.expect(['password:', r"yes/no"], timeout=120)
                if i==0:
                    self.child.sendline(password)
                elif i==1:
                    self.child.sendline("yes")
                    self.child.expect("password:", timeout=120)
                    self.child.sendline(password)
                    self.child.expect(self.PROMPT)

#==================================================================
#    
#==================================================================

    def do_ssh_command(self, command):
        """send a command and return the response"""
        self.child.sendline(command)
        self.child.expect(self.PROMPT)
        response = self.child.before
        return response
#==================================================================
#    
#==================================================================
    
    def close(self):
        """close the connection"""
        self.child.close()
        
#==================================================================
#    
#==================================================================
    @staticmethod
    def do_ssh( user, password,command):
        ssh = JT_SSH()
        ssh.ssh_inner_initialize(user,password,"localhost")        
        dd_out = ssh.do_ssh_command(command)                
        ssh.close()
        return dd_out

#==================================================================
#    
#==================================================================
        
#if __name__=="__main__":
#import getpass
#password = getpass.getpass("Password: ")
#ssh = SSH("RemoteUsername", password, "RemoteHost")
#print ssh.command("pwd")
#ssh.close()
