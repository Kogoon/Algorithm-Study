# 2020.02.02
"""
acmicpc.net/problem/1697
문제:
입력: 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
출력: 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
#수빈 위치 N 동생 K
time_sec = 0
if N < K:
    N -= 1
    time_sec += 1

while True:
    if K == N:
        print(time_sec)
        sys.exit()
    elif K < N:
        N -= 1
        time_sec += 1
    elif K == (N+1):
        N += 1
        time_sec += 1
    else:
        N = N * 2
        time_sec += 1
