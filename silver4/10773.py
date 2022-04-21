#https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline


res = []
k = int(input())
for i in range(k):
    num = int(input())
    if num:
        res.append(num)
    else:
        res.pop()
print(sum(res))