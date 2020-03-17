# 2020.03.18
"""
acmicpc.net/problem/2523
입력: 첫째 줄에 N이 주어진다.
출력: 첫째 줄부터 2xN-1번째 줄까지 차례대로 별을 출력한다.
"""
#import sys
#input = sys.stdin.readline

N = int(input())

for i in range(1, 2*N+1):
    if i > N:
        for j in range(N-1, 0, -1):
            print("*" * j)
        break
    print("*" * i)

# i 가 0일때를 신경을 못썼다. 