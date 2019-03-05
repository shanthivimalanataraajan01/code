# your code goes here
n=input()
m=""
for i in n:
	if i.islower() :
		m=m+i.upper()
	else:
		m=m+i.lower()
print(m)
