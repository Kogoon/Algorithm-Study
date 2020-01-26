# 2020.01.26
#  모두의 알고리즘 with 파이썬/이승찬/길벗
#   최댓값을 구하는 알고리즘 

# 입력: 숫자가 n개 들어있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))