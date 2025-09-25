from cmput274 import *

def digitToNumber(c):
    """
    digitToNumber returns the iteger value that repersents the single digit
    character provided
    
    c       - is a single character string, containing only a digit character
    returns - an integer in the range [0, 9]
    
    Examples:
        digitToNumber(9) -> 57
        digitToNumber(4) -> 52
        digitToNumber(0) -> 48
    """
    return ord(c) - 48