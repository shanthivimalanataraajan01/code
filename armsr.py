a,b=map(int,input().split())
x=' '
for n in range(a+1,b):
	s=0
	t=n
	while t>0:
		d=t%10
		s=s+d*d*d
		t=t//10
	if s==n:
		x=x+str(n)+' '
print(x.strip())		
		
