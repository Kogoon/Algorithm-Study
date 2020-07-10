# 2020.04.29
"""
acmicpc.net/problem/10996
문제: 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
입력: 첫째 줄에 (1 <= N <= 100)이 주어진다.
출력: 첫째 줄부터 차례대로 별을 출력한다. 
"""
import sys 
input = sys.stdin.readline

N = int(input())

row = N * 2
col = N

if N == 1:
    print("*")

else:
    for i in range(N):
        pass