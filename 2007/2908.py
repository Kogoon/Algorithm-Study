# 2020.07.14
"""
acmicpc.net/problem/2908
"""
import sys 
input = sys.stdin.readline

a, b = map(str, input().split())
check = []
check.append(int(a[::-1]))
check.append(int(b[::-1]))
print(max(check))
