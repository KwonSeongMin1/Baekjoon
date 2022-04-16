#https://www.acmicpc.net/problem/13706
n = int(input())

min = 1    #최소
max = n   #최대

def judge(n,m,k):
    min = n
    max = m
    n = k
    mid = (min+max)//2
    if mid**2 == n:
        return mid
    elif mid**2 > n:
        judge(min,mid,n)
    else:
        judge(mid,max,n)

print(judge(min,max,n))

