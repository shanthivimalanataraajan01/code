n=input()
l=[]
for i in range(len(n)):
    a=n.count(n[i])
    l.append(a)
a=max(l)
b=l.index(a)
print(a[b])
