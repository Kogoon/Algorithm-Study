#-*- coding: utf-8 -*-
# 2020.03.17
"""
입력: 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
    둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어 있고 중복되지 않으며, 길이는 최대 100이다. 
출력: 첫째 줄에 그룹 단어의 개수를 출력한다. 
"""
"""
N = int(input())
words = []
for i in range(N):
    words.append(input())

alpha_compare = []
count = 0

for i in range(len(words)):
    for j in words[i]:
        alpha_compare.append(j)
        print(alpha_compare)
            
    alpha_compare = []
    print(alpha_compare)

print(count)

for i in range(len(words)):
    for j in words[i]:
        if j in alpha_compare:
            alpha_compare.append(j)
        else:
            break

    print(alpha_compare)
    alpha_compare = []
    print(alpha_compare)
"""
import sys 
input = sys.stdin.readline

def compareText(list):

    key = 0
    
    for _ in range(len(list)):
        
        comp = list[key]
        for i in range(key+2, len(list)-1):
            if comp == list[i]:
                return False
        key += 1    
    
    return True


N = int(input())
count = 0
for i in range(N):
    text = list(input().rstrip())
    result = compareText(text)
    if result is True:
        count += 1
print(count)

    