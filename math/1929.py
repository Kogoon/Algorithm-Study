#
# 수학
"""
acmicpc.net/problem/1929
문제: M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
입력: 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.(1<=M<=N<=1,000,000)
출력: 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""
# 소수 구하기
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
sosu = []

for i in range(2, int(N)):
    if N % i != 0 :
        sosu.append(i)

for i in range(M, N):
    if i in sosu:
        print(i)



