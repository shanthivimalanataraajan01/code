a=input()
l=[int(x) for x in input().split()]
b=[]
for i in range(len(l)):
    c=l.count(l[i])
    b.append(c)
for i in range(len(a)):
    if a[i]==1:
        print(a[i])
