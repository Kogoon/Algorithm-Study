"""
문제규칙: - 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
         - 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
         - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다. 
        사과의 위치와 뱀의 이동경로가 주어질 때, 이 게임이 몇 초에 끝나는지 계산하라.
입력: 첫째 줄에 보드의 크기 N이 주어진다. 다음 줄에 사과의 개수 K가 주어진다.
    다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨위 맨 좌측에는 사과가 없다. 
    다음줄에는 뱀의 방향 변환 횟수 L이 주어진다. 
    다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며, 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽 (C가 'L') 또는 오른쪽 (C가 'D')로 
    90도 방향을 회전시킨다는 뜻이다. 
"""
time = 0

N = int(input())
K = int(input())

array = [[0 for col in range(N)] for row in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    array[x][y] = 1

L = int(input())
n_time = []
direction = []
for _ in range(L):
    t, d = input().split()
    n_time.append(t)
    direction.append(d)

X, Y = 0, 0
while True:
    if X == N:
        break
    snake_queue = array[X][Y]
    X += 1
    time += 1
    
print(time)
