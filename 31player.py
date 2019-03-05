# your code goes here
n=input()
a=0
b=0
for i in n:
	if i=="(":
		a=a+1
	elif i==")":
		b=b+1
if a==b:
	print('yes')
else:
	print('no')
