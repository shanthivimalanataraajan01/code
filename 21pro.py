#ms
a = int(input())
b = 0
l = list(map(int,input().split(" ")))
for i in range(a-1):
	first = (sum(l[0:(i+1)]))//(i+1)
	last = ((sum(l[(i+1):(a+1)])))//(a-(i+1))
	if(first == last):
		b = 1
if b==1:
	print("yes")
else:
	print("no")
