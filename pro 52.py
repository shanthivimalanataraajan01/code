# your code goes here
a,b=map(int,input().split())
c,d=map(int,input().split())
i,j=map(int,input().split())
m,s=map(int,input().split())
e=d-b
f=j-s
g=i-c
h=m-a
if e==f and g==h:
	print("yes")
else:
	print("no")
