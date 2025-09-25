def digitSum(n):
    if n < 10:
        return n
    
    digit = n // (10**logFloor(n))
    
    return digit + digitSum(n // (10**logFloor(n)))

def logFloor(n):
     if n < 10:
         return 0
      
     return 1 + logFloor(n/10)
 