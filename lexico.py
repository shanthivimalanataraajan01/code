#ms
s=input()
l=[]
for i in s:
	l.append(i)
l.sort()
for i in range(len(l)):
	print(l[i],end='')
