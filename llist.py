from cmput274 import *

def create_List(n):
    if n == 1:
        return cons(1, empty())
    
    return cons(n, create_List(n - 1))

myList = create_List(10)

def extract_list_item(list, i): return first(list) if i == 0 else extract_list_item(rest(list), i - 1)

print(myList)
print(extract_list_item(myList, 2))