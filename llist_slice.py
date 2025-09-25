from cmput274 import *
from llist import extract_list_item

myLl = cons(1, cons(2, cons(3, cons(4, cons(5, empty())))))

# problem 2
def list_slice(list, start, end):
    if start == end - 1:
        return cons(extract_list_item(list, start), empty())
    
    return cons(extract_list_item(list, start), list_slice(list, start + 1, end))

print(list_slice(myLl, 1, 5))
