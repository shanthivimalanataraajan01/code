a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=c[::-1]
if d==b:
  print("yes")
else:
  print("no")
