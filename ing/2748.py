#
"""
피보나치 수 2
"""
import sys
input = sys.stdin.readline

def fibonazzi(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return fibonazzi(n-1) + fibonazzi(n-2)

n = int(input())

print(fibonazzi(n))
