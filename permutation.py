# your code goes here
def permutation(li):
	if l(li)==0:
		return []
	if l(li)==1:
		return[li]
	k=[]
	for i in range(l(li)):
		a=li[i]
		rem=li[:i]+li[i+1:]
		for m in permutation(rem):
			b.append([a]+m)
	return b
		
n=list(input())
for i in permutation(n):
	for c in i:
		print(c,end="")
	print()

      
