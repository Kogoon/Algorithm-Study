#
"""
"""
import sys
input = sys.stdin.readline

N, M, root = map(int, input().split())
check = [0] * (N+1)
maps = [[0] * (N+1) for i in range(N+1)]
for m in range(M):
  a, b = map(int, input().split())
  maps[a][b] = 1
  maps[b][a] = 1

def dfs():
  pass

def bfs():
  pass

print(dfs(*root))
