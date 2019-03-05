#ms
n=int(input())
d=0
a,b=map(int,input().split())
for i in range(a+1,b):
	if i==n:
		d+=1
		break
if d>0:
	print('yes')
else:
	print('no')
