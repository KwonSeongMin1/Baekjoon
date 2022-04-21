#https://www.acmicpc.net/problem/11651
import sys
input = sys.stdin.readline

n = int(input())
pos = []
for i in range(n):
    x,y = map(int,input().split())
    pos.append([y,x])
    
pos.sort()

for y,x in pos:
    print(x,y)