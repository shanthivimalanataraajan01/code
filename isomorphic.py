f,t=map(str,input().split())
p=[]
k=[]
c=0
if len(f)==len(t):
    for i in f:
        a=f.count(i)
        p.append(a)
    for j in t:
        b=t.count(j)
        k.append(b)
    for m in range(0,len(p)):
        for n in range(0,len(k)):
            if m==n:
                if p[m]==k[n]:
                    c=c+1
    if c==len(p):
        print("yes")
    else:
        print("no")
else:
    print("no")

