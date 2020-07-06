#
"""
"""
import sys 
input = sys.stdin.readline

pattern = [['*','*','*'],
           ['*',' ','*'],
           ['*','*','*']]

N = int(input())

A = [['*' for col in range(N)] for row in range(N)]

print(len(A))