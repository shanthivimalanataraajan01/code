#ms
m=input("")
n=""
for i in range(len(m)):
	if i==0:
		n+=m[i].upper()
	elif (m[i-1].isspace()):
		n+=m[i].upper()
	else:
		n+=m[i].lower()
print(n)
	
