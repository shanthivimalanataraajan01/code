l,r=map(int,input().split(" "))
for i in range(1,100000):
    if i%l==0 and i%r==0:
        print(i)
        break
