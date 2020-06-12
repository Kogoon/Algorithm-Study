#
"""
문제: 양수와 +. - 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고나서 세준이는 괄호를 모두 지웠다. 
    그리고 세준이는 괄호를 적절히 써서 이 식의 값을 최소로 만들려고 한다. 
    괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오. 
입력: 첫째 줄베 식이 주어진다. 식은 '0'~'9','+' 그리고 '-'만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
    그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
출력: 첫째 줄에 정답을 출력한다. 
"""
import sys
input = sys.stdin.readline

prob = list(input())
prob_r = []
prob_rr = []
sum = 0
ans = 0
i_am_str = ""

for i in prob:
    if i == '-' or i =='+':
        prob_r.append(i_am_str)
        prob_r.append(i)
        i_am_str = ""
    elif i == '\n':
        prob_r.append(i_am_str)
    else:
        i_am_str += i

for j in prob_r:
    if j=='-':
        prob_rr.append(sum)
        sum = 0
        continue
    if j=='+':
        continue
    sum += int(j)

prob_rr.append(sum)      
ans += prob_rr.pop(0)

for _ in prob_rr:
    ans -= _

print(ans)
