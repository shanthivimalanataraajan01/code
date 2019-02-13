n=input()
x=' '
for i in range(0,len(n)):
	if i %2==1:
		x=x+str(i)+' '
print(x.strip())
