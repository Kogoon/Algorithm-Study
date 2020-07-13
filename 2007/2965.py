# 2020.07.14
"""
acmicpc.net/problem/2965
"""
import sys 
input = sys.stdin.readline

a, b, c = map(int, input().split())

check = []
check.append(c-b)
check.append(b-a)
_max = max(check)
print(_max - 1)
