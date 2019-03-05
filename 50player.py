# your code goes here
n=int(input())
a=0
for i in range(2,n):
	if n%i==0:
		a=1
	else:
		continue
if a==1:
	print("yes")
else:
	print("no")
