from cmput274 import *

def descendList(n):
    if n == 0:
        return cons(0, empty())
    
    return cons(n, descendList(n - 1))

print(descendList(4))
