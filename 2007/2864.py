# 2020.07.14
"""
acmicpc.net/problem/2864
"""
import sys 
input = sys.stdin.readline

A, B = map(str, input().split())

min = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(min, max)
