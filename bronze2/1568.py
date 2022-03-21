n = int(input());
k = 1;
res = 0;
count = 0;
while True:
    res = res + k;
    k = k + 1;
    count = count + 1;
    if res + k > n:
        k = 1;
    if n == res:
        break;
print(count)