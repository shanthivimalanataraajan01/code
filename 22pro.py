a=int(input())
l=list(map(int,input().split()))
m=0
n=0
for i in range(0,a):
	if i%2==0:
		m=m+l[i]
	else:
	  n=n+l[i]
if m>n:
	print(m)
else:
	print(n)
