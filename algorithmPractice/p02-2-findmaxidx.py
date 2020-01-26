# 2020.01.26
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
#   최댓값의 위치를 구하는 알고리즘

# 입력: 숫자가 n개 들어있는 리스트
# 출력: 숫자 n개 중에서 최댓값이 있는 위치 (0부터 n-1까지의 값)

def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

v = [17, 92, 18, 33, 54, 7, 34, 42]
print(find_max_idx(v))