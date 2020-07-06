#
"""
"""
import sys
input = sys.stdin.readline

sentence = list(input().rstrip())
while True:
    bd = 0
    sd = 0

    if sentence[i] == ']':
        bd += 1
    elif sentence[i] == ')':
        sd += 1
    elif sentence[i] == '[':
        bd -= 1
    elif sentence[i] == '(':
        sd -= 1

    if sd == -1 or bd == -1:
        print("no")

if bd == 0 and sd == 0:
    print("yes")
else:
    print("no")