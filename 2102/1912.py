# 21.02.25

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0] * n
result = a[0] 

for i in range(n):
  d[i] = max(d[i-1] + a[i], a[i])
  result = max(d[i], result)

print(result)
