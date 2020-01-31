# 2020.02.01
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
#   최대공약수를 구하는 알고리즘 

# 입력: a, b
# 출력: a와 b의 최대공약수

def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i 

        i = i - 1 # i를 1로 감소시킴 

print(gcd(1, 5))    #1
print(gcd(3, 6))    #3
print(gcd(60, 24))  #12
print(gcd(81, 27))  #27