#https://www.acmicpc.net/problem/1145

num = list(map(int,input().split()))
num.sort()
res = 1
while True:
    count = 0
    for i in range(5):
        if res % num[i] == 0:
            count = count + 1
    if count >= 3:
        break
    res = res+1
print(res)