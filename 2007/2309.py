# 2020.07.02
"""
"""
import sys
input = sys.stdin.readline

N = 9
nan = [0 for _ in range(9)]
sum = 0

for i in range(N):
    nan[i] = int(input().rstrip())
    sum += nan[i]

nan.sort()
#print(nan)
for i in range(N):
    for j in range(1, N):
        if (sum - nan[i] - nan[j]) == 100:
            for k in range(N):
                if i != k and j != k:
                    print(nan[k])
            sys.exit()