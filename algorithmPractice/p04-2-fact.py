# 2020.01.29
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
#   팩토리얼을 구하는 알고리즘 2

# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))