# your code goes here
from collections import OrderedDict
a=input()
b="".join(OrderedDict.fromkeys(a))
print(b)
