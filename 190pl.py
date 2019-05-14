m=map(int,input().split())
m=sorted(m)
a= m[0]*m[0]
b= m[1]*m[1]
c= m[2]*m[2]
if a+b==c:
  print("yes")
else:
  print("no")  
