a=input()
l=[int(c) for c in input().split()]
b=[]
for i in range(len(l)):
    c=l.count(l[i])
    b.append(c)
for i in range(len(b)):
    if b[i]==1:
        print(b[i])
