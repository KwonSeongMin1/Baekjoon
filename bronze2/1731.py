#https://www.acmicpc.net/problem/1731
N = int(input())
flag = True
num = []
for i in range(N):
    n = int(input())
    num.append(n)
    if i == 2:
        p = num[2] - num[1]
        q = num[1] - num[0]
        if p != q:
            p = int(num[2] / num[1])
            flag = False
if flag:
    print(num[N-1] + p)
else:
    print(num[N-1] * p)
