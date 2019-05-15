
#ms
l=list(input().split())
l1=[]
for i in l:
  l1.append(sorted(list(i)))
l2=[]
for i in l1:
  l2.append("".join(i))
print(*l2)
