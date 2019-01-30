# your code goes here
a,n=map(int,input().split())
c=[int(i) for i in input().split()]
t=0
for r in range(0,len(c)):
	if c[r]==n:
		t=t+1
print(t)		
