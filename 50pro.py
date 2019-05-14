a,b=map(int,input().split())
c=[]
for i in range(a):
  c.append(list(map(int,input().split())))
cost=10000000
e=0
for i in range(a):
  if c[i][0]==1:
    s=c[i][1]
    d=c[i][2]
    for j in range(i+1,a):
      if c[j][0]==s:
        s=c[j][1]
        d+=c[j][2]
    if d<cost and s==b:
      cost=d
      e+=1
if e==0:
  print(-1)
else:
  print(cost)
