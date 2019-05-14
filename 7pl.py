# your code goes here
a=str(input())
b=[]
l=len(a)
i=0
while(i<l-1):
    b.append(a[i+1])
    b.append(a[i])
    i=i+2
if(l%2==0):
    print("".join(b))
else:
    a.append(a[l-1])
    print("".join(b))
    
