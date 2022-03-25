#https://www.acmicpc.net/problem/1032

num = int(input())
res_file = list(input())
for i in range(num-1):
    file = input()
    for j in range(len(file)):
        if ord(res_file[j]) - ord(file[j]) != 0:
            res_file[j] = '?'
print(''.join(res_file))