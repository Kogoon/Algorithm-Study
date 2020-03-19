import sys
input = sys.stdin.readline


def fibonacci(n):
    global zero, one
    if(n == 0):
        zero = zero + 1
        return 0
    elif(n == 1):
        one = one + 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

T = int(input())
for i in range(T):
    zero, one = 0, 0
    a = int(input())
    fibonacci(a)
    print(zero, one)
