#ms
a,b=input().split()
n=sorted(a)
k=sorted(b)
if len(a)==len(b):
  for i in range(len(a)):
    if a[i]!=a[i]:
      print("false")
      break
  else:
    print("true")
else:
  print("false")
