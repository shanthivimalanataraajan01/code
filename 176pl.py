a,b=map(str,input().split())
c=[]
d=[]
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in d:
        d.append(i)
e=0
for i in c:
    if c.count(i)==d.count(i):
        e+=1
if e==len(c) and c==len(d):
    print("true")
else:
    print("false")
