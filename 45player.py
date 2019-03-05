# your code goes here
a,b=map(int,input().split())
t=a//2
for i in range(t,0,-1):
	for j in range(1,t):
		if i+j==t and i*j==a:
			print("yes")
			exit(0)
else:
	print("no")
