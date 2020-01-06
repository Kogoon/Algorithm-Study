# 2020.01.06
"""
acmicpc.net/problem/1924
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까?
    이를 알아내는 프로그램을 작성하시오.
입력: 첫째 줄에 빈 칸을 사이에 두고 x(1<=x<=12)와 y(1<=y<=31)이 주어진다.
    참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
출력: 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT 중 하나를 출력한다.
"""
# 1 1 이면 1월 1일 월요일. MON
# 그러면 1로 나누어 떨어지면 월요일, 7로 나누어 떨어지면 일요일... 이런식으로?
def daySearch(day):
    if(day%7==0):
        print("SUN")
    elif(day%7==1):
        print("MON")
    elif(day%7==2):
        print("TUE")
    elif(day%7==3):
        print("WED")
    elif(day%7==4):
        print("THU")
    elif(day%7==5):
        print("FRI")
    elif(day%7==6):
        print("SAT")
X, Y = map(int, input().split())
# 라고 생각했는데 월을 따로 받으니..
month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
#일수 저장. (단순)
Y = Y + month[X - 1]
daySearch(Y)

    

    