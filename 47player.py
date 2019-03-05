# your code goes here
a,b,c=map(int,input().split())
d=0
if a!=0 and b!=0 and c!=0:
	if a+b+c==180:
		d=1
	
if d==1:
	print("yes")
else:
	print("no")
