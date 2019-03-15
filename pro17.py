# your code goes herems
n,k=map(int,input().split())
l=list(map(int,input().split()))
f=0
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==k:
			f=1
			break
if f==1:
	print('yes')
else:
	print('no')
