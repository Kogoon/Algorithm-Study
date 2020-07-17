# 2020.07.18
"""
acmicpc.net/problem/18258
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque([])
for _ in range(N):
  command = input().split()
  if command[0] == 'push':
    queue.append(command[1])
  elif command[0] == 'pop':
    if not queue:
      print("-1")
    else:
      temp = queue.popleft()
      print(temp)
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    if not queue:
      print("1")
    else:
      print("0")
  elif command[0] == 'front':
    if not queue:
      print("-1")
    else:
      print(queue[0])
  elif command[0] == 'back':
    if not queue:
      print("-1")
    else:
      print(queue[len(queue)-1])
