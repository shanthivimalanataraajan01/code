#ms
m,n=map(str,input().split())
c=0
if len(n)<=len(m):
    for i in n:
        if i in m:
            c=c+1
    if c==len(n):
        print("yes")
    else:
        print("no")

else:
    print("no")
