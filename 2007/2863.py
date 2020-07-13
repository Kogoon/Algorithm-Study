# 2020.07.14
"""
acmicpc.net/problem/2863
"""
import sys 
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())
check = []

check.append(A/C + B/D)
check.append(C/D + A/B)
check.append(D/B + C/A)
check.append(B/A + D/C)

_max = check.index(max(check))
print(_max)
