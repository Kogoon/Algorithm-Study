# 20.06.13
"""
"""
import math
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

N_f = math.factorial(N)
K_f = math.factorial(K)
NK_f = math.factorial(N-K)

print(int(N_f / (K_f * NK_f)))
