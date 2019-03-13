# your code goes herems
import string,sys
def ispangram(s,alphabet=string.ascii_lowercase):
	a=set(alphabet)
	if a<=set(s.lower()):
		return ("yes")
	else:
		return ("no")
s=input()
print(ispangram(s))
