# 20.06.13 gcd
"""
"""
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a, b = map(int, input().split())
n = gcd(a, b)
a = ""
for i in range(n):
    a += "1"

print(a)
