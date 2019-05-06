#your code goes herea
a=list(map(str,input().split()))
for i in range(len(a)):
	a[i]=a[i][::-1]
for i in range(len(a)):
	if i==len(a)-1:
		print(a[i],end="")
	else:
		print(a[i],end=" ")
