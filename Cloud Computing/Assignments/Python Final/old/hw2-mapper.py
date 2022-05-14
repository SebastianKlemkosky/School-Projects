#!/usr/bin/env python2.7
from csv import reader
import sys

# skip first line (the header)
next(sys.stdin)

for line in reader(sys.stdin):
 boro, crime = (line[13].strip(), line[7].strip())
 if not boro or not crime:
   continue
 print ("%s\t%s\t%s" % (boro, crime, 1))
 #print ("%s\t%s" % (boro, 1))
 #Where is most of the crime happening in New York?
 #Boro is the location so count all occurences of it
 
 #What is the total number of crimes reported in that location ?
 #Print the max number of occurences
 
 #What types of crime are happening in that location (show unique crime types) ?
 #Print the unique crimes types

