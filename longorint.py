# your code goes here
n=input()
m=int(n.replace("," , ""))
if m>= -2147483648 and m<= 2147483647:
    print("INT")
elif m>=9223372036854775808 and m<= 9223372036854775807:
    print("LONG LONG")
else:
    print("LONG")
