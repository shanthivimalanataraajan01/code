w=int(input())
e=[int(i) for i in input().split()]
s=sorted(e)
for i in range(0,len(e)):
	if(i == (len(e)-1)):
		print(s[i],end="")
	else:
		print(s[i],end=" ")
