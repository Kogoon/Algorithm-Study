# 2020.02.02
"""
acmicpc.net/problem/1697
문제:
입력: 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
출력: 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""
def find_her(N, K):
    find_time = 0
    """
    if N == K:
        return find_time
    """
    while True:
        if N > K:
            N -= 1
        
        if N == K:
            return find_time

        if N < K:
            if N * 2 <= K:
                N = N * 2
            else:
                N -= 1 

        find_time += 1

N, K = map(int, input().split())
print(find_her(N, K))
