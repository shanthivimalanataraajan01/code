#ms
n,k = map(int,input().split())
c = list(map(int,input().split()))
amount = int(input())
total = (sum(c)-c[k])//2
if amount == total:
  print("Bon Appetit")
else:
  print(amount-total)
