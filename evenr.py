m,n=map(int,input().split())
x=' '
for i in range(m+1,n):
	if i%2==0:
		x=x+str(i)+' '
print(x.strip())
