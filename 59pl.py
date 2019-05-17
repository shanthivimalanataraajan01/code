n=int(input())
m=input()
a=""
b=""
for i in range(len(m)):
    if m[i]=='1':
        a=a+m[i]+' '
    else:
        b=b+a
        a=""
print(b.strip())
