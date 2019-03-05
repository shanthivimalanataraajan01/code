# your code goes here
s=list(map(str,input().split()))
n=""
for i in s:
	n=n+i
c=0
for i in n:
	if n.count(i)==1:
		print(i,end=" "	)
