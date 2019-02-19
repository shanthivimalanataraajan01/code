#ms
b=int(input())
i=1
s=0
while i<=b:
	if b%i==0:
		s=s+1
	i=i+1
if s!=2:
	print("yes")
else:
	print("no")
