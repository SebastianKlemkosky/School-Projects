import sys

def mmm(args):
  smallPos = 100000000
  largeNeg = -100000000
  for arg in args:
    n = int(arg)
    if(smallPos > n and n > 0):
      smallPos = n
    if(largeNeg < n and n < 0):
      largeNeg = n
  return (smallPos, largeNeg)

largeNeg, smallPos = mmm(sys.argv[1:])
print("Smallest positive=%d Largest negative=%d" % (smallPos, largeNeg))
