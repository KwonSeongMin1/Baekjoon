#https://www.acmicpc.net/problem/23882

n,k = map(int,input().split())
count = 0
a = list(map(int,input().split()))
b = sorted(a)

for i in range(len(a)-1,0,-1):  
    if b[i] != a[i]:
        a[a.index(b[i])] = a[i]
        a[i] = b[i]
        count = count + 1
    if count == k:
        break;

if count < k:
    print(-1)
else:  
    print(' '.join(map(str,a)))
