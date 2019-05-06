# your code goes here
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse = True)
print(l[m-1])
