# 20.06.13
"""
"""
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    n = gcd(a, b)
    x = a/n
    y = b/n 
    return n*x*y

a, b = map(int, input().split())

print(gcd(a, b))
print(int(lcm(a, b)))

