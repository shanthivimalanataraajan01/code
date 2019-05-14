#ms
import sys, string, math
a = int(input())
b = a
l = []
for i in range( 2,b) :
    if a%i == 0: 
      l.append(i)
    while a%i == 0 : 
      a //= i
if len(l) == 0 : 
  print(b)
else :          
   print(*l)
