#ms
b=int(input())
i=1
x=' '
while i<=b:
	if b%i==0:
		x=x+str(i)+' '
	i=i+1	
print(x.strip())	
