# your code goes here
s=input()
vowels={"a","e","i","o","u","A","E","I","O","U"}
if any(char in vowels for char in s):
	print("yes")
else:
	print("no")
