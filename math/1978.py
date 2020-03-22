#
# 수학
"""
acmicpc.net/problem/1978
"""
# 소수 찾기

import sys
input = sys.stdin.readline

n = int(input())
check = [True for i in range(1000)]
numbers = list(map(int, input().split()))
print(numbers)