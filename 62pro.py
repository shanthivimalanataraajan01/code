def find(a,b,c):
  l=0
  m=0
  if a[b:c]==a[b:c][::-1]:
    m=len(a[b:c])
    b-=1
    c+=1
    while b>=0 and c<=len(s) and a[b:c]==a[b:c][::-1]:
      m+=2
      b-=1
      c+=1
    if m>l:
      l=m
  return l

s=input()
r=0
t=0
if s==s[::-1]:
  r=len(s)
else:
  for i in range(2,4):
    j=0
    while j+i<=len(s):
      t=find(s,j,i+j)
      j+=1
      if r<t:
        r=t
print(len(s)-r)
