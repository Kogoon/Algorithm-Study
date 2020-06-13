# 20.06.13
"""
"""
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
ans = 1
a.sort()
if N == 1:
    ans = a[0]**2
else:
    ans = a[1] * a[-2]
print(ans)