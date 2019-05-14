#ms
a,b=map(str,input().split())
c=len(a)
d=len(b)
e=""
if c>d:
	e=e+s[:d]+b
elif d>c:
	e=e+b[:c]+s
else:
	e=e+s+b
print(e)
