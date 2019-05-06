# your code goes here
n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
a=set([i for i in l if l.count(i)==1 ])
for i in a:
	l1.append(i)
	c=1
l1.sort
if c==1:
	for i in range(len(l1)):
		if i==len(l1)-1:
			print(l1[i],end='')
		else:
			print(l1[i],end=' ')
else:
	print('unique')
