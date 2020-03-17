# 2020.03.17
"""
acmicpc.net/problem/10818
문제: N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
입력: 첫째 줄에 정수의 개수 N이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
    모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
출력: 첫째 줄에 주어진 정수는 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다. 
"""
import sys

N = int(input()) #정수의 개수
numbers = list(map(int, input().split()))
#if numbers > N:
#    sys.exit()
numbers.sort()
min_num = numbers[0]
max_num = numbers[N-1]
print(min_num, max_num)