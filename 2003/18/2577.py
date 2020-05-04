# 2020.03.18
"""
acmicpc.net/problem/2577
문제: 세 개의 자연수 A, B, C가 주어질 때 AxBxC를 계산한 결과에 
    0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오
입력: 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. 
    A, B, C는 모두 100보다 같거나 크고, 1,000보다 작은 자연수이다.
출력: 첫째 줄에는 AxBxC의 결과에 0이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지
    AxBxC의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
"""
A = int(input())
B = int(input())
C = int(input())
ABC_multi = list(str(A * B * C))
ABC_multi = [int(i) for i in ABC_multi]
"""
# 사용된 숫자만 요구한다면... 근데 그게 아니라 1부터 9까지...
count = {}
for i in ABC_multi:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

print(count)
"""
count = [0 for i in range(10)]

for i in range(10):
    for j in ABC_multi:
        if j == i:
            count[i] += 1
        
for i in range(10):
    print(count[i])

    