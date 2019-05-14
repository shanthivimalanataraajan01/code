n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(0,len(a)):
	for j in range(0,len(a)):
		for k in range(0,len(a)):
			if i<=j<=k:
				c=p*a[i]+q*a[j]+r*a[k]
				b.append(c)
print(max(b))
© 2019 GitHub, Inc.
