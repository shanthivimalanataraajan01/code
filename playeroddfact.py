#ms
def isodd(n):
      if n%2!=0:
            return 1
      else:
           return 0
a=[]
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        if isodd(i)==1:
            a.append(i)
for i in range(len(a)):
    if i==0:
        print(a[i],end="")
    else:
        print("",a[i],end="")
