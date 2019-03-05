#ms
a,b = map(int,input().split())
n=b
i=0
while n<=a:
	if n==a:
		print("yes")
		break
	num=b**i
	i=i+1
else:
	print("no")
