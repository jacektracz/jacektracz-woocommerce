import sys
import defines
import logging
from pykd import *
from defines import *

def getAddress(localAddr):
    res = dbgCommand("x " + localAddr)
    if res.count("\n") > 1:
        print "[-] Warning, more than one result for", localAddr
    return res.split()[3]

def link(prefix,command,label):
	#print ".printf /D \"<link cmd=\"%s\">%s</link>\\n\"" % (command,label)
	#dbgCommand(".printf /D \"<link cmd=\\\"%s\\\">%s</link>\\n\"" % (command,label));
	dprintln("%s<link cmd=\"%s\">%s</link>"%(prefix,command,label),True)
	
def getAsInt(symbol):
	#print symbol
	return int(dbgCommand(".printf \"\%i\","+symbol))

def getAsPtr(symbol):
	#print symbol
	return dbgCommand(".printf \"\%p\","+symbol)

def getAsHex(symbol):
	#print symbol
	return dbgCommand(".printf \"\%x\","+symbol)

def getAsStr(symbol):
	#print symbol
	return dbgCommand(".printf \"\%ma\","+symbol)

def getAsStrEx(symbol,maxl):
	
    sout = dbgCommand(".printf \"\%ma\","+symbol)
    if len(sout) > maxl:
            sout = sout[:maxl]
    return sout

def getAsStrDbg(symbol):
	#print symbol
	sout = dbgCommand(".printf \"\%ma\","+symbol)
	return sout
