# your code goes here
s=input()
a=len(s)
m=0
n=0
l=[]
for i in s:
	l.append(i)
if a%2!=0:
	m=a//2
	l[m]="*"
	print("".join(l))
else:
	m=a//2
	n=m-1
	l[m]="*"
	l[n]="*"
	print("".join(l))
