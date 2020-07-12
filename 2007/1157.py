# 2020.07.13
"""
acmicpc.net/problem/1157
문제: 알파벳 대소문자로 된 단어가 주어지면,
    이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
    단, 대문자와 소문자를 구분하지 않는다. 
입력: 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
출력: 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
    단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다. 
"""
#prob_word = list(str(input()))
#prob_word.sort(key=str.lower)

import sys
input = sys.stdin.readline

word = list(input().rstrip().upper())
count = [0] * 26
cnt = [0] * 26
a = 0
b = 0
for w in word:
    temp = ord(w)
    temp -= 65
    count[temp] += 1
    cnt[temp] += 1

cnt.sort(reverse=True)

if cnt[0] == cnt[1]:
    print("?")
else:
    for i in range(0, 26):
        if count[i] > a:
            a = count[i]
            b = i
    
    print(chr(b+65))
