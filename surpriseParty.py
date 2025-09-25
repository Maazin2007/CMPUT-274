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

def timeToMins(s):
    """
    timeToMins returns the minutes since midnight repersented 
    by the given time string.
    
    s       - a string of the form "HH:MM" hwere HH is 00-23 
              and MM is 00-59
    returns - an integer, the minutes since midnight
    
    Examples:
     timeToMin("03:45") -> 205
     timeToMin("14:53") -> 897
    """
    
    return timeUnitToNum(s[0:2])*60 + timeUnitToNum(s[3:5])

def timeToEnter(lot, dur):
    """
    timeToEnter finds a time that it is possible to enter a house and throw a suprise
    party without ruining the suprise
    
    lot     - List of strings of the form "HH:MM", and the elements of the list are (e1,r2,e1,r2,..,en, rn)
              where ei is the ith time that the person leaves the house and ri is the ith time that they returned
              to the house
    dur     - is an integer, repersents the number of minutes needed to throw a suprise party
    returns - the first time string that begins a long enough duration, or False
    
    Examples:
        times = cons("03:20", cons("07:45", cons("11:30", cons("18:10", empty()))))
        timesToEnter(times, 180) -> "3:20"
        timesToEnter(times, 300) -> "11:30"
        timesToEnter(times, 500) -> False
    """
    if isEmpty(lot):
        return False
    
    exitTime = first(lot)
    returnTime = first(rest(lot))
    timeGone = timeToMins(returnTime) - timeToMins(exitTime)
    
    if timeGone < dur:
        return timeToEnter(rest(rest(lot)), dur)
    


    
    
    

    