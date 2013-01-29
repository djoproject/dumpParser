#!/usr/bin/python

from logEvent import LogEvent
from datetime import datetime
import calendar

#date -s "25 JAN 2013 11:14:11"
class nmeaSetTimeEvent(LogEvent):
    def __init__(self,time,line):
        self.time = time
        
        line = line.strip()
        splittedSpace = line.split(" ")
        
        if len(splittedSpace) != 6 :
            print "(nmeaNewPositionEvent) WARNING, invalid nmea datetime, space split : "+str(line)
            return
            
        try:
            self.day =  int(splittedSpace[2][1:])
        except ValueError as va:
            print "(nmeaNewAltitudeEvent) WARNING, invalid nmea day, int cast : "+str(line)+" "+str(va)
            return
        
        self.month = 01 #TODO splittedSpace[3]
        
        try:
            self.year =  int(splittedSpace[4])
        except ValueError as va:
            print "(nmeaNewAltitudeEvent) WARNING, invalid nmea year, int cast : "+str(line)+" "+str(va)
            return
        
        splittedSpace[5] = splittedSpace[5].strip()
        splittedDoublePoint = splittedSpace[5].split(":")
        
        if len(splittedDoublePoint) != 3 :
            print "(nmeaNewPositionEvent) WARNING, invalid nmea time, double point split : "+str(line)
            return
        
        try:
            self.hour = int(splittedDoublePoint[0])
        except ValueError as va:
            print "(nmeaNewAltitudeEvent) WARNING, invalid nmea hour, int cast : "+str(line)+" "+str(va)
            return

        try:
            self.minute =  int(splittedDoublePoint[1])
        except ValueError as va:
            print "(nmeaNewAltitudeEvent) WARNING, invalid nmea minute, int cast : "+str(line)+" "+str(va)
            return

        try:
            self.second =  int(splittedDoublePoint[2][:-1])
        except ValueError as va:
            print "(nmeaNewAltitudeEvent) WARNING, invalid nmea second, int cast : "+str(line)+" "+str(va)
            return
        
        self.timestamp = calendar.timegm(datetime(self.year,self.month,  self.day ,self.hour,self.minute,   self.second ).utctimetuple()) 
        
        LogEvent.__init__(self,time,"nmeaNewPositionEvent",line)
        
    def addLine(self,line):
        print "WARNING, add line not allowed to nmeaSetTimeEvent : "+line
        
    def __str__(self):
        return "(nmeaSetTimeEvent) at "+str(self.time)+" : "+str(self.day)+"/"+str(self.month)+"/"+str(self.year)+" "+str(self.hour)+":"+str(self.minute)+":"+str(self.second)
        
#position (not new) : 4516.2482N 00635.5607E, fix time : 101417
#position : 4516.2482N 00635.5607E, fix time : 101417
#position : 0000.0000N 00000.0000E
#position (not new) : 0000.0000N 00000.0000E
class nmeaNewPositionEvent(LogEvent):
    def __init__(self,time,line,New=False):
        self.time = time
        self.New = New
        
        line = line.strip()
        splittedDoublePoint = line.split(":")
        
        if len(splittedDoublePoint) != 3 and len(splittedDoublePoint) != 2:
            print "(nmeaNewPositionEvent) WARNING, invalid nmea Position, double point split : "+str(line)
            return
            
        #latitude-longitude
        splittedDoublePoint[1] = splittedDoublePoint[1].strip()
        splittedSpace = splittedDoublePoint[1].split(" ")
        
        if len(splittedDoublePoint) != 2:
            if len(splittedSpace) != 4:
                print "(nmeaNewPositionEvent) WARNING, invalid nmea Position, space split : "+str(line)
                return
                
            self.longitude = splittedSpace[0]
            self.latitude  = splittedSpace[1][:-1]
            
            #fix time
            splittedDoublePoint[2] = splittedDoublePoint[2].strip()
            if len(splittedDoublePoint[2]) != 6:
                print "(nmeaNewPositionEvent) WARNING, invalid nmea Position, fix time length : "+str(line)
                return
                
            self.fixtime = splittedDoublePoint[2]
            #self.hour    = line[-6:-4]
            #self.minute  = line[-4:-2]
            #self.seconds = line[-2:][:2]
        else:
            if len(splittedSpace) != 2:
                print "(nmeaNewPositionEvent) WARNING, invalid nmea Position, space split : "+str(line)
                return
                
            self.longitude = splittedSpace[0]
            self.latitude  = splittedSpace[1]
            
            self.fixtime = None
        
        LogEvent.__init__(self,time,"nmeaNewPositionEvent",line)
        
    def addLine(self,line):
        print "WARNING, add line not allowed to nmeaSetTimeEvent : "+line
        
    def __str__(self):
        return "(nmeaNewPositionEvent) at "+str(self.time)+", longitude = "+str(self.longitude)+", latitude = "+str(self.latitude)

#altitude (not new) : 2873.60009765625 M, fix time : 101418
#altitude : 2873.60009765625 M, fix time : 101418
#altitude (not new) : altitude : 0.0 M
#altitude : 0.0 M
class nmeaNewAltitudeEvent(LogEvent):
    def __init__(self,time,line,New=False):
        self.time = time
        self.New = New
        
        line = line.strip()
        splittedDoublePoint = line.split(":")
        
        if len(splittedDoublePoint) != 3 and len(splittedDoublePoint) != 2:
            print "(nmeaNewAltitudeEvent) WARNING, invalid nmea altitude, double point split : "+str(line)
            return
        
        #altitude
        splittedDoublePoint[1] = splittedDoublePoint[1].strip()
        splittedSpace = splittedDoublePoint[1].split(" ")
        
        if len(splittedDoublePoint) != 2:
            if len(splittedSpace) != 4:
                print "(nmeaNewAltitudeEvent) WARNING, invalid nmea altitude, space split : "+str(line)
                return
        
            try:
                self.altitude = float(splittedSpace[0])
            except ValueError as va:
                print "(nmeaNewAltitudeEvent) WARNING, invalid nmea altitude, float cast : "+str(line)+" "+str(va)
                return
            
            #units
            self.unit = splittedSpace[1][:-1]
        
            #fix time
            splittedDoublePoint[2] = splittedDoublePoint[2].strip()
            if len(splittedDoublePoint[2]) != 6:
                print "(nmeaNewAltitudeEvent) WARNING, invalid nmea altitude, fix time length : "+str(line)
                return
                
            self.fixtime = splittedDoublePoint[2]
        else:
            if len(splittedSpace) != 2:
                print "(nmeaNewAltitudeEvent) WARNING, invalid nmea altitude, space split : "+str(line)
                return
        
            try:
                self.altitude = float(splittedSpace[0])
            except ValueError as va:
                print "(nmeaNewAltitudeEvent) WARNING, invalid nmea altitude, float cast : "+str(line)+" "+str(va)
                return
            
            #units
            self.unit = splittedSpace[1]
        
            self.fixtime = None
        
        LogEvent.__init__(self,time,"nmeaNewAltitudeEvent",line)
        
    def addLine(self,line):
        print "(nmeaNewAltitudeEvent) WARNING, add line not allowed to nmeaSetTimeEvent : "+line
        
    def __str__(self):
        return "(nmeaNewAltitudeEvent) at "+str(self.time)+", altitude = "+str(self.altitude)+" "+str(self.unit)
        
        
