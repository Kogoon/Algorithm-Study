# 2020.07
"""
입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
    각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
    n은 양수이며 11보다 작다.
출력: 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
"""
# 1을 이용한건 항상 1개
# 2와 1만을 이용한건 피보나찌 수열로 증가 
# 3을 이용한건 ...
import sys 
input = sys.stdin.readline 

T = int(input())

for i in range(T):
    N = int(input())
    memo = []
    for j in range(N+1):
        
