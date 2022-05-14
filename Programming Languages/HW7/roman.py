#! /usr/bin/python

import sys

#Given a string number return it's roman numeral form
def roman(strNum):
    #String to be returned
    result = ""
    
    #Check if the string is a number
    if(strNum.isdigit() == False):
      return "Error"
    
    #convert string to int
    num = int(strNum)
    
    #Check if too small or too big a number
    if(num <= 0):
      return "ERROR"
    if(num > 3999):
      return "ERROR" 
    
    #Integers in greatest to least
    integers = (3000, 2000, 1000, 900, 800, 700 , 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    
    #Numerals in greatest to least
    numerals = ('MMM', 'MM', 'M', 'CM', 'DCCC', 'DCC','DC','D','CD', 'CCC', 'CC', 'C', 'XC', 'LXXX', 'LXX', 'LX' , 'L' , 'XL', 'XXX', 'XX', 'X', 'IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I')
    
    #Iterator through the integer list picking up numerals if possible
    for x in range(len(integers)):
        cnt = int(num / integers[x])
        result += numerals[x] * cnt
        
        num -= integers[x] * cnt
     
    # return result 
    return result   
    

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
      res =  str(lis[0]) + " is " + str(roman(lis[0]))
      
    #if more than 1 argument in list
    if(len(lis) > 1): 
      for i in range(len(lis)):
        if(i == 0):
          res =  str(lis[0]) + " is " + str(roman(lis[0]))
        if(i > 0):
          res += " and " + str(lis[i]) + " is " + str(roman(lis[i]))
    #print the result
    print(res)
    
    