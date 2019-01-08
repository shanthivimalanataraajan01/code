#vimala
#hi
m,n=map(int,input().split())
x=' '
for n in range(m+1,n):
	if n>0:
		for i in range(2,n):
			if n%i==0:
				break
		else:
			x=x+str(n)+' '
print(x.strip())			
	
		
