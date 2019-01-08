n=int(input())
r=0
t=n
while n>0:
	d=n%10
	r=r*10+d
	n=n//10
if r==t:
	print("yes")
else:
	print("no")
