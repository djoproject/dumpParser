#!/usr/bin/python

import os
from logstruct import NmeaLog, DumpLog, parseNmeaFile, parseDumpLogFile
from dumpStruct import FileDump

#nmeaLogDirectory = "/Volumes/Home/Downloads/root/nmea/log/"
nmeaLogDirectory = "/home/djo/developement/raw/nmea/log/"
nmeaLog = []
#dumpLogDirectory = "/Volumes/Home/Downloads/root/dumper/log/"
dumpLogDirectory = "/home/djo/developement/raw/dumper/log/"
dumpLog = []
#dumpDirectory    = "/Volumes/Home/Downloads/root/dumper/dump/"
dumpDirectory    = "/home/djo/developement/raw/dumper/dump/"
dump = []

#load nmea logs
print "parsing nmea log..."
for f in os.listdir(nmeaLogDirectory):
    if os.path.isfile(nmeaLogDirectory+f) and f.endswith(".log"):
        nmeaLog.extend(parseNmeaFile(nmeaLogDirectory+f))
    else:
        print "warning, not a valid file : "+nmeaLogDirectory+f

#update all the New position 
for log in nmeaLog:
    log.updateAllEventTime()

print "DONE !"

print "parsing dump log..."
#load dump logs
for f in os.listdir(dumpLogDirectory):
    if os.path.isfile(dumpLogDirectory+f) and f.endswith(".log"):
        dumpLog.extend(parseDumpLogFile(dumpLogDirectory+f))
    else:
        print "warning, not a valid file : "+dumpLogDirectory+f
print "DONE !"

print "parsing dump..."
#load dump files 
for f in os.listdir(dumpDirectory):
    if os.path.isfile(dumpDirectory+f) and f.endswith(".txt"):
        dump.append(FileDump(dumpDirectory+f))
    else:
        print "warning, not a valid file : "+dumpDirectory+f
print "DONE !"
    
#correlate all structures
#TODO
