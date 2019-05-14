a,b=input().split()
for i in range(0,len(a)-1):
  if a[i:i+2] in b:
    print('yes')
    break
else:
  print('no')
