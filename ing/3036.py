#
"""
"""
from fractions import Fraction
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

N = int(input())
circle = list(map(int, input().split()))
for i in range(1, N):
    print("{}/{}".format(int(circle[0]/circle[i]), circle[0]%circle[i]))