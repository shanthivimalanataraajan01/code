# your code goes here
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort()
print(a[k-1])
