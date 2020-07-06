# 2020.03.13
"""
acmicpc.net/problem/1181
문제: 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
    1. 길이가 짧은 것부터
    2. 길이가 같으면 사전 순으로
입력: 첫째 줄에 단어의 개수 N이 주어진다. (1 <= M <= 20,000) 
    둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
    주어지는 문자열의 길이는 50을 넘지 않는다. 
출력: 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러번 입력된 경우에는 한 번씩만 출력한다. 
"""
p_words = []
min_num, max_num = 0, 0
N = int(input())

for i in range(N):
    p_words.append(input())

p_words.sort()
print(p_words)
#  words_length = []
p_words.sort(key=len)
print(p_words)
print("----------------------------")
#print(len(p_words[-1]))

for i in range(N):
    if i > 1:
        if p_words[i] == p_words[i-1]:
            pass
        else:
            print(p_words[i])

    else:
        print(p_words[i])


