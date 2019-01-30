# your code goes here
a,n=map(int,input().split())
c=[int(i) for i in input().split()]
for r in range(0,len(c)):
	if c[r]==n:
		print("yes")
		break
else:
	print("no")
