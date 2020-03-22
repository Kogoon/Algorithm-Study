# 2020.03.22
"""
acmicpc.net/problem/1406
문제:   L   : 커서를 왼쪽으로 한 칸 옮김 (맨앞이면 무시)
        D   : 커서를 오른쪽으로 한 칸 옮김 (맨 뒤면 무시)
        B   :   커서 왼쪽에 있는 문자를 삭제함. 
        P # :   #이라는 문자를 커서 왼쪽에 추가함. 
입력: 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며 길이는 100,000을 넘지 않는다.
    둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다.
    명령어는 위의 네 가지중 하나의 형태로만 주어진다.
출력: 첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다. 
"""
import sys
input = sys.stdin.readline

Left_st = list(input().rstrip())
Right_st = []

N = int(input())
for i in range(N):
    cmd = []
    cmd = list(input().split())
    if cmd[0] == "L":
        if not Left_st:
            continue
        Right_st.append(Left_st.pop())
    elif cmd[0] == "D":
        if not Right_st:
            continue
        Left_st.append(Right_st.pop(0))
    elif cmd[0] == "B":
        if not Left_st:
            continue
        Left_st.pop()
    elif cmd[0] == "P":
        Left_st.append(cmd[1])

for i in Left_st:
    print(i, end="")

for i in Right_st:
    print(Right_st.pop(0))
