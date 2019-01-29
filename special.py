n=input()
c=0
for i in range(0,len(n)):
	if n[i].isnumeric():
		pass
	elif n[i].isalpha():
		pass
	else:
		c=c+1
print(c)
