def multiple(n):
    x=' '
    for i in range(1,6):
        s=i*n
        x=x+str(s)+' '
    print(x.strip())

n=int(input())
multiple(n)
