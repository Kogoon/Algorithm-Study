# 2020.07.14
"""
acmicpc.net/problem/1475
"""
import sys 
input = sys.stdin.readline

a, b, c, d, e = map(int, input().split())
sum = a**2 + b**2 + c**2 + d**2 + e**2
print(sum%10)
