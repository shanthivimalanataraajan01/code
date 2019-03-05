#ms
n=int(input())
sum=0
while n>0:
	m=n%10
	s=m**2
	sum=sum+s
	n=n//10
print(sum)
