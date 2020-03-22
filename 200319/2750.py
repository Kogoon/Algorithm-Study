# 2020.03.19
"""
acmicpc.net/problem/2750
문제: N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
입력: 첫째 줄에 수의 개수 N이 주어진다. 둘째 줄부터는 N개의 줄에는 숫자가 주어진다.
    이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
출력: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers.sort()

for i in numbers:
    print(i)