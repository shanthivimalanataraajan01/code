n=int(input())
t=n
s=0
while t>0:
	d=t%10
	s=s+d*d*d
	t=t//10
if n==s:
	print("yes")
else:
	print("no")
