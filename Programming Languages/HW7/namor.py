#! /usr/bin/python

import sys
import re

def namor(strNum):
    
  strR = strNum  
  
  #print(strR)
  
  #Check for some invalid numeral combos
  if(re.search("IIII", strR) or re.search("XXXX", strR) or re.search("CCCC", strR)):
    return -1
  
  
  
     
  #result number  
  result = 0
  
  x = 0
  
  while (x < len(strNum)):
     #Convert current Numeral letter
     str1 = convert(strNum[x])
     #Check if current isn't the last letter
     if (x + 1 < len(strNum)):
       #Convert next letter
       str2 = convert(strNum[x + 1])
       #check if current is greater than next (Cases like IV or VI)
       if (str1 >= str2):
         result = result + str1
         x = x + 1
       else:
         result = result + str2 - str1
         x = x + 2
     else:
       result = result + str1
       x = x + 1
 
  #if result is < 1 return -1
  if(result < 1):
    return -1
  #if result > 3999 return -1
  if(result > 3999):
    return -1
    
  return result 
    
#function/method to convert from numeral to integer using a dictionary
def convert(c):

  ones = {'IX': 9, 'VIII': 8, 'VII':7, 'VI':6, 'V':5, 'IV':4, 'III':3, 'II':2, 'I':1}
  tens = {'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60, 'L': 50, 'XL': 40, 'XXX': 30, 'XX': 20, 'X': 10}
  hundreds = {'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600, 'D': 500, 'CD': 400, 'CCC': 300, 'CC': 200, 'C': 100}
  thousands = { 'MMM': 3000, 'MM': 2000, 'M': 1000}
  
  #Main Dictionary
  numbers = { 'MMM': 3000, 'MM': 2000, 'M': 1000, 'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600, 'D': 500, 'CD': 400, 'CCCC': -1, 'CCC': 300, 'CC': 200, 'C': 100, 'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60, 'L': 50, 'XL': 40, 'XXXX': -1, 'XXX': 30, 'XX': 20, 'X': 10, 'IX': 9, 'VIII': 8, 'VII':7, 'VI':6, 'V':5, 'IV':4, 'III':3, 'II':2, 'I':1 }
  
  
    
  
  
  
  #If it is in the dictionary return the value
  if(c in numbers):
    return numbers[c]
  
  
  
  
  
  #return -1
  return -1



if __name__ == '__main__':
    # Map command line arguments to function arguments.
    #Take arguments as a list
    lis = sys.argv[1:]
    #result string
    res = ""
    #If nothing in list
    if(len(lis) == 0):
      res = "Please enter a value"
    #if only 1 argument in list
    if(len(lis) == 1):
      res =  str(lis[0]) + " is " + str(namor(lis[0]))
      
    #if more than 1 argument in list
    if(len(lis) > 1): 
      for i in range(len(lis)):
        if(i == 0):
          res =  str(lis[0]) + " is " + str(namor(lis[0]))
        if(i > 0):
          res += " and " + str(lis[i]) + " is " + str(namor(lis[i]))
          
    #print the result
    print(res)
    