# your code goes herems
k=int(input())
l=[]
for i in range(k):
	m=list(map(int,input().split()))
	l.extend(m)
l.sort()
print(*l)
