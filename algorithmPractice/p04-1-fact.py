# 2020.01.29
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
#   팩토리얼을 구하는 알고리즘 1

# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


print(fact(1))
print(fact(5))
print(fact(10))