# 2020.07.14
"""
acmicpc.net/problem/3052
"""
import sys
input = sys.stdin.readline

s = set()
for i in range(10):
  num = int(input())
  s.add(num%42)
print(len(s))

