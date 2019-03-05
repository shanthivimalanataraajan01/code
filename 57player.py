#ms
import collections
a,b = map(str,input().split())
c = dict(collections.Counter(a))
print(c[b])
