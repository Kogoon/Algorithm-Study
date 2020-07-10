# 2020.07.10
"""
"""
from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())
"""
for _ in range(T):
    cnt = 0
    count_value = {}
    many_clothes = int(input())
    clothes = dict(input().split() for dict_count in range(many_clothes))
    clothes_list = list(clothes.keys())
    clothes_kind = list(clothes.values())
    for i in clothes_kind:
        try: count_value[i] += 1
        except: count_value[i] = 1
    a = list(count_value.values())
    if len(a) == 1:
        print(len(clothes_list))
    else:
        cnt += a[0] + 1
        for j in range(1, len(a)):
            cnt *= a[j] + 1
        print(cnt - 1)
"""
for t in range(T):
    clothes = []
    count = int(input())
    for i in range(count):
        a, b = input().split()
        clothes.append(b)
    result = 1
    count_clothes = list(Counter(clothes).values())
    #print(count_clothes)
    for cnt in range(len(count_clothes)):
        result *= count_clothes[cnt] + 1
    print(result -1)

    


        