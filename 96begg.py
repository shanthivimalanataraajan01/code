#ms
n,a,d=map(int,input().split())
l=[]
if d!=0:
	for i in range(a,n+1,d):
		l.append(i)
print(sum(l))
