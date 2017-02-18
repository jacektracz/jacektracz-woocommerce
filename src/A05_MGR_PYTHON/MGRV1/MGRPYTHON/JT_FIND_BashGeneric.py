import os
import subprocess
import optparse

class JT_FIND_BashGeneric:
    
    
    #HOLDING_SPOT="""fake_command"""
    
    #Determines Home Directory Usage in Gigs
    HOMEDIR_USAGE = """
    du -sh $HOME | cut -f1
    """
    
    #Determines IP Address
    IPADDR = """
    /sbin/ifconfig -a | awk '/(cast)/ { print $2 }' | cut -d':' -f2 | head -1
    """
    
    VERBOSE=False
    VERBOSE_DN=False
    #==================================================================
    #
    #==================================================================        
    
    def run_subprocess_popen(self,cmd) :
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return proc.communicate()[0]
        
    #==================================================================
    #
    #==================================================================        
    
    def run_subprocess_call(self, cmd):
            subprocess.call(cmd, shell=True)

    
    #==================================================================
    #
    #==================================================================        
    
    def run_os_variable(self, p_var,p_val):
            os.environ[p_var] = p_val
            os.system('python echoenv.py')

        
    #==================================================================
    #
    #==================================================================        
    
    def run_os_popen(self, cmd):
            os.popen(cmd)
    
    #==================================================================
    #
    #==================================================================        
                
    def run_subprocess_popen_strip(self,cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read().strip()
        return out
    
        
    #==================================================================
    #
    #==================================================================        
    
    def report(self,output,cmdtype="UNIX COMMAND:"):
    
        if self.VERBOSE:
            print "%s: %s" % (cmdtype, output)
        else:
            print output
        
    #==================================================================
    #
    #==================================================================        
    
    def print_do_nothing(self,tt):
        if self.VERBOSE_DN:
            print tt
        
    def controller(self):        
        #Create instance of OptionParser Module, included in Standard Library
        p = optparse.OptionParser(description='A unix toolbox',
                                                prog='py4sa',
                                                version='py4sa 0.1',
                                                usage= '%prog [option]')
        p.add_option('--ip','-i', action="store_true", help='gets current IP Address')
        p.add_option('--usage', '-u', action="store_true", help='gets disk usage of homedir')
        p.add_option('--verbose', '-v',
                    action = 'store_true',
                    help='prints verbosely',
                    default=False)
        
        #Option Handling passes correct parameter to run_subprocess_popen_strip
        options, arguments = p.parse_args()
        self.print_do_nothing(arguments)
        if options.verbose:
            self.VERBOSE=True
        if options.ip:
            value = self.run_subprocess_popen_strip(self.IPADDR)
            self.report(value,"IPADDR")
        elif options.usage:
            value = self.run_subprocess_popen_strip(self.HOMEDIR_USAGE)
            self.report(value, "HOMEDIR_USAGE")
        else:
            p.print_help()
    
        
    #==================================================================
    #
    #==================================================================        
    
    def main(self):
        self.controller()
