#ms
m,n=map(str,input().split())
c=0
if len(m)!=len(n):
	print('no')
else:
	for i in range(len(m)):
		if m[i]!=n[i]:
			c=c+1
if c==1:
    print('yes')
else:
    print('no')
		
