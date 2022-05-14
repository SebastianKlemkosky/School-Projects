from csv import reader
from pyspark.mllib.clustering import KMeans
from pyspark import SparkContext
import numpy as np
import re

# Initializing the Spark Context and getting the crime data for manipulation
sc = SparkContext(appName="MySparkProg")
sc.setLogLevel("ERROR")
data = sc.textFile("hdfs://10.56.3.221:54310/hw2-input/")


# Use csv reader to split each line of file into a list of elements.
# This will automatically split the csv data correctly.
splitData = data.mapPartitions(lambda x: reader(x))


# print splitdata.collect() 
masterList = splitData.collect()
crimeList = masterList[1:]
julyCrimeList = []


# RPT_DT is the data Month/Day/Year is the sixth element in each list
#
# We need to check every list for the fifth element and make sure it's July
for i in range(len(crimeList)):
  month = crimeList[i][5] 
  if month[:2] == '07':
    julyCrimeList.append(crimeList[i][7])


# Print julyCrimeList
#
# julyCrimeList is the list of lists of all crimes in the csv that occured in july.
#
# What are the top 3 crime types (use OFNS_DESC) that were reported in the month of July
# (use RPT_DT)? Crime types should be ranked based on the number of crimes reported in the
# month of July.
#
# How many crimes of type DANGEROUS WEAPONS were reported in the month
# of July?

# Create an RDD for julyCrimeList
#
# Then add up all the matching crimes and sort them in descending order
crimeRDD = sc.parallelize(julyCrimeList)
crimeCount = crimeRDD.map(lambda crime: (crime, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a: -a[1])


# Print out the top 3 Crimes by taking the first 3 elements of crimeCount
print "1.) What are the top 3 crime types that were reported in the month of July?"
for (crime, count) in crimeCount.take(3):
  print ("\t - %s %d" % (crime, count))


# Print out Crime Count for Dangerous Weapons by filtering crimeCount for 'Dangerous Weapon'
print "2.) How many crimes of type DANGEROUS WEAPONS were reported in the month of July?"
for (crime, count) in crimeCount.collect():
  if crime == 'DANGEROUS WEAPONS':
    print ("\t - %s %d" % (crime, count))