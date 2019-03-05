#ms
l,b,h=map(int,input().split())
m=[]
tsa=(2*l*b)+(2*b*h)+(2*l*h)
v=l*b*h
m.append(tsa)
m.append(v)
for i in range(0,len(m)):
	if i==(len(m)-1):
		print(m[i],end="")
	else:
		print(m[i],end=" ")
    
