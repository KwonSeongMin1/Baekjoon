from re import X


p = int(input())
n = list(map(int,input().split()))
count = 0
n = sorted(n)
for i in range(0,p-1,1):
    if n[i] == n[i+1]:
        count = count + 1
print(count)