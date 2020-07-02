# 2020.07.02
"""
"""
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

N = int(input())
circle = list(map(int, input().split()))

for i in range(1, N):
    G = gcd(circle[0], circle[i])
    a = int(circle[0]/G)
    b = int(circle[i]/G)
    print("{}/{}".format(a, b))