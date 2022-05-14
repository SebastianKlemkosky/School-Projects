from csv import reader
from pyspark.mllib.clustering import KMeans
from pyspark import SparkContext
import numpy as np
import re
sc = SparkContext(appName="MySparkProg")
sc.setLogLevel("ERROR")
data = sc.textFile("hdfs://10.56.3.221:54310/hw2-input/")

# use csv reader to split each line of file into a list of elements.
# this will automatically split the csv data correctly.
splitdata = data.mapPartitions(lambda x: reader(x))

#print splitdata.collect() 

masterlist = splitdata.collect()
headerlist = masterlist[0]
crimelist = masterlist[1:]
julycrimelist = []

#RPT_DT is the data Month/Day/Year is the sixth element in each list

#We need to check every list for the fifth element and make sure it's july

for i in range(len(crimelist)):
  month = crimelist[i][5] 
  if month[:2] == '07':
    julycrimelist.append(crimelist[i][7])

#print julycrimelist

#julylist is the list of lists of all crimes in the csv that occured in july.

#What are the top 3 crime types (use OFNS_DESC) that were reported in the month of July
#(use RPT_DT)? Crime types should be ranked based on the number of crimes reported in the
#month of July.

#How many crimes of type DANGEROUS WEAPONS were reported in the month
#of July ?

crimeRDD = sc.parallelize(julycrimelist)
crimeCount = crimeRDD.map(lambda crime: (crime, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a: -a[1])

#Print out the top 3 Crimes
print "What are the top 3 crime types that were reported in the month of July?"
for (crime, count) in crimeCount.take(3):
  print ("%s %d\n" % (crime, count))

#Print out Crime Count for Dangerous Weapons
print "How many crimes of type DANGEROUS WEAPONS were reported in the month of July?"
for (crime, count) in crimeCount.collect():
  if crime == 'DANGEROUS WEAPONS':
    print ("%s %d\n" % (crime, count))
    
    
    
    
    
    

