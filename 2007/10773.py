# 2020.07.04
"""
"""
import sys
input = sys.stdin.readline

K = int(input())
stk = []

for i in range(K):
    num = int(input())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)
sum = 0
for j in range(len(stk)):
    sum += stk[j]

print(sum)