# 2020.06.30
"""
피보나치 수 2
"""
import sys
input = sys.stdin.readline

N = int(input())
fibo = []
for i in range(N+1):
  if i <= 1:
    fibo.append(i)
  else:
    temp = fibo[i-1] + fibo[i-2]
    fibo.append(temp)

print(fibo[N])