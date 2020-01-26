# 2020.01.26
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
#   숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들어보세요.

# 입력: 숫자 n개를 리스트로
# 출력: 숫자 n개 중 최솟값

def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(n):
        if min_v > a[i]:
            min_v = a[i]
    return min_v

v = [17, 92, 8, 33, 45, 68, 18, 32]
print(find_min(v))