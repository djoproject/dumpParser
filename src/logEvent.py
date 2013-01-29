#!/usr/bin/python

class LogEvent(object):
    def __init__(self,time,name,line):
        self.time = time
        self.name = name
        self.lines = [line]
        
        #self.addLine(line)

    def addLine(self,line):
        self.lines.append(line)
        
    def __str__(self):
        return "("+str(self.name)+") at "+str(self.time)+" : "+str(self.lines)
