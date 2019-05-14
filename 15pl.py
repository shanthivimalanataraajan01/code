a=str(input())
b=[]
for i in range (0,len(a)):
    b.append(a.count(a[i]))
c=b.index(max(b))
print(a[c])
