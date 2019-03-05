#ms
n=int(input())
s=1
while n > 0:
    b=n%10
    s=s*b
    n=n//10
print(s)
