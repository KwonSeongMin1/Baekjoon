#https://www.acmicpc.net/problem/1920
a = int(input())
n1 = list(map(int,input().split()))
n1.sort()
b = int(input())
n2 = list(map(int,input().split()))

min = n1[0]
max = n1[-1]

def judge(min,max,n2):
    
        