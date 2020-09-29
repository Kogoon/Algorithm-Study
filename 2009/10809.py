# 2020.09.29
"""
acmicpc.net/problem/10809
"""
import sys
input = sys.stdin.readline

S = list(input().rstrip())
alpha = [-1] * 26
saving = []

for i in range(len(S)):
  temp = ord(S[i]) - 97
  saving.append(temp)

for j in range(len(saving)):
  temp = saving[j]
  if alpha[temp] != -1:
    continue
  alpha[temp] = j

for k in range(len(alpha)):
  print(alpha[k], end=" ")
  

"""
인턴(회사)에 8시 30분까지 출근하고 30분동안 생각하고 풀어본 문제. 
2달만에 알고리즘 문제를 접해봤다. 
포문을 여러개 써서 좋은 알고리즘 같지는 않다. 
알고리즘 여전히 어려운데 여러번 연습하고 앞으로도 출근하고 조금의 시간 할애해서 
알고리즘 문제 푸는 시간을 갖도록 해야겠다. 
"""
