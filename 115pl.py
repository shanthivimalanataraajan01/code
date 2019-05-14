#ms
a,b=input().split()
s=''
if len(a)!=len(b):
  d=min(len(a),len(b))
  s=a[:d]+b[:d]
else:
  s=a+b
print(s)
