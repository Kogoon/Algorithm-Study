#
# 자료구조(참고)
"""
acmicpc.net/problem/10808
문제: 알파벳 소문자로만 이루어진 단어 S가 주어진다.
    각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
입력: 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
출력: 단어에 포함되어 있는 a의 개수, b의 개수, ..., z의 개수를 공백으로 구분해서 출력한다. 
"""
# 알파벳 개수
s = list(input())
c = [0 for x in range(26)]
#print(s)
for i in range(len(s)):
    s[i] = ord(s[i]) - 97

#print(s)
#print(c)

for i in range(0, 26):
    for j in range(len(s)):
        if i == s[j]:
            c[i] = c[i] + 1

#print(c)

for y in range(len(c)):
    print(c[y], end=" ")