# your code goes herems
n=input()
a=""
b=[]
for i in range(len(n)):
	if n[i] not in a:
		a=a+n[i]
	elif n[i]  in a:
		b.append(len(a))
		a=""
	if i==len(n)-1:
		b.append(len(a))
		a=""
print(max(b))
