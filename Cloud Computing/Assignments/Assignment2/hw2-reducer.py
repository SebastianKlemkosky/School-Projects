#!/usr/bin/env python2.7
import sys
import numpy as np

# Vars to track crime count and for traversing information
current_boro = None
boro = None
crime = None
current_crime = None
most_crime_boro = None
current_count = 0
most_crime = 0

# Create a dictionary with the boroughs as keys to store the
# type of crimes found
boroughs = {}

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

        # Add the crime to the list under its appropriate borough, if the borough doesn't
        # aready exist in the dictionary, create it and add the crime
        if not boroughs.has_key(boro):
          boroughs[boro] = []
          boroughs[boro].append(str(crime))
        else:
          boroughs[boro].append(str(crime))
    else:
        if current_boro:       
            if most_crime < current_count:
              most_crime = current_count
              most_crime_boro = current_boro
              
        current_count = count
        current_boro = boro

# do not forget to output the last word if needed!
if current_boro == boro:
  '''
    if current_boro == "STATEN ISLAND":
      boroughs["STATEN_ISLAND"].append(str(crime))
    else:
  '''
  boroughs[boro].append(str(crime))

  if most_crime < current_count:
    most_crime = current_count
    most_crime_boro = current_boro

# Get all the unique crimes for the borough and
# add it to a list to be used later
unique = np.unique(boroughs[most_crime_boro])

# Print out the questions and responses of the borough with most crime and the information
print("Where is most of the crime happening in New York?")
print("   - The most crime is happening in %s\n" % (most_crime_boro))

print("What is the total number of crimes reported in that location ?")
print("   - The crime count is %s\n" % (most_crime))

print("What types of crime are happening in that location (show unique crime types) ?")
print("   - Types of unique crimes")
# Loop through the list of unique crimes and print them out for response
for i in range(len(unique)):
  print("\t%s" % unique[i])