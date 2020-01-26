# 2020.01.26
#  모두의 알고리즘 with 파이썬 / 이승찬 / 길벗
#   동명이인을 찾는 알고리즘

# 입력: 이름이 n개 들어 있는 리스트
# 출력: 이름 n개 중 반복되는 이름의 집합

def find_same_name(a):
    n = len(a)
    result = set()      # 결과를 저장할 빈 집합
    for i in range(0, n-1): # 첫번째 변수부터 n-2 변수까지 기준
        for j in range(i + 1, n): # 두번째 변수부터 n-1까지 기준과 대조
            if a[i] == a[j]:
                result.add(a[i])
    return result

    
name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))
