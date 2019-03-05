# your code goes here
s,t=map(str,input().split())
c=0
if len(s)==len(t):
	for i in range(len(s)):
		if s[i]!=t[i]:
			c=c+1
	if c==0:
		print("yes")
	else:
		print("no")
else:
	print("no")
