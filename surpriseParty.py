from digitToNumber import *

def timeUnitToNum(s):
    """
    timeUnitToNum takes a two digit string and return the integer it repersents!
    
    s       - a two digit string
    returns - integer
    
    Examples:
        timeUnitToNum("05") -> 5
        timeUnitToNum("47") -> 45
    """
    
    tensdigit = digitToNumber(s[0])
    onesdigit = digitToNumber(s[1])
    
    return tensdigit*10 + onesdigit

print(timeUnitToNum('46'))
    