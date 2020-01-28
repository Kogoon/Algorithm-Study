# 2020.01.29
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
"""
문제: 1부터 n까지의 합 구하기를 재귀 호출로 만들어 보세요.
입력: n
출력: 1부터 n까지의 합
"""

def fact(n):
    f = 0
    for i in range(1, n+1):
        f = f + i

    return f

def fact_r(n):
    if n <= 1:
        return 1
    return n + fact_r(n-1) 

print(fact(1))
print(fact(5))
print(fact(10))

print(fact_r(1))
print(fact_r(5))
print(fact_r(10))

print("==============================")