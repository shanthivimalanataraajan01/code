#ms
m,n = map(int,input().split())
l = list(map(int,input().split()))
if(m<n):
    for i in range(a):
        if(i == a-1):
            print(l[i],end="")
        else:
            print(l[i],end=" ")
else:
    b= a-n
    for i in range(b,a):
        print(l[i],end = " ")
    for i in range(0,b):
        if(i==b-1):
            print(l[i],end="")
        else:
            print(l[i],end = " ")
