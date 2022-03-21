N,L = input().split()
num, count = 0,0
while count < int(N):
    num = num+1
    if L not in str(num):
        count=count+1
print(num)