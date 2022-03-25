#https://www.acmicpc.net/problem/24049

N,M = map(int,input().split())
flower = [[0] * (M+1) for _ in range(N+1)]

num_list = list(map(int,input().split()))
for i in range(N):
    flower[i+1][0] = num_list[i]
num_list = list(map(int, input().split()))
for i in range(N):
    flower[0][i+1] = num_list[i]
    
print(flower)