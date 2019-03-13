# your code goes herems
k=int(input())
l1=[]
for i in range(k):
	l=list(map(int,input().split()))
	l1.extend(l)
l1.sort()
print(*l1)
