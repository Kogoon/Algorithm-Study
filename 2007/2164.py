# 2020.07.09
"""
import sys
input = sys.stdin.readline

N = int(input())

num_list = [] 
for i in range(1, N+1):
  num_list.append(i)

while True:
  if len(num_list) == 1:
    print(num_list[0])
    break
  num_list.pop(0)
  temp = num_list[0]
  num_list.pop(0)
  num_list.append(temp)
# 시간초과
"""
#덱으로 구현 
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

num_list = deque() 
for i in range(1, N+1):
  num_list.append(i)

while True:
  if len(num_list) == 1:
    print(num_list[0])
    break
  num_list.popleft()
  temp = num_list.popleft()
  num_list.append(temp)