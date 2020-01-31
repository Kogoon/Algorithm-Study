# 2020.02.01
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
#   유클리드 방식을 이용해 최대공약수를 구하는 알고리즘
#    - a와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'의 최대공약수와 같습니다.
#      즉, gcd(a, b) = gcd(b, a%b)
#    - 어떤 수와 0의 최대

# 입력: a, b
# 출력: a와 b의 최대공약수 

def gcd(a, b):
    if b == 0:          # b가 0이면 종료
        return a
    return gcd(b, a%b)  # 좀 더 작은 값으로 자기 자신 호출

print(gcd(1, 5))    # 1
print(gcd(3, 6))    # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27

