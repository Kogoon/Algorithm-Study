# 2020.01.26
#  모두의 알고리즘 with 파이썬/이승찬/길벗
#   절댓값 구하기 알고리즘. 
#    각각 abs_sign(a)와 abs_square(a)라는 파이썬 함수 이용.
#     abs_sign(a) : 부호로 판단하는 알고리즘
#     abs_square(a) : 제곱 후 제곱근을 구하여 절댓값을 구하는 알고리즘

# 1. a의 절댓값 구하기 알고리즘 - 부호판단.
#   - a가 0보다 크거나 같은지 확인 그렇다면 a를, 그렇지 않다면 -a를.
# 2. a의 절댓값 구하기 알고리즘 - 제곱 후 제곱근
#   - a를 제곱하여 변수 b에 저장.
#   - b를 제곱근을 구해 결과로 돌려준다.  

import math 

# 절댓값 알고리즘 1 (부호판단)
# 입력: 실수 a
# 출력: a의 절댓값. 

def abs_sign(a):
    if (a >= 0):
        return a
    else:
        return -a

# 절댓값 알고리즘 2 (제곱-제곱근)
# 입력: 실수 a
# 출력: a의 절댓값

def abs_square(a):
    b = a * a
    return math.sqrt(b) # math(수학) 모듈의 제곱근 함수

print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))
#abs_square 과 같은 결과가 나오는 이유는 math.sqrt(b)가 소수점이 붙은 값을 돌려주기 떄문.


