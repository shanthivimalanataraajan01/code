# your code goes here
s= int(input(""))
m = list(map(int,input().split()))
for i in range(s-1,-1,-1):
    if(i == 0):
        print(m[i],end="")
    else:
        print(m[i],end="->")
    

	
