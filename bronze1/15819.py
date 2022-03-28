# https://www.acmicpc.net/problem/15819

n,i = map(int,input().split())

handle = []

for count in range(0,n):
    h = input()
    handle.append(h)  
    handle.sort()
print(handle[i-1])