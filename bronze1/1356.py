# https://www.acmicpc.net/problem/1356
# 11034 1 1034  11 034  110 34  1103 4
num=input()
flag,i=0,0
j = len(num)-1
num1 = int(num[i])
num2 = 1
for _ in range(1, len(num)):
    num2 *= int(num[_])

while i!=j:
    if num1 == num2:
        flag=1
    i+=1
    num1*=int(num[i])
    num2=1
    for _ in range(i+1, len(num)):
        num2 *= int(num[_])
if(flag):
    print("YES")
else:
    print("NO")