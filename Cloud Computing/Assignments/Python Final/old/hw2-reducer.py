#!/usr/bin/env python2.7
import sys
import numpy as np



current_boro = None
current_count = 0
boro = None
crime = None
current_crime = None
most_crime_boro = None
most_crime = 0

BRONX =[] 
BROOKLYN = []
MANHATTAN = []
QUEENS = []
STATEN_ISLAND = []   



# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    boro, crime, count = line.split('\t', 2)
    
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_boro == boro:
        current_count += count
                  
        if boro == 'BRONX':
          BRONX.append(crime)
        if boro == 'BROOKLYN':
          BROOKLYN.append(crime)
        if boro == 'MANHATTAN':
          MANHATTAN.append(crime)
        if boro == 'QUEENS':
          QUEENS.append(crime)
        if boro == 'STATEN ISLAND':
          STATEN_ISLAND.append(crime)             
    else:
        if current_boro:
            # write result to STDOUT
            #print ("%s\t%s" % (current_boro, current_count))
                        
            if most_crime < current_count:
              most_crime = current_count
              most_crime_boro = current_boro
              
        current_count = count
        current_boro = boro

# do not forget to output the last word if needed!
if current_boro == boro:
    #print ("%s\t%s" % (current_boro, current_count))
    
    if boro == 'BRONX':
      BRONX.append(crime)
    if boro == 'BROOKLYN':
      BROOKLYN.append(crime)
    if boro == 'MANHATTAN':
      MANHATTAN.append(crime)
    if boro == 'QUEENS':
      QUEENS.append(crime)
    if boro == 'STATEN ISLAND':
      STATEN_ISLAND.append(crime)  
    
    if most_crime < current_count:
      most_crime = current_count
      most_crime_boro = current_boro

 #Where is most of the crime happening in New York?
 #Boro is the location so count all occurences of it
 
 #What is the total number of crimes reported in that location ?
 #Print the max number of occurences
 
 #What types of crime are happening in that location (show unique crime types) ?
 #Print the unique crimes types


print("Where is most of the crime happening in New York?")
print("The most crime is happening in %s\n" % (most_crime_boro))

print("What is the total number of crimes reported in that location ?")
print("The crime count is %s\n" % (most_crime))


if most_crime_boro == 'BRONX':
  unique = np.unique(BRONX)
if most_crime_boro == 'BROOKLYN':
  unique = np.unique(BROOKLYN)
if most_crime_boro == 'MANHATTAN':
  unique = np.unique(MANHATTAN)
if most_crime_boro == 'QUEENS':
  unique = np.unique(QUEENS)
if most_crime_boro == 'STATEN ISLAND':
  unique = np.unique(STATEN_ISLAND)



print("What types of crime are happening in that location (show unique crime types) ?")
print("Types of unique crimes")
for i in range(len(unique)):
  print(unique[i])







