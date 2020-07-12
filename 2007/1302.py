# 2020.07.13
"""
문제
김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

예제 입력 1 
5
top
top
top
top
kimtop

예제 출력 1 
top
"""
"""
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
books = []
book_name = []
counts = {}
for n in range(N):
    book = input().rstrip()
    books.append(book)
    if book not in book_name: book_name.append(book)

for name in books:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

count_books = list(Counter(books).values())
print(books, count_books, book_name, counts)
#['top', 'top', 'top', 'top', 'kimtop'] [4, 1] ['top', 'kimtop'] {'top': 4, 'kimtop': 1}
"""
"""
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
books = []
for n in range(N):
    book = input().rstrip()
    books.append(book)

count_books = list(Counter(books))

print(count_books)
"""

import sys
input = sys.stdin.readline

N = int(input())
counts = {}
books = []
for n in range(N):
    book = input().rstrip()
    books.append(book)

for name in books:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

_max = max(counts.values())
best_seller = []
print(_max)
for key, value in counts.items():
    if value == _max:
        best_seller.append(key)
print(sorted(best_seller)[0])
"""
import sys
input = sys.stdin.readline

books = {}
N = int(input())
for n in range(N):
    book = input().rstrip()
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1

temp = []
for key in books.keys():
    if books[key] == max(books.values()):
        temp.append(key)
temp.sort()
print(temp[0])
"""