# 2020.07.19 
"""
acmicpc.net/problem/1920
"""
import sys
input = sys.stdin.readline

N = int(input())
n = set(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

for i in m:
  if i in n:
    print(1)
  else:
    print(0)

"""
문제 자체는 어렵지 않은데 n 입력받는 과정에서 list로 입력받아서 시간초과가 뜸. 
list -> O(n), set을 사용하면, 중복값 제거 및 오름차순으로 정렬 set -> O(1)
"""
