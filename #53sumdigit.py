n=int(input())
s=0
t=n
while n>0:
	t=n%10
	s=s+t
	n=n//10
print(s)	
