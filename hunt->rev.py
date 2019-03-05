n=int(input())
a=[int(i) for i in input().split()]
b=a[::-1]
for i in range(0,len(b)):
	print(b[i],end="->")
