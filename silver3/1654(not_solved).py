k,n = map(int,input().split())
lanSum = 0
num = [0 for _ in range(k)]
for _ in range(k):
    num[_] = int(input())
    lanSum += num[_]
lanSum //= n
while True:
    flag = 0
    for i in range(k):
        flag += num[i] // lanSum
    if n >= flag:
        break
    else:
        lanSum -= 1
print(lanSum)
