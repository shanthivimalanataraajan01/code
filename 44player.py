# your code goes here
a,b=map(str,input().split())
c=int(b)
d=len(a)
s=a
for i in range(c):
	s=s[-1]+s[:d-1]
print(s)
