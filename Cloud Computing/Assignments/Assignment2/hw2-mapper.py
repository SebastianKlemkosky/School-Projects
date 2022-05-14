#!/usr/bin/env python2.7
from csv import reader
import sys

# skip first line (the header)
next(sys.stdin)

# Loop through the reader and only get the borough and crime values and
# print them to be used in hw2-reducer.py
for line in reader(sys.stdin):
 boro, crime = (line[13].strip(), line[7].strip())
 if not boro or not crime:
   continue
 print ("%s\t%s\t%s" % (boro, crime, 1))