n,m,l = map(int,input().split())
a = [1]
count = 0
lnum = 0
for i in range(1,n,1):
    a.append(0)
while True:
    if a[lnum % n] == m:
        break
    if a[lnum%n]%2 == 0:
        lnum = lnum + l
        a[lnum%n] = a[lnum%n] + 1
    else:
        lnum = lnum - l
        a[lnum%n] = a[lnum % n] + 1
    count = count + 1
print(count)
