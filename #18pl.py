n=int(input())
m="kabali"
m=list(m)
d=0
for i in range(n):
    b=input()
    if len(m)==len(b):
        b=list(b)
        c=0
        for i in range(len(m)):
            if m[i] in b:
                c=c+1
        if c==len(m):
            d=d+1
print(d)
