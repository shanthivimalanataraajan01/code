#ms
n=int(input())
a=list(map(int,input().split(" ")))
for i in range(a,n):
	if sum(a[:i])//len(a[:i])==sum(a[i:])//len(a[i:]):
		print("yes")
		break
else:
	print("no")
