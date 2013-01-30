#!/usr/bin/python

from logEvent import LogEvent

#card uid : E0:16:24:66:04:C0:86:2C
class dumpNewDumpEvent(LogEvent):
    def __init__(self,time,line):
        
        line = line.strip()
        
        splittedSpace = line.split(" ")
        
        if(len(splittedSpace) != 4):
            print "WARNING, invalid line to dumpNewDumpEvent : "+line
            return
            
        self.UID = splittedSpace[3]
        self.UID = self.UID.replace(":","")
        
        self.newTime = None
        
        LogEvent.__init__(self,time,"dumpNewDumpEvent",line)
        
    def addLine(self,line):
        print "WARNING, add line not allowed to nmeaSetTimeEvent : "+line
        
    def __str__(self):
        return "dumpNewDumpEvent at "+str(self.time)+", uid = "+str(self.UID)
