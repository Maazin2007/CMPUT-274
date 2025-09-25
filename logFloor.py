from math import floor

def logFloor(n):
     if n < 10:
         return 0
      
     return 1 + logFloor(n/10)