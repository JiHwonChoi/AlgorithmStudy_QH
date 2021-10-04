import sys

a, b = map(int,sys.stdin.readline().split(' '))
A=list(map(int,sys.stdin.readline().split(' ')))
B=list(map(int,sys.stdin.readline().split(' ')))
C=A^B
print(len(C))
