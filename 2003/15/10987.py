# 2020.03.15
"""
문제: 알파벳 소문자로만 이루어진 단어가 주어진다.
    이때, 모음 (a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.
입력: 첫째 줄에 단어가 주어진다.
    단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다. 
출력: 첫째 줄에 모음의 개수를 출력한다.
"""
# vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0
word = list(input())
for i in range(len(word)):
    if word[i] == "a":
        vowel_count += 1
    elif word[i] == "e":
        vowel_count += 1
    elif word[i] == "i":
        vowel_count += 1
    elif word[i] == "o":
        vowel_count += 1
    elif word[i] == "u":
        vowel_count += 1
    else:
        continue

print(vowel_count) 