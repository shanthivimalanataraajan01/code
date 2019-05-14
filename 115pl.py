#ms
a,b=map(str,input().split())
c=len(a)
d=len(b)
e=""
if c>d:
	e=e+a[:d]+b
elif d>c:
	e=e+b[:c]+a
else:
	e=e+a+b
print(e)
