n = input()
a = map(int,raw_input().split())
a.sort()
s = [55]
for i in range(0,n-1):
    if a[i] == a[i+1]:
        p = s.pop()
        if a[i] == p:
          s.append(p)
        else:
          s.append(p)
          s.append(arr[i])
s.pop(0)
if s == []:
    print 'unique'
else:
    print (' '.join(map(str,s)))
