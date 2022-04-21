#https://www.acmicpc.net/problem/11050

import sys
input = sys.stdin.readline

def factorial(x):
    if x<=1:
        return 1
    else:
        return x * factorial(x-1)
    
n,r = map(int,input().split())

print(int(factorial(n) / (factorial(r) * factorial(n-r))))