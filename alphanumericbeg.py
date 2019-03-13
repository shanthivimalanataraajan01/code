#ms
string = input()
a=0
for i in string:
	if(i.isnumeric()):
		a = a + 1
	print(a,end='')
