import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = 0

d = [x for x in a]

for i in range(n):
  d[i] = a[i]
  for j in range(i):
    if a[i] > a[j] and d[i] < d[j] + a[i]:
      d[i] = d[j] + a[i]

  if d[i] > result:
    result = d[i]

print(result)
